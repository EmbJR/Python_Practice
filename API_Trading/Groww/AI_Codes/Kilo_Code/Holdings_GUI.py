"""
Groww API - Holdings GUI
========================
A tkinter-based GUI to display holdings and sell selected stocks.

Author: Kilo Code
Platform: Groww
"""

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import time
from datetime import datetime
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Import growwapi directly
from growwapi import GrowwAPI


# Color scheme for the GUI
class GUIColors:
    HEADER_BG = "#1a1a2e"
    HEADER_FG = "#ffffff"
    BG_COLOR = "#16213e"
    FG_COLOR = "#eaeaea"
    GREEN = "#00ff88"
    RED = "#ff4757"
    YELLOW = "#ffa502"
    BLUE = "#3742fa"
    PURPLE = "#9c88ff"
    BUTTON_BG = "#0f3460"
    BUTTON_HOVER = "#1e5f74"
    TABLE_BG = "#1f1f38"
    TABLE_SELECT = "#2d2d5a"


# Configuration - Use token from AGENTS.md
API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3NzE1NDc0MDAsImlhdCI6MTc3MTQ4MDU0OSwibmJmIjoxNzcxNDgwNTQ5LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCI0YjZkODRhNi0zYmE2LTQ1ODAtODFlYS03MGM5ZjY2YmVkYmJcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjIxMjY3MTU4LTgyODAtNDY2ZS1iZWZlLTRmZWE3NzA5MDU3NFwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOjcxOTQ6ZTZjNTo4ZDMxOmVjMGMsMTYyLjE1OC4xOTEuMTg5LDM1LjI0MS4yMy4xMjNcIixcInR3b0ZhRXhwaXJ5VHNcIjoxNzcxNTQ3NDAwMDAwfSIsImlzcyI6ImFwZXgtYXV0aC1wcm9kLWFwcCJ9.mSTdqvAXI8tRWwglKdY-RHYA8oZpDw00S41hpNuHtgbUhPuFh1l1G1uX4i8GqKe4svCHL9CeXJU5I5aDCIHuKQ"

# Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)


def get_current_price(symbol, exchange="NSE"):
    """Get the Last Traded Price (LTP) for a given symbol."""
    # Skip if symbol is None, empty, or 'None' string
    if not symbol or symbol == 'None' or str(symbol).strip() == '':
        return None
    
    # Try primary exchange first, then try alternate if failed
    exchanges_to_try = [exchange]
    if exchange == 'NSE':
        exchanges_to_try.append('BSE')
    else:
        exchanges_to_try.append('NSE')
    
    for exch in exchanges_to_try:
        try:
            ltp_symbol = f"{exch}_{symbol}"
            ltp_response = groww.get_ltp(
                exchange_trading_symbols=ltp_symbol,
                segment=groww.SEGMENT_CASH
            )
            #print("-----------DB6------------")
            current_price = float(float(ltp_response[ltp_symbol]))
            return current_price
        except Exception as e:
            # If first exchange failed, try the alternate one
            if exch == exchanges_to_try[0]:
                continue
            # Both exchanges failed
            print(f"Error getting LTP for {symbol}: {e}")
            return None


def _fetch_single_ltp(args):
    """Helper function to fetch LTP for a single symbol (used for parallel execution)."""
    symbol, exchange = args
    return symbol, exchange, get_current_price(symbol, exchange)


def get_current_prices_parallel(symbols_exchanges_list):
    """
    Get LTP for multiple symbols in parallel using ThreadPoolExecutor.
    
    Args:
        symbols_exchanges_list: List of tuples [(symbol, exchange), ...]
    
    Returns:
        Dictionary mapping symbol to current price
    """
    if not symbols_exchanges_list:
        return {}
    
    prices = {}
    
    # Use ThreadPoolExecutor to fetch LTP in parallel
    # Adjust max_workers based on API rate limits
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all tasks
        future_to_symbol = {
            executor.submit(_fetch_single_ltp, (symbol, exchange)): (symbol, exchange)
            for symbol, exchange in symbols_exchanges_list
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_symbol):
            try:
                symbol, exchange, price = future.result()
                prices[symbol] = price
            except Exception as e:
                symbol, exchange = future_to_symbol[future]
                print(f"Error fetching LTP for {symbol}: {e}")
                prices[symbol] = None
    
    return prices


def sell_stock(symbol, quantity, exchange="NSE"):
    """Sell stock from holdings."""
    try:
        trading_symbol = f"{exchange}_{symbol}"
        quantity = int(float(quantity))
        
        current_price = get_current_price(symbol, exchange)
        
        if current_price is None:
            print(f"  [ERROR] Could not get current price for {symbol}")
            return False, None
        
        # Place sell order (CNC for delivery)
        order_response = groww.place_order(
            segment=groww.SEGMENT_CASH,
            trading_symbol=trading_symbol,
            exchange=groww.EXCHANGE_NSE if exchange == "NSE" else groww.EXCHANGE_BSE,
            transaction_type=groww.TRANSACTION_TYPE_SELL,
            quantity=quantity,
            product=groww.PRODUCT_CNC,
            order_type=groww.ORDER_TYPE_MARKET,
            validity=groww.VALIDITY_DAY
        )
        
        print(f"  [SUCCESS] Sold {quantity} shares of {symbol} at ~Rs.{current_price}")
        time.sleep(1)
        return True, current_price
        
    except Exception as e:
        print(f"  [ERROR] Failed to sell {symbol}: {e}")
        return False, None


class HoldingsGUI:
    """Main GUI class for Holdings Monitor"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Groww Holdings Monitor")
        self.root.geometry("1200x600")
        self.root.configure(bg=GUIColors.BG_COLOR)
        
        self.holdings_data = []
        self.sell_quantities = {}
        self.refresh_interval = 1000  # 1 second auto-refresh
        self.is_running = True
        self.auto_refresh_enabled = True
        self.is_refreshing = False  # Flag to prevent concurrent refreshes
        
        # Create GUI
        self.create_header()
        self.create_control_panel()
        self.create_table()
        self.create_status_bar()
        
        # Start refresh
        self.trigger_refresh()
        # Start auto-refresh every 1 second
        self.auto_refresh()
    
    def auto_refresh(self):
        """Automatically refresh holdings every 1 second."""
        if self.auto_refresh_enabled:
            self.trigger_refresh()
        self.root.after(self.refresh_interval, self.auto_refresh)
    
    def create_header(self):
        header_frame = tk.Frame(self.root, bg=GUIColors.HEADER_BG, height=50)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="GROWW HOLDINGS MONITOR",
            font=('Consolas', 14, 'bold'),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.HEADER_FG
        ).pack(side=tk.LEFT, padx=20)
        
        self.time_label = tk.Label(
            header_frame,
            text="",
            font=('Consolas', 10),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.YELLOW
        )
        self.time_label.pack(side=tk.RIGHT, padx=20)
        self.update_time()
    
    def update_time(self):
        self.time_label.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if self.is_running:
            self.root.after(1000, self.update_time)
    
    def create_control_panel(self):
        control_frame = tk.Frame(self.root, bg=GUIColors.BG_COLOR)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(
            control_frame,
            text="Refresh",
            font=('Consolas', 10),
            bg=GUIColors.BUTTON_BG,
            fg=GUIColors.HEADER_FG,
            command=self.trigger_refresh,
            padx=15
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Label(
            control_frame,
            text="Enter qty to sell:",
            font=('Consolas', 10),
            bg=GUIColors.BG_COLOR,
            fg=GUIColors.PURPLE
        ).pack(side=tk.LEFT, padx=(20, 5))
        
        self.summary_label = tk.Label(
            control_frame,
            text="",
            font=('Consolas', 10),
            bg=GUIColors.BG_COLOR,
            fg=GUIColors.YELLOW
        )
        self.summary_label.pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            control_frame,
            text="SELL SELECTED",
            font=('Consolas', 11, 'bold'),
            bg=GUIColors.RED,
            fg=GUIColors.HEADER_FG,
            command=self.sell_selected,
            padx=20
        ).pack(side=tk.RIGHT, padx=5)
    
    def create_table(self):
        table_frame = tk.Frame(self.root, bg=GUIColors.BG_COLOR)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        y_scroll = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ('symbol', 'company', 'qty', 'avg_price', 'current_price', 
                   'invested', 'current_value', 'pnl', 'pnl_pct')
        
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show='headings',
            yscrollcommand=y_scroll.set,
            selectmode='browse'
        )
        y_scroll.config(command=self.tree.yview)
        
        # Configure columns
        self.tree.heading('symbol', text='Symbol')
        self.tree.column('symbol', width=80, anchor='center')
        
        self.tree.heading('company', text='Company')
        self.tree.column('company', width=150, anchor='w')
        
        self.tree.heading('qty', text='Qty')
        self.tree.column('qty', width=60, anchor='center')
        
        self.tree.heading('avg_price', text='Avg Price')
        self.tree.column('avg_price', width=90, anchor='e')
        
        self.tree.heading('current_price', text='Current')
        self.tree.column('current_price', width=90, anchor='e')
        
        self.tree.heading('invested', text='Invested')
        self.tree.column('invested', width=100, anchor='e')
        
        self.tree.heading('current_value', text='Value')
        self.tree.column('current_value', width=100, anchor='e')
        
        self.tree.heading('pnl', text='P&L')
        self.tree.column('pnl', width=90, anchor='e')
        
        self.tree.heading('pnl_pct', text='%')
        self.tree.column('pnl_pct', width=60, anchor='e')
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Tags for colors
        self.tree.tag_configure('profit', foreground=GUIColors.GREEN)
        self.tree.tag_configure('loss', foreground=GUIColors.RED)
        
        # Bind selection
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
        
        # Input frame below table
        input_frame = tk.Frame(self.root, bg=GUIColors.BG_COLOR)
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            input_frame,
            text="Sell Quantity:",
            font=('Consolas', 10),
            bg=GUIColors.BG_COLOR,
            fg=GUIColors.FG_COLOR
        ).pack(side=tk.LEFT, padx=5)
        
        self.qty_entry = tk.Entry(
            input_frame,
            font=('Consolas', 11),
            width=10
        )
        self.qty_entry.pack(side=tk.LEFT, padx=5)
        self.qty_entry.bind('<KeyRelease>', self.on_qty_change)
        
        self.selected_info_label = tk.Label(
            input_frame,
            text="Select a holding from table",
            font=('Consolas', 10),
            bg=GUIColors.BG_COLOR,
            fg=GUIColors.PURPLE
        )
        self.selected_info_label.pack(side=tk.LEFT, padx=20)
    
    def create_status_bar(self):
        status_frame = tk.Frame(self.root, bg=GUIColors.HEADER_BG, height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.total_pnl_label = tk.Label(
            status_frame,
            text="Total P&L: Rs.0.00",
            font=('Consolas', 10, 'bold'),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.YELLOW
        )
        self.total_pnl_label.pack(side=tk.LEFT, padx=20)
        
        self.portfolio_label = tk.Label(
            status_frame,
            text="Value: Rs.0.00",
            font=('Consolas', 10),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.PURPLE
        )
        self.portfolio_label.pack(side=tk.LEFT, padx=20)
        
        self.count_label = tk.Label(
            status_frame,
            text="Holdings: 0",
            font=('Consolas', 10),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.FG_COLOR
        )
        self.count_label.pack(side=tk.RIGHT, padx=20)
    
    def trigger_refresh(self):
        """Trigger a refresh in a separate thread if not already refreshing."""
        if not self.is_refreshing:
            threading.Thread(target=self.refresh_thread, daemon=True).start()
    
    def refresh_thread(self):
        """Fetch holdings and update the display."""
        self.is_refreshing = True
        try:
            holdings_response = groww.get_holdings_for_user()
            holdings_df = pd.DataFrame(holdings_response['holdings'])
            
            # Filter out rows with invalid/None symbols early to avoid unnecessary processing
            holdings_df = holdings_df[holdings_df['trading_symbol'].notna()]
            holdings_df = holdings_df[holdings_df['trading_symbol'] != 'None']
            holdings_df = holdings_df[holdings_df['trading_symbol'].str.strip() != '']
            
            #StockNames = holdings_df['trading_symbol'].tolist()
            print("-----------DB1------------")
            
            if holdings_df.empty:
                self.root.after(0, self.show_empty)
                return
            
            results = []
            
            # First pass: collect all symbols and their exchanges
            symbols_exchanges_list = []
            holdings_with_info = []
            
            for _, row in holdings_df.iterrows():
                try:
                    raw_symbol = row.get('trading_symbol', '')
                    if not raw_symbol or raw_symbol == 'None':
                        print("-----------DB2------------")
                        continue
                    
                    symbol = str(raw_symbol)
                    exchange = 'NSE'
                    
                    # Check tradable_exchanges field for correct exchange
                    tradable_exchanges = row.get('tradable_exchanges', '')
                    if tradable_exchanges:
                        if 'BSE' in str(tradable_exchanges):
                            exchange = 'BSE'
                        elif 'NSE' in str(tradable_exchanges):
                            exchange = 'NSE'
                    
                    # Remove exchange prefix from symbol for LTP lookup
                    if 'BSE_' in symbol:
                        exchange = 'BSE'
                        symbol = symbol.replace('BSE_', '')
                    elif 'NSE_' in symbol:
                        symbol = symbol.replace('NSE_', '')
                    
                    #print("-----------DB5------------")
                    # Skip if symbol is empty after processing
                    if not symbol or symbol.strip() == '':
                        print(f"Skipping row with empty symbol after processing")
                        print("-----------DB3------------")
                        continue
                    
                    quantity = int(row.get('quantity', 0))
                    if quantity <= 0:
                        print("-----------DB4------------")
                        continue
                    
                    avg_price = float(row.get('average_price', 0))
                    company_name = str(row.get('tradable_symbol', symbol)) if row.get('tradable_symbol') else str(symbol)
                    
                    # Collect symbol and exchange for parallel LTP fetch
                    symbols_exchanges_list.append((symbol, exchange))
                    
                    # Store other info for later use
                    holdings_with_info.append({
                        'symbol': symbol,
                        'company': company_name,
                        'quantity': quantity,
                        'avg_price': avg_price,
                        'exchange': exchange
                    })
                    
                except Exception as e:
                    print(f"Error processing row: {e}")
                    continue
            
            # Fetch all LTPs in parallel
            print(f"Fetching LTP for {len(symbols_exchanges_list)} symbols in parallel...")
            ltp_prices = get_current_prices_parallel(symbols_exchanges_list)
            
            # Second pass: calculate P&L using fetched prices
            for holding in holdings_with_info:
                try:
                    symbol = holding['symbol']
                    exchange = holding['exchange']
                    quantity = holding['quantity']
                    avg_price = holding['avg_price']
                    company_name = holding['company']
                    
                    current_price = ltp_prices.get(symbol)
                    if current_price is None:
                        current_price = avg_price
                    
                    invested = avg_price * quantity
                    current_value = current_price * quantity
                    pnl = (current_price - avg_price) * quantity
                    pnl_percent = ((current_price / avg_price) - 1) * 100 if avg_price > 0 else 0
                    
                    results.append({
                        'symbol': symbol,
                        'company': company_name,
                        'quantity': quantity,
                        'avg_price': round(avg_price, 2),
                        'current_price': round(current_price, 2),
                        'invested': round(invested, 2),
                        'current_value': round(current_value, 2),
                        'pnl': round(pnl, 2),
                        'pnl_percent': round(pnl_percent, 2),
                        'exchange': exchange
                    })
                    
                except Exception as e:
                    print(f"Error calculating P&L: {e}")
                    continue
            
            self.holdings_data = results
            self.root.after(0, self.update_display)
            
        except Exception as e:
            print(f"Error fetching: {e}")
            error_msg = str(e)
            self.root.after(0, lambda msg=error_msg: self.show_error(msg))
        finally:
            self.is_refreshing = False
    
    def show_empty(self):
        self.count_label.config(text="Holdings: 0")
        self.total_pnl_label.config(text="Total P&L: Rs.0.00")
        self.portfolio_label.config(text="Value: Rs.0.00")
        self.selected_info_label.config(text="No holdings found")
    
    def show_error(self, msg):
        self.selected_info_label.config(text=f"Error: {msg}")
    
    def update_display(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for h in self.holdings_data:
            tag = 'profit' if h['pnl'] >= 0 else 'loss'
            company = h.get('company') or h.get('symbol') or ''
            company_display = company[:20] + '...' if len(company) > 20 else company
            self.tree.insert('', 'end', values=(
                h['symbol'],
                company_display,
                h['quantity'],
                f"{h['avg_price']:.2f}",
                f"{h['current_price']:.2f}",
                f"{h['invested']:.2f}",
                f"{h['current_value']:.2f}",
                f"{h['pnl']:.2f}",
                f"{h['pnl_percent']:.2f}%"
            ), tags=(tag,), iid=h['symbol'])
        
        self.update_totals()
    
    def update_totals(self):
        total_invested = sum(h['invested'] for h in self.holdings_data)
        total_value = sum(h['current_value'] for h in self.holdings_data)
        total_pnl = sum(h['pnl'] for h in self.holdings_data)
        
        self.count_label.config(text=f"Holdings: {len(self.holdings_data)}")
        self.portfolio_label.config(text=f"Value: Rs.{total_value:,.2f}")
        
        if total_pnl >= 0:
            self.total_pnl_label.config(text=f"Total P&L: Rs.{total_pnl:,.2f}", fg=GUIColors.GREEN)
        else:
            self.total_pnl_label.config(text=f"Total P&L: -Rs.{abs(total_pnl):,.2f}", fg=GUIColors.RED)
    
    def on_select(self, event):
        selection = self.tree.selection()
        if not selection:
            self.selected_info_label.config(text="Select a holding from table")
            return
        
        symbol = selection[0]
        holding = next((h for h in self.holdings_data if h['symbol'] == symbol), None)
        
        if holding:
            self.selected_info_label.config(
                text=f"{holding['symbol']} - {holding['quantity']} shares available"
            )
            self.qty_entry.delete(0, tk.END)
            self.qty_entry.insert(0, str(holding['quantity']))
    
    def on_qty_change(self, event):
        selection = self.tree.selection()
        if not selection:
            return
        
        symbol = selection[0]
        try:
            qty = int(self.qty_entry.get())
            holding = next((h for h in self.holdings_data if h['symbol'] == symbol), None)
            
            if holding:
                if qty < 0:
                    qty = 0
                elif qty > holding['quantity']:
                    qty = holding['quantity']
                
                if qty > 0:
                    self.sell_quantities[symbol] = qty
                elif symbol in self.sell_quantities:
                    del self.sell_quantities[symbol]
                
                total_value = sum(
                    self.sell_quantities.get(h['symbol'], 0) * h['current_price']
                    for h in self.holdings_data
                )
                self.summary_label.config(text=f"Sell Value: Rs.{total_value:,.2f}")
        except ValueError:
            pass
    
    def sell_selected(self):
        if not self.sell_quantities:
            messagebox.showwarning("No Selection", "Select a holding and enter quantity to sell")
            return
        
        holdings_to_sell = []
        for h in self.holdings_data:
            if h['symbol'] in self.sell_quantities:
                qty = self.sell_quantities[h['symbol']]
                if qty > 0:
                    holdings_to_sell.append({**h, 'sell_qty': qty})
        
        if not holdings_to_sell:
            messagebox.showwarning("No Selection", "Enter quantity to sell")
            return
        
        total_value = sum(h['sell_qty'] * h['current_price'] for h in holdings_to_sell)
        
        confirm = f"Sell {sum(h['sell_qty'] for h in holdings_to_sell)} shares?\n\n"
        confirm += f"Total: Rs.{total_value:,.2f}\n\n"
        for h in holdings_to_sell:
            confirm += f"- {h['symbol']}: {h['sell_qty']} @ Rs.{h['current_price']:.2f}\n"
        
        if not messagebox.askyesno("Confirm", confirm):
            return
        
        # Sell
        sold = []
        failed = []
        
        for h in holdings_to_sell:
            success, _ = sell_stock(h['symbol'], h['sell_qty'], h['exchange'])
            if success:
                sold.append(h['symbol'])
            else:
                failed.append(h['symbol'])
            time.sleep(1)
        
        msg = f"Sold: {len(sold)}\n"
        if failed:
            msg += f"Failed: {len(failed)}"
        messagebox.showinfo("Done", msg)
        
        self.sell_quantities.clear()
        self.trigger_refresh()
    
    def on_closing(self):
        self.is_running = False
        self.root.destroy()


def main():
    root = tk.Tk()
    app = HoldingsGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
