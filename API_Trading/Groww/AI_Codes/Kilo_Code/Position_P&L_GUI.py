"""
Groww API - Position P&L GUI
============================
A tkinter-based GUI to display open positions with P&L and exit selected positions.

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


# Configuration - Same as original file
API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3NzE1NDc0MDAsImlhdCI6MTc3MTQ4MDU0OSwibmJmIjoxNzcxNDgwNTQ5LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCI0YjZkODRhNi0zYmE2LTQ1ODAtODFlYS03MGM5ZjY2YmVkYmJcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjIxMjY3MTU4LTgyODAtNDY2ZS1iZWZlLTRmZWE3NzA5MDU3NFwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOjcxOTQ6ZTZjNTo4ZDMxOmVjMGMsMTYyLjE1OC4xOTEuMTg5LDM1LjI0MS4yMy4xMjNcIixcInR3b0ZhRXhwaXJ5VHNcIjoxNzcxNTQ3NDAwMDAwfSIsImlzcyI6ImFwZXgtYXV0aC1wcm9kLWFwcCJ9.mSTdqvAXI8tRWwglKdY-RHYA8oZpDw00S41hpNuHtgbUhPuFh1l1G1uX4i8GqKe4svCHL9CeXJU5I5aDCIHuKQ"

# Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)

# Brokerage charges
BROKERAGE_CHARGE = 0
STT_CHARGE = 0.00025
GST_RATE = 0.18
SEBI_CHARGE = 0.000001
STAMP_DUTY = 0.0001
NSE_EXCHANGE_CHARGE = 0.0000135
BSE_EXCHANGE_CHARGE = 0.0000135


def get_current_price(symbol, exchange="NSE"):
    """Get the Last Traded Price (LTP) for a given symbol."""
    try:
        ltp_symbol = f"{exchange}_{symbol}"
        ltp_response = groww.get_ltp(
            exchange_trading_symbols=ltp_symbol,
            segment=groww.SEGMENT_CASH
        )
        current_price = float(float(ltp_response[ltp_symbol]))
        return current_price
    except Exception as e:
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


def calculate_charges(quantity, price, is_buy, exchange="NSE"):
    """Calculate all applicable charges for a trade."""
    trade_value = quantity * price
    brokerage = BROKERAGE_CHARGE * trade_value
    exchange_charge = (NSE_EXCHANGE_CHARGE if exchange == "NSE" else BSE_EXCHANGE_CHARGE) * trade_value
    sebi_charge = SEBI_CHARGE * trade_value
    stt_charge = STT_CHARGE * trade_value if not is_buy else 0
    stamp_duty = STAMP_DUTY * trade_value if is_buy else 0
    gst_base = brokerage + exchange_charge
    gst_charge = GST_RATE * gst_base
    
    if is_buy:
        total_charges = brokerage + exchange_charge + sebi_charge + stamp_duty + gst_charge
    else:
        total_charges = brokerage + exchange_charge + sebi_charge + stt_charge + gst_charge
    
    return {
        'brokerage': brokerage,
        'exchange_charge': exchange_charge,
        'sebi_charge': sebi_charge,
        'stt_charge': stt_charge,
        'stamp_duty': stamp_duty,
        'gst_charge': gst_charge,
        'total_charges': total_charges,
        'trade_value': trade_value
    }


def calculate_position_pnl(position_df, symbol):
    """Calculate P&L for a specific position."""
    symbol_data = position_df[position_df['trading_symbol'] == symbol].copy()
    exchange = "NSE"
    if 'exchange' in symbol_data.columns:
        exchange = symbol_data['exchange'].iloc[0] if not symbol_data.empty else "NSE"
    
    total_buy_qty = symbol_data['credit_quantity'].fillna(0).sum()
    total_buy_value = (symbol_data['credit_price'].fillna(0) * symbol_data['credit_quantity'].fillna(0)).sum()
    total_sell_qty = symbol_data['debit_quantity'].fillna(0).sum()
    total_sell_value = (symbol_data['debit_price'].fillna(0) * symbol_data['debit_quantity'].fillna(0)).sum()
    
    net_qty = int(total_buy_qty - total_sell_qty)
    avg_buy_price = float(total_buy_value / total_buy_qty if total_buy_qty > 0 else 0)
    cost_price = avg_buy_price if net_qty > 0 else 0
    
    return {
        'symbol': symbol,
        'net_qty': net_qty,
        'avg_buy_price': avg_buy_price,
        'cost_price': cost_price,
        'total_cost': float(cost_price * abs(net_qty)),
        'exchange': exchange
    }


def get_exchange_from_position(position_df, symbol):
    """Determine the exchange for a symbol."""
    try:
        symbol_data = position_df[position_df['trading_symbol'] == symbol]
        if not symbol_data.empty:
            ts = symbol_data['trading_symbol'].iloc[0]
            if 'BSE_' in ts:
                return "BSE"
            return "NSE"
    except:
        pass
    return "NSE"


def close_position(symbol, quantity, exchange="NSE"):
    """Close a position by selling the stock."""
    try:
        # Check if symbol already has exchange prefix
        if 'NSE_' in symbol or 'BSE_' in symbol:
            trading_symbol = symbol
            # Extract clean symbol if prefix exists
            if 'NSE_' in symbol:
                symbol = symbol.replace('NSE_', '')
                exchange = 'NSE'
            elif 'BSE_' in symbol:
                symbol = symbol.replace('BSE_', '')
                exchange = 'BSE'
        else:
            trading_symbol = f"{exchange}_{symbol}"
        
        quantity = int(float(quantity))
        
        current_price = get_current_price(symbol, exchange)
        
        if current_price is None:
            print(f"  [ERROR] Could not get current price for {symbol}")
            return False
        
        order_response = groww.place_order(
            segment=groww.SEGMENT_CASH,
            trading_symbol=trading_symbol,
            exchange=groww.EXCHANGE_NSE if exchange == "NSE" else groww.EXCHANGE_BSE,
            transaction_type=groww.TRANSACTION_TYPE_SELL,
            quantity=quantity,
            product=groww.PRODUCT_MIS,
            order_type=groww.ORDER_TYPE_MARKET,
            validity=groww.VALIDITY_DAY
        )
        
        print(f"  [SUCCESS] Position closed for {symbol}: Sold {quantity} shares at ~Rs.{current_price}")
        time.sleep(0.5)  # Reduced delay
        return True
        
    except Exception as e:
        print(f"  [ERROR] Failed to close position for {symbol}: {e}")
        return False


class PositionGUI:
    """Main GUI class for Position P&L Monitor"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Groww Position P&L Monitor")
        self.root.geometry("1300x600")
        self.root.configure(bg=GUIColors.BG_COLOR)
        
        self.positions_data = []
        self.refresh_interval = 5000  # 5 seconds refresh
        self.is_running = True
        self.is_refreshing = False  # Flag to prevent concurrent refreshes
        
        # Create GUI components
        self.create_header()
        self.create_control_panel()
        self.create_table()
        self.create_status_bar()
        
        # Start auto-refresh in a separate thread
        self.refresh_thread = threading.Thread(target=self.refresh_positions_thread, daemon=True)
        self.refresh_thread.start()
    
    def create_header(self):
        """Create the header section"""
        header_frame = tk.Frame(self.root, bg=GUIColors.HEADER_BG, height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="GROWW POSITION P&L MONITOR",
            font=('Consolas', 16, 'bold'),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.HEADER_FG
        )
        title_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.time_label = tk.Label(
            header_frame,
            text="",
            font=('Consolas', 11),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.YELLOW
        )
        self.time_label.pack(side=tk.RIGHT, padx=20, pady=10)
        
        self.update_time()
    
    def update_time(self):
        """Update the time display"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=f"Time: {current_time}")
        if self.is_running:
            self.root.after(1000, self.update_time)
    
    def create_control_panel(self):
        """Create the control panel with buttons"""
        control_frame = tk.Frame(self.root, bg=GUIColors.BG_COLOR)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.refresh_btn = tk.Button(
            control_frame,
            text="Refresh",
            font=('Consolas', 10),
            bg=GUIColors.BUTTON_BG,
            fg=GUIColors.HEADER_FG,
            command=self.trigger_refresh,
            padx=15,
            pady=5
        )
        self.refresh_btn.pack(side=tk.LEFT, padx=5)
        
        self.exit_btn = tk.Button(
            control_frame,
            text="EXIT SELECTED POSITIONS",
            font=('Consolas', 11, 'bold'),
            bg=GUIColors.RED,
            fg=GUIColors.HEADER_FG,
            command=self.exit_selected_positions,
            padx=20,
            pady=5
        )
        self.exit_btn.pack(side=tk.RIGHT, padx=5)
        
        self.summary_label = tk.Label(
            control_frame,
            text="Select positions to exit",
            font=('Consolas', 10),
            bg=GUIColors.BG_COLOR,
            fg=GUIColors.PURPLE
        )
        self.summary_label.pack(side=tk.RIGHT, padx=20)
    
    def create_table(self):
        """Create the positions table using Treeview"""
        table_frame = tk.Frame(self.root, bg=GUIColors.BG_COLOR)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        y_scroll = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ('symbol', 'qty', 'avg_price', 'current_price', 
                   'invested', 'current_value', 'gross_pnl', 'charges', 
                   'net_pnl', 'net_pnl_pct')
        
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
        self.tree.column('symbol', width=100, anchor='center')
        
        self.tree.heading('qty', text='Qty')
        self.tree.column('qty', width=60, anchor='center')
        
        self.tree.heading('avg_price', text='Avg Price')
        self.tree.column('avg_price', width=90, anchor='e')
        
        self.tree.heading('current_price', text='Current')
        self.tree.column('current_price', width=90, anchor='e')
        
        self.tree.heading('invested', text='Invested')
        self.tree.column('invested', width=100, anchor='e')
        
        self.tree.heading('current_value', text='Curr Value')
        self.tree.column('current_value', width=100, anchor='e')
        
        self.tree.heading('gross_pnl', text='Gross P&L')
        self.tree.column('gross_pnl', width=90, anchor='e')
        
        self.tree.heading('charges', text='Charges')
        self.tree.column('charges', width=80, anchor='e')
        
        self.tree.heading('net_pnl', text='Net P&L')
        self.tree.column('net_pnl', width=90, anchor='e')
        
        self.tree.heading('net_pnl_pct', text='%')
        self.tree.column('net_pnl_pct', width=70, anchor='e')
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Configure color tags
        self.tree.tag_configure('profit', foreground=GUIColors.GREEN)
        self.tree.tag_configure('loss', foreground=GUIColors.RED)
        
        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)
    
    def on_tree_select(self, event):
        """Handle treeview selection"""
        self.update_summary()
    
    def create_status_bar(self):
        """Create the status bar at the bottom"""
        status_frame = tk.Frame(self.root, bg=GUIColors.HEADER_BG, height=35)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.total_pnl_label = tk.Label(
            status_frame,
            text="Total Net P&L: Rs.0.00 (0.00%)",
            font=('Consolas', 11, 'bold'),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.YELLOW
        )
        self.total_pnl_label.pack(side=tk.LEFT, padx=20)
        
        self.portfolio_label = tk.Label(
            status_frame,
            text="Portfolio: Rs.0.00",
            font=('Consolas', 10),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.PURPLE
        )
        self.portfolio_label.pack(side=tk.LEFT, padx=20)
        
        self.count_label = tk.Label(
            status_frame,
            text="Positions: 0",
            font=('Consolas', 10),
            bg=GUIColors.HEADER_BG,
            fg=GUIColors.FG_COLOR
        )
        self.count_label.pack(side=tk.RIGHT, padx=20)
    
    def trigger_refresh(self):
        """Trigger a manual refresh if not already refreshing"""
        if not self.is_refreshing:
            threading.Thread(target=self.refresh_positions_thread, daemon=True).start()
    
    def refresh_positions_thread(self):
        """Fetch positions in a separate thread using parallel LTP fetching"""
        self.is_refreshing = True
        try:
            self.root.after(0, self.clear_table)
            
            position_response = groww.get_positions_for_user()
            position_df = pd.DataFrame(position_response['positions'])
            
            if position_df.empty:
                self.root.after(0, self.update_empty_state)
                return
            
            unique_symbols = position_df['trading_symbol'].unique().tolist()
            results = []
            
            # First pass: collect all symbols and their exchanges
            symbols_exchanges_list = []
            positions_with_info = []
            
            for symbol in unique_symbols:
                try:
                    pnl_data = calculate_position_pnl(position_df, symbol)
                    
                    if pnl_data['net_qty'] == 0:
                        continue
                    
                    exchange = pnl_data.get('exchange', get_exchange_from_position(position_df, symbol))
                    
                    # Collect symbol and exchange for parallel LTP fetch
                    symbols_exchanges_list.append((symbol, exchange))
                    
                    # Store other info for later use
                    positions_with_info.append({
                        'symbol': symbol,
                        'exchange': exchange,
                        'net_qty': pnl_data['net_qty'],
                        'cost_price': pnl_data['cost_price'],
                        'total_cost': pnl_data['total_cost']
                    })
                    
                except Exception as e:
                    print(f"Error processing {symbol}: {e}")
                    continue
            
            # Fetch all LTPs in parallel
            print(f"Fetching LTP for {len(symbols_exchanges_list)} symbols in parallel...")
            ltp_prices = get_current_prices_parallel(symbols_exchanges_list)
            
            # Second pass: calculate P&L using fetched prices
            for pos_info in positions_with_info:
                try:
                    symbol = pos_info['symbol']
                    exchange = pos_info['exchange']
                    net_qty = pos_info['net_qty']
                    cost_price = pos_info['cost_price']
                    total_cost = pos_info['total_cost']
                    
                    current_price = ltp_prices.get(symbol)
                    if current_price is None:
                        current_price = cost_price
                    
                    current_value = current_price * abs(net_qty)
                    invested_value = cost_price * abs(net_qty)
                    
                    buy_charges = calculate_charges(abs(net_qty), cost_price, True, exchange)
                    sell_charges = calculate_charges(abs(net_qty), current_price, False, exchange)
                    total_charges = buy_charges['total_charges'] + sell_charges['total_charges']
                    
                    if net_qty > 0:
                        gross_pnl = (current_price - cost_price) * net_qty
                        pnl = gross_pnl - total_charges
                        pnl_percent = ((current_price / cost_price) - 1) * 100 if cost_price > 0 else 0
                    else:
                        gross_pnl = 0
                        pnl = 0
                        pnl_percent = 0
                    
                    position_info = {
                        'symbol': symbol,
                        'qty': net_qty,
                        'avg_price': round(cost_price, 2),
                        'current_price': round(current_price, 2),
                        'invested': round(invested_value, 2),
                        'current_value': round(current_value, 2),
                        'gross_pnl': round(gross_pnl, 2),
                        'charges': round(total_charges, 2),
                        'net_pnl': round(pnl, 2),
                        'net_pnl_pct': round(pnl_percent, 2),
                        'exchange': exchange
                    }
                    
                    results.append(position_info)
                    
                except Exception as e:
                    print(f"Error calculating P&L for {symbol}: {e}")
                    continue
            
            self.positions_data = results
            self.root.after(0, lambda: self.update_table(results))
            
        except Exception as e:
            print(f"Error fetching positions: {e}")
            self.root.after(0, self.show_error)
        finally:
            self.is_refreshing = False
    
    def clear_table(self):
        """Clear the table"""
        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def update_empty_state(self):
        """Update display when no positions"""
        self.count_label.config(text="Positions: 0")
        self.total_pnl_label.config(text="Total Net P&L: Rs.0.00 (0.00%)", fg=GUIColors.YELLOW)
        self.portfolio_label.config(text="Portfolio: Rs.0.00")
        self.summary_label.config(text="No positions found")
    
    def show_error(self):
        """Show error state"""
        self.summary_label.config(text="Error fetching positions")
    
    def update_table(self, results):
        """Update the table with position data"""
        self.clear_table()
        
        for pos in results:
            tag = 'profit' if pos['net_pnl'] >= 0 else 'loss'
            
            self.tree.insert('', 'end', values=(
                pos['symbol'],
                pos['qty'],
                f"{pos['avg_price']:.2f}",
                f"{pos['current_price']:.2f}",
                f"{pos['invested']:.2f}",
                f"{pos['current_value']:.2f}",
                f"{pos['gross_pnl']:.2f}",
                f"{pos['charges']:.2f}",
                f"{pos['net_pnl']:.2f}",
                f"{pos['net_pnl_pct']:.2f}%"
            ), tags=(tag,))
        
        self.update_totals()
        self.update_summary()
    
    def update_totals(self):
        """Update totals in status bar"""
        total_invested = sum(p['invested'] for p in self.positions_data)
        total_current = sum(p['current_value'] for p in self.positions_data)
        total_net_pnl = sum(p['net_pnl'] for p in self.positions_data)
        
        pnl_percent = ((total_current / total_invested) - 1) * 100 if total_invested > 0 else 0
        
        self.count_label.config(text=f"Positions: {len(self.positions_data)}")
        self.portfolio_label.config(text=f"Portfolio: Rs.{total_current:,.2f}")
        
        if total_net_pnl >= 0:
            self.total_pnl_label.config(
                text=f"Total Net P&L: Rs.{total_net_pnl:,.2f} ({pnl_percent:.2f}%)",
                fg=GUIColors.GREEN
            )
        else:
            self.total_pnl_label.config(
                text=f"Total Net P&L: -Rs.{abs(total_net_pnl):,.2f} ({pnl_percent:.2f}%)",
                fg=GUIColors.RED
            )
    
    def update_summary(self):
        """Update summary based on selection"""
        selected = self.get_selected_positions()
        count = len(selected)
        self.summary_label.config(text=f"Selected: {count} position(s)")
    
    def get_selected_positions(self):
        """Get list of selected positions"""
        selected = []
        for item in self.tree.selection():
            values = self.tree.item(item)['values']
            if values:
                symbol = values[0]
                for pos in self.positions_data:
                    if pos['symbol'] == symbol:
                        selected.append(pos)
                        break
        return selected
    
    def exit_selected_positions(self):
        """Exit selected positions"""
        selected = self.get_selected_positions()
        
        if not selected:
            messagebox.showwarning("No Selection", "Please select position(s) to exit.\n\nClick on a row to select it.\nHold Ctrl+Click to select multiple.")
            return
        
        total_pnl = sum(p['net_pnl'] for p in selected)
        
        confirm_msg = f"Are you sure you want to exit {len(selected)} position(s)?\n\n"
        if total_pnl >= 0:
            confirm_msg += f"Expected profit: Rs.{total_pnl:,.2f}"
        else:
            confirm_msg += f"Expected loss: Rs.{abs(total_pnl):,.2f}"
        
        response = messagebox.askyesno("Confirm Exit", confirm_msg)
        
        if not response:
            return
        
        self.exit_btn.config(state='disabled', text="Closing...")
        
        def exit_thread():
            closed = []
            failed = []
            
            for pos in selected:
                try:
                    success = close_position(pos['symbol'], pos['qty'], pos['exchange'])
                    
                    if success:
                        closed.append(pos['symbol'])
                    else:
                        failed.append(pos['symbol'])
                    
                    time.sleep(0.5)  # Reduced delay for closing positions
                    
                except Exception as e:
                    print(f"Error closing {pos['symbol']}: {e}")
                    failed.append(pos['symbol'])
            
            self.root.after(0, lambda: self.on_exit_complete(closed, failed))
        
        threading.Thread(target=exit_thread, daemon=True).start()
    
    def on_exit_complete(self, closed, failed):
        """Handle exit completion"""
        self.exit_btn.config(state='normal', text="EXIT SELECTED POSITIONS")
        
        if closed:
            msg = f"Successfully closed {len(closed)} position(s):\n" + "\n".join(f"  - {s}" for s in closed)
            if failed:
                msg += f"\n\nFailed to close {len(failed)} position(s):\n" + "\n".join(f"  - {s}" for s in failed)
            messagebox.showinfo("Exit Complete", msg)
        else:
            messagebox.showerror("Exit Failed", f"Failed to close positions:\n" + "\n".join(f"  - {s}" for s in failed))
        
        self.trigger_refresh()
    
    def on_closing(self):
        """Handle window closing"""
        self.is_running = False
        self.root.destroy()


def main():
    """Main function to run the GUI"""
    root = tk.Tk()
    app = PositionGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
