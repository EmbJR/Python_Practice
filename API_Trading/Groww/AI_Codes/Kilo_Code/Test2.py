"""
Groww API - Position List with P&L and Trending Amounts
========================================================
This script fetches all open positions from Groww API and displays:
- Current positions with quantity
- Average buy/sell prices
- Current market price (LTP)
- P&L (Profit and Loss)
- Trending amounts (current value vs cost)

Author: Kilo Code
Platform: Groww
"""

# Import required libraries
from growwapi import GrowwAPI
import pandas as pd
import time
import os
import sys
from datetime import datetime

# ANSI Color Codes for visual appeal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    BG_BLACK = '\033[40m'
    BG_GREEN = '\033[42m'
    BG_RED = '\033[41m'
    BG_YELLOW = '\033[43m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

# =============================================================================
# CONFIGURATION - Replace with your API Token
# =============================================================================
# Note: Token can be generated from Groww Dashboard
# Tokens expire frequently - regenerate if API calls fail

API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3NzEyODgyMDAsImlhdCI6MTc3MTIxNzM5OSwibmJmIjoxNzcxMjE3Mzk5LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCI0YTUzNDhkZi1lZTc1LTQ2NmUtODQxOC1jZjIwYzdiMjc5NjlcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjU2N2QzMjhhLWFmZDAtNDFkZC04OGUyLWFiMDdkNjYzNGFhOFwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOmVjMDQ6NDFmOjhkMDg6N2Q5MSwxNzIuNzAuMjE5Ljg3LDM1LjI0MS4yMy4xMjNcIixcInR3b0ZhRXhwaXJ5VHNcIjoxNzcxMjg4MjAwMDAwfSIsImlzcyI6ImFwZXgtYXV0aC1wcm9kLWFwcCJ9.pCSSsYEcqVthtllSnZM8bRIwdErBUdm9aiDt7BBGenwWNheh93tjSHGB7C6wPTksITkTiYrc054Emhqln_6DJQ"

# Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)


def get_current_price(symbol, exchange="NSE"):
    """
    Get the Last Traded Price (LTP) for a given symbol.
    
    Parameters:
        symbol: Trading symbol (e.g., 'RELIANCE')
        exchange: Exchange prefix ('NSE' or 'BSE')
    
    Returns:
        Current LTP price
    """
    try:
        # Format: NSE_RELIANCE or BSE_RELIANCE
        ltp_symbol = f"{exchange}_{symbol}"
        
        # Get LTP from Groww API
        ltp_response = groww.get_ltp(
            exchange_trading_symbols=ltp_symbol,
            segment=groww.SEGMENT_CASH
        )
        
        # Extract price from response
        current_price = float(ltp_response[ltp_symbol])
        
        # Rate limiting - wait 1 second between API calls
        time.sleep(1)
        
        return current_price
    
    except Exception as e:
        print(f"Error getting LTP for {symbol}: {e}")
        return None


def calculate_position_pnl(position_df, symbol):
    """
    Calculate P&L for a specific position.
    
    Parameters:
        position_df: DataFrame containing position data
        symbol: Trading symbol
    
    Returns:
        Dictionary with P&L details
    """
    # Filter data for this symbol
    symbol_data = position_df[position_df['trading_symbol'] == symbol].copy()
    
    # Calculate total buy (credit) quantity and value
    total_buy_qty = symbol_data['credit_quantity'].fillna(0).sum()
    total_buy_value = (symbol_data['credit_price'].fillna(0) * 
                       symbol_data['credit_quantity'].fillna(0)).sum()
    
    # Calculate total sell (debit) quantity and value
    total_sell_qty = symbol_data['debit_quantity'].fillna(0).sum()
    total_sell_value = (symbol_data['debit_price'].fillna(0) * 
                        symbol_data['debit_quantity'].fillna(0)).sum()
    
    # Net position
    net_qty = total_buy_qty - total_sell_qty
    
    # Average prices
    avg_buy_price = total_buy_value / total_buy_qty if total_buy_qty > 0 else 0
    avg_sell_price = total_sell_value / total_sell_qty if total_sell_qty > 0 else 0
    
    # Cost and current value
    cost_price = avg_buy_price if net_qty > 0 else avg_sell_price
    
    return {
        'symbol': symbol,
        'net_qty': net_qty,
        'avg_buy_price': avg_buy_price,
        'avg_sell_price': avg_sell_price,
        'cost_price': cost_price,
        'total_cost': cost_price * abs(net_qty)
    }


def get_exchange_from_position(position_df, symbol):
    """
    Determine the exchange for a symbol from position data.
    """
    try:
        # Try to get exchange from position data
        symbol_data = position_df[position_df['trading_symbol'] == symbol]
        if not symbol_data.empty:
            return "NSE"  # Default to NSE for positions
    except:
        pass
    return "NSE"


def main():
    """
    Main function to list all positions with P&L and trending amounts.
    Runs in an infinite loop with 2-second refresh.
    """
    iteration = 0
    
    while True:
        iteration += 1
        
        # Clear screen for clean display
        clear_screen()
        
        # Print header with timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(Colors.BG_BLACK + Colors.BOLD + Colors.HEADER + "=" * 80 + Colors.ENDC)
        print(Colors.BG_BLACK + Colors.BOLD + Colors.HEADER + "  GROWW API - REAL-TIME POSITION MONITOR" + Colors.ENDC)
        print(Colors.BG_BLACK + Colors.BOLD + Colors.HEADER + "=" * 80 + Colors.ENDC)
        print(Colors.YELLOW + f"  Last Update: {current_time} | Iteration: {iteration}" + Colors.ENDC)
        print()
        
        # Step 1: Get all positions from Groww
        try:
            position_response = groww.get_positions_for_user()
            position_df = pd.DataFrame(position_response['positions'])
        except Exception as e:
            print(Colors.RED + f"Error fetching positions: {e}" + Colors.ENDC)
            print(Colors.YELLOW + "Retrying in 2 seconds..." + Colors.ENDC)
            time.sleep(2)
            continue
        
        if position_df.empty:
            print(Colors.YELLOW + "No positions found!" + Colors.ENDC)
            time.sleep(2)
            continue
        
        # Get unique trading symbols
        unique_symbols = position_df['trading_symbol'].unique().tolist()
        
        # Step 2: Create a list to store results
        results = []
        
        # Step 3: Process each symbol
        for symbol in unique_symbols:
            try:
                # Calculate position details
                pnl_data = calculate_position_pnl(position_df, symbol)
                
                # Skip if no net position
                if pnl_data['net_qty'] == 0:
                    continue
                
                # Get current price (LTP)
                exchange = get_exchange_from_position(position_df, symbol)
                current_price = get_current_price(symbol, exchange)
                
                if current_price is None:
                    current_price = pnl_data['cost_price']
                
                # Calculate P&L and trending amounts
                current_value = current_price * abs(pnl_data['net_qty'])
                invested_value = pnl_data['cost_price'] * abs(pnl_data['net_qty'])
                
                # P&L calculation
                if pnl_data['net_qty'] > 0:  # Long position
                    pnl = (current_price - pnl_data['cost_price']) * pnl_data['net_qty']
                    pnl_percent = ((current_price / pnl_data['cost_price']) - 1) * 100 if pnl_data['cost_price'] > 0 else 0
                else:  # Short position
                    pnl = (pnl_data['cost_price'] - current_price) * abs(pnl_data['net_qty'])
                    pnl_percent = ((pnl_data['cost_price'] / current_price) - 1) * 100 if current_price > 0 else 0
                
                # Trending amount
                trending = current_value - invested_value
                trending_percent = ((current_value / invested_value) - 1) * 100 if invested_value > 0 else 0
                
                # Store result
                results.append({
                    'Symbol': symbol,
                    'Qty': pnl_data['net_qty'],
                    'Avg Buy Price': round(pnl_data['cost_price'], 2),
                    'Current Price': round(current_price, 2),
                    'Invested Value': round(invested_value, 2),
                    'Current Value': round(current_value, 2),
                    'P&L': round(pnl, 2),
                    'P&L %': round(pnl_percent, 2),
                    'Trending': round(trending, 2),
                    'Trending %': round(trending_percent, 2)
                })
                
            except Exception as e:
                print(Colors.RED + f"Error processing {symbol}: {e}" + Colors.ENDC)
                continue
        
        # Step 4: Display results in a table
        print(Colors.BLUE + "-" * 80 + Colors.ENDC)
        print(Colors.BOLD + Colors.GREEN + "  POSITION SUMMARY" + Colors.ENDC)
        print(Colors.BLUE + "-" * 80 + Colors.ENDC)
        
        if results:
            # Create DataFrame from results
            results_df = pd.DataFrame(results)
            
            # Sort by P&L (descending)
            results_df = results_df.sort_values('P&L', ascending=False)
            
            # Display settings
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.float_format', '{:.2f}'.format)
            
            # Print header row
            print()
            print(Colors.BOLD + f"{'Symbol':<12} {'Qty':>6} {'Avg Price':>12} {'Current':>12} "
                  f"{'Inv Value':>12} {'Curr Value':>12} {'P&L':>12} {'%':>8}" + Colors.ENDC)
            print(Colors.BLUE + "-" * 100 + Colors.ENDC)
            
            # Print each row with color coding
            for _, row in results_df.iterrows():
                pnl_color = Colors.GREEN if row['P&L'] >= 0 else Colors.RED
                pnl_str = f"{pnl_color}{row['P&L']:>12.2f}{Colors.ENDC}"
                pnl_pct_str = f"{pnl_color}{row['P&L %']:>7.2f}%{Colors.ENDC}"
                
                print(f"{Colors.BOLD}{row['Symbol']:<12}{Colors.ENDC} "
                      f"{row['Qty']:>6} "
                      f"{row['Avg Buy Price']:>12.2f} "
                      f"{Colors.BOLD}{row['Current Price']:>12.2f}{Colors.ENDC} "
                      f"{row['Invested Value']:>12.2f} "
                      f"{row['Current Value']:>12.2f} "
                      f"{pnl_str} {pnl_pct_str}")
            
            print(Colors.BLUE + "-" * 100 + Colors.ENDC)
            
            # Calculate totals
            total_invested = results_df['Invested Value'].sum()
            total_current = results_df['Current Value'].sum()
            total_pnl = results_df['P&L'].sum()
            total_trending = results_df['Trending'].sum()
            total_pnl_percent = ((total_current / total_invested) - 1) * 100 if total_invested > 0 else 0
            
            # Color total P&L
            total_pnl_color = Colors.GREEN if total_pnl >= 0 else Colors.RED
            
            print(Colors.BOLD)
            print(f"{'TOTAL':<12} {'':<6} {'':<12} {'':<12} "
                  f"{total_invested:>12.2f} {total_current:>12.2f} "
                  f"{total_pnl_color}{total_pnl:>12.2f}{Colors.ENDC} "
                  f"{total_pnl_color}{total_pnl_percent:>7.2f}%{Colors.ENDC}")
            print(Colors.BLUE + "-" * 100 + Colors.ENDC)
            
            # Summary indicators
            print()
            if total_pnl >= 0:
                print(Colors.GREEN + f"  Total Profit: Rs.{total_pnl:,.2f} ({total_pnl_percent:.2f}%)" + Colors.ENDC)
            else:
                print(Colors.RED + f"  Total Loss: Rs.{abs(total_pnl):,.2f} ({total_pnl_percent:.2f}%)" + Colors.ENDC)
            
            print(Colors.YELLOW + f"  Portfolio Value: Rs.{total_current:,.2f} | Trending: Rs.{total_trending:,.2f}" + Colors.ENDC)
            
        else:
            print(Colors.YELLOW + "  No open positions to display." + Colors.ENDC)
        
        print()
        print(Colors.BLUE + "=" * 80 + Colors.ENDC)
        print(Colors.YELLOW + "  Next update in 2 seconds... (Press Ctrl+C to stop)" + Colors.ENDC)
        print(Colors.BLUE + "=" * 80 + Colors.ENDC)
        
        # Wait 2 seconds before next update
        time.sleep(2)


# Run the main function
if __name__ == "__main__":
    main()
