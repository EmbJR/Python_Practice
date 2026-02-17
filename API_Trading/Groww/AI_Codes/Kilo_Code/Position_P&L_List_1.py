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

# India Brokergae Charges (Groww - Zero Brokerage for Intraday)
# Source: Standard Groww charges
# - Brokerage: ₹0 (Zero brokerage for equity intraday)
# - STT (Securities Transaction Tax): 0.025% on sell side
# - GST: 18% on (brokerage + exchange fees)
# - SEBI Charges: 0.0001% (₹10 per crore)
# - Stamp Duty: 0.01% on buy side (varies by state, using 0.01% as standard)
# - Exchange Transaction Charges: 0.00135% for NSE

BROKERAGE_CHARGE = 0  # ₹0 for intraday
STT_CHARGE = 0.00025  # 0.025% on sell side
GST_RATE = 0.18  # 18% GST
SEBI_CHARGE = 0.000001  # 0.0001% (₹10 per crore)
STAMP_DUTY = 0.0001  # 0.01% on buy side
NSE_EXCHANGE_CHARGE = 0.0000135  # 0.00135% for NSE
BSE_EXCHANGE_CHARGE = 0.0000135  # 0.00135% for BSE

API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3NzEzNzQ2MDAsImlhdCI6MTc3MTMwOTk5MiwibmJmIjoxNzcxMzA5OTkyLCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCJlZjRlMjUzNS0zOWJiLTQzOGItYjE1MC0wMDEzN2RiNGU2ODhcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjlmODlmZTJkLTRhZGYtNGU3Zi1hOGY5LTM1MjUzZTEyN2E5NVwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOmZkZGY6MWNmMDo5ZDg3OjQ2NDksMTYyLjE1OC4xOTEuMjE0LDM1LjI0MS4yMy4xMjNcIixcInR3b0ZhRXhwaXJ5VHNcIjoxNzcxMzc0NjAwMDAwfSIsImlzcyI6ImFwZXgtYXV0aC1wcm9kLWFwcCJ9.gZu9npYxGj7vs9Eb2T5afJurVH75y1fq6vuB6NAyK1eB5Xo7zLIZnGGmLQTTNz7_GAamdLLTNAODSchg5PKJWg"

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


def calculate_charges(quantity, price, is_buy, exchange="NSE"):
    """
    Calculate all applicable charges for a trade.
    
    Parameters:
        quantity: Number of shares
        price: Price per share
        is_buy: True for buy, False for sell
        exchange: Exchange prefix ('NSE' or 'BSE')
    
    Returns:
        Dictionary with breakdown of all charges
    """
    trade_value = quantity * price
    
    # Brokerage (Zero for Groww intraday)
    brokerage = BROKERAGE_CHARGE * trade_value
    
    # Exchange Transaction Charges
    exchange_charge = (NSE_EXCHANGE_CHARGE if exchange == "NSE" else BSE_EXCHANGE_CHARGE) * trade_value
    
    # SEBI Charges (both buy and sell)
    sebi_charge = SEBI_CHARGE * trade_value
    
    # STT (only on sell side)
    stt_charge = STT_CHARGE * trade_value if not is_buy else 0
    
    # Stamp Duty (only on buy side)
    stamp_duty = STAMP_DUTY * trade_value if is_buy else 0
    
    # GST on (brokerage + exchange charges)
    gst_base = brokerage + exchange_charge
    gst_charge = GST_RATE * gst_base
    
    # Total charges
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
    """
    Calculate P&L for a specific position including all charges.
    
    Parameters:
        position_df: DataFrame containing position data
        symbol: Trading symbol
    
    Returns:
        Dictionary with P&L details including charges
    """
    # Filter data for this symbol
    symbol_data = position_df[position_df['trading_symbol'] == symbol].copy()
    
    # Get exchange from position data
    exchange = "NSE"
    if 'exchange' in symbol_data.columns:
        exchange = symbol_data['exchange'].iloc[0] if not symbol_data.empty else "NSE"
    
    # Calculate total buy (credit) quantity and value
    total_buy_qty = symbol_data['credit_quantity'].fillna(0).sum()
    total_buy_value = (symbol_data['credit_price'].fillna(0) * 
                       symbol_data['credit_quantity'].fillna(0)).sum()
    
    # Calculate total sell (debit) quantity and value
    total_sell_qty = symbol_data['debit_quantity'].fillna(0).sum()
    total_sell_value = (symbol_data['debit_price'].fillna(0) * 
                        symbol_data['debit_quantity'].fillna(0)).sum()
    
    # Calculate buy charges
    buy_charges = calculate_charges(total_buy_qty, total_buy_value / total_buy_qty if total_buy_qty > 0 else 0, True, exchange)
    
    # Calculate sell charges
    sell_charges = calculate_charges(total_sell_qty, total_sell_value / total_sell_qty if total_sell_qty > 0 else 0, False, exchange)
    
    # Net position
    net_qty = total_buy_qty - total_sell_qty
    
    # Average prices
    avg_buy_price = total_buy_value / total_buy_qty if total_buy_qty > 0 else 0
    avg_sell_price = total_sell_value / total_sell_qty if total_sell_qty > 0 else 0
    
    # Cost and current value
    cost_price = avg_buy_price if net_qty > 0 else avg_sell_price
    
    # Total charges incurred
    total_buy_charges = total_buy_qty * calculate_charges(1, avg_buy_price, True, exchange)['total_charges'] if total_buy_qty > 0 else 0
    total_sell_charges = total_sell_qty * calculate_charges(1, avg_sell_price, False, exchange)['total_charges'] if total_sell_qty > 0 else 0
    
    return {
        'symbol': symbol,
        'net_qty': net_qty,
        'avg_buy_price': avg_buy_price,
        'avg_sell_price': avg_sell_price,
        'cost_price': cost_price,
        'total_cost': cost_price * abs(net_qty),
        'exchange': exchange,
        'total_buy_charges': total_buy_charges,
        'total_sell_charges': total_sell_charges
    }


# Constants for trading logic
STOP_LOSS_PERCENT = -0.5  # -0.5% stop loss
TRAILING_STOP_LOSS_PERCENT = -0.5  # Trailing stop loss percentage

# Dictionary to store the trailing stop-loss for each symbol
# This ensures the trailing stop-loss is always incremental (never goes below the previous value)
trailing_stop_loss_dict = {}

# Dictionary to track if trailing stop-loss is "active" for a symbol
# Once active, the -0.5% stop-loss is ignored for that symbol
trailing_sl_active_dict = {}

def close_position(symbol, quantity, exchange="NSE"):
    """
    Close a position by selling the stock.
    
    Parameters:
        symbol: Trading symbol (e.g., 'RELIANCE')
        quantity: Number of shares to sell
        exchange: Exchange prefix ('NSE' or 'BSE')
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Format: NSE_RELIANCE or BSE_RELIANCE
        trading_symbol = f"{exchange}_{symbol}"
        
        # Get current price for order
        current_price = get_current_price(symbol, exchange)
        
        if current_price is None:
            print(Colors.RED + f"  [ERROR] Could not get current price for {symbol}, cannot close position" + Colors.ENDC)
            return False
        
        # Place sell order (MIS for intraday)
        order_response = groww.place_order(
            trading_symbol=trading_symbol,
            exchange=groww.EXCHANGE_NSE if exchange == "NSE" else groww.EXCHANGE_BSE,
            transaction_type=groww.TRANSACTION_TYPE_SELL,
            quantity=quantity,
            product=groww.PRODUCT_MIS,
            order_type=groww.ORDER_TYPE_MARKET,
            validity=groww.VALIDITY_DAY
        )
        
        print(Colors.GREEN + f"  [SUCCESS] Position closed for {symbol}: Sold {quantity} shares at ~Rs.{current_price}" + Colors.ENDC)
        time.sleep(1)  # Rate limiting
        return True
        
    except Exception as e:
        print(Colors.RED + f"  [ERROR] Failed to close position for {symbol}: {e}" + Colors.ENDC)
        return False


def check_and_execute_trading_logic(pnl_data, current_price, symbol, exchange):
    """
    Check P&L conditions and execute trading logic.
    
    Logic:
    1. If trailing stop-loss is NOT active and P&L < -0.5%, close the position immediately
    2. If trailing stop-loss is active, ignore the -0.5% stop-loss (only use trailing SL)
    3. If P&L increases (price goes up), update trailing stop-loss
       - Only update if final P&L at trailing SL price would be positive
       - Trailing stop-loss is always incremental (never goes below previous value)
       - Close position when price drops below trailing stop-loss
    
    Parameters:
        pnl_data: Dictionary with position P&L details
        current_price: Current market price
        symbol: Trading symbol
        exchange: Exchange prefix
    
    Returns:
        True if position was closed, False otherwise
    """
    try:
        if pnl_data['net_qty'] <= 0:
            # Clear trailing stop-loss if position no longer exists
            if symbol in trailing_stop_loss_dict:
                del trailing_stop_loss_dict[symbol]
            if symbol in trailing_sl_active_dict:
                del trailing_sl_active_dict[symbol]
            return False
        
        avg_buy_price = pnl_data['cost_price']
        net_qty = pnl_data['net_qty']
        
        # Calculate current P&L percentage
        pnl_percent = ((current_price / avg_buy_price) - 1) * 100 if avg_buy_price > 0 else 0
        
        print(Colors.BLUE + f"\n  [CHECK] {symbol}: Current Price: Rs.{current_price:.2f}, Avg Buy: Rs.{avg_buy_price:.2f}, P&L: {pnl_percent:.2f}%" + Colors.ENDC)
        
        # Calculate stop-loss prices
        initial_stop_loss = avg_buy_price * (1 + STOP_LOSS_PERCENT / 100)
        
        # Check if trailing stop-loss is already active for this symbol
        is_trailing_sl_active = trailing_sl_active_dict.get(symbol, False)
        
        print(Colors.BLUE + f"  [CHECK] {symbol}: Initial SL: Rs.{initial_stop_loss:.2f}, Trailing SL Active: {is_trailing_sl_active}" + Colors.ENDC)
        
        # Feature 3: If trailing stop-loss is already active, ignore -0.5% stop-loss
        # Only check trailing stop-loss
        if is_trailing_sl_active:
            # Get current stored trailing stop-loss
            current_stored_sl = trailing_stop_loss_dict.get(symbol)
            
            if current_stored_sl is not None:
                # Check if current price has dropped below the trailing stop-loss
                if current_price < current_stored_sl:
                    print(Colors.RED + f"  [TRAILING STOP-LOSS TRIGGERED] {symbol}: Price (Rs.{current_price:.2f}) < Trailing SL (Rs.{current_stored_sl:.2f}) - Closing position!" + Colors.ENDC)
                    # Clear the trailing stop-loss for this symbol since position is closed
                    del trailing_stop_loss_dict[symbol]
                    del trailing_sl_active_dict[symbol]
                    return close_position(symbol, net_qty, exchange)
                else:
                    # Price is still above trailing SL, no action needed
                    print(Colors.GREEN + f"  [TRAILING ACTIVE] {symbol}: Price (Rs.{current_price:.2f}) > Trailing SL (Rs.{current_stored_sl:.2f}) - Holding position" + Colors.ENDC)
            
            # Feature 1: Update trailing stop-loss if price goes higher
            # Only if P&L is positive and final P&L at new trailing SL would be positive
            if pnl_percent > 0:
                new_trailing_sl = current_price * (1 + TRAILING_STOP_LOSS_PERCENT / 100)
                
                # Feature 2: Check if final P&L at new trailing SL price would be positive
                pnl_at_new_sl_percent = ((new_trailing_sl / avg_buy_price) - 1) * 100 if avg_buy_price > 0 else 0
                
                if pnl_at_new_sl_percent > 0:
                    # Feature 1: Ensure trailing stop-loss is always incremental
                    if current_stored_sl is not None:
                        if new_trailing_sl > current_stored_sl:
                            # Only update if the new SL is higher than the previous one
                            trailing_stop_loss_dict[symbol] = new_trailing_sl
                            print(Colors.GREEN + f"  [TRAILING STOP-LOSS UPDATED] {symbol}: P&L positive ({pnl_percent:.2f}%) & Final P&L at new SL positive ({pnl_at_new_sl_percent:.2f}%) - Updated SL: Rs.{new_trailing_sl:.2f} (Previous: Rs.{current_stored_sl:.2f})" + Colors.ENDC)
                        else:
                            # Keep the previous trailing stop-loss (it cannot go down)
                            print(Colors.YELLOW + f"  [TRAILING STOP-LOSS MAINTAINED] {symbol}: New SL (Rs.{new_trailing_sl:.2f}) < Previous SL (Rs.{current_stored_sl:.2f}) - Keeping higher value" + Colors.ENDC)
                    else:
                        # First time setting trailing stop-loss for this symbol
                        trailing_stop_loss_dict[symbol] = new_trailing_sl
                        print(Colors.GREEN + f"  [TRAILING STOP-LOSS SET] {symbol}: Initial SL: Rs.{new_trailing_sl:.2f}" + Colors.ENDC)
                else:
                    print(Colors.YELLOW + f"  [TRAILING STOP-LOSS NOT UPDATED] {symbol}: Final P&L at new SL would be negative ({pnl_at_new_sl_percent:.2f}%) - Keeping previous SL" + Colors.ENDC)
            
            return False
        
        # Trailing stop-loss is NOT active yet - check -0.5% stop-loss first
        # Condition 1: If P&L < -0.5%, close position immediately
        if pnl_percent < STOP_LOSS_PERCENT:
            print(Colors.RED + f"  [STOP-LOSS TRIGGERED] {symbol}: P&L ({pnl_percent:.2f}%) < {STOP_LOSS_PERCENT}% - Closing position!" + Colors.ENDC)
            # Clear the trailing stop-loss for this symbol since position is closed
            if symbol in trailing_stop_loss_dict:
                del trailing_stop_loss_dict[symbol]
            if symbol in trailing_sl_active_dict:
                del trailing_sl_active_dict[symbol]
            return close_position(symbol, net_qty, exchange)
        
        # Condition 2: If P&L increases (price goes up), activate and update trailing stop-loss
        # Only activate trailing SL when P&L becomes positive
        if pnl_percent > 0:
            # New trailing stop-loss based on current price
            new_trailing_sl = current_price * (1 + TRAILING_STOP_LOSS_PERCENT / 100)
            
            # Feature 2: Check if final P&L at trailing SL price would be positive
            pnl_at_trailing_sl_percent = ((new_trailing_sl / avg_buy_price) - 1) * 100 if avg_buy_price > 0 else 0
            
            # Only activate trailing stop-loss if final P&L at that price would be positive
            if pnl_at_trailing_sl_percent > 0:
                # Get the current stored trailing stop-loss for this symbol (if exists)
                current_stored_sl = trailing_stop_loss_dict.get(symbol)
                
                # Feature 1: If we already have a trailing stop-loss set, ensure it doesn't go below the previous value
                # The trailing stop-loss should always be incremental (can go up, but never down)
                if current_stored_sl is not None:
                    if new_trailing_sl > current_stored_sl:
                        # Only update if the new SL is higher than the previous one
                        trailing_stop_loss_dict[symbol] = new_trailing_sl
                        # Mark trailing SL as active
                        trailing_sl_active_dict[symbol] = True
                        print(Colors.GREEN + f"  [TRAILING STOP-LOSS ACTIVATED] {symbol}: P&L positive ({pnl_percent:.2f}%) & Final P&L at SL positive ({pnl_at_trailing_sl_percent:.2f}%) - Updated SL: Rs.{new_trailing_sl:.2f} (Previous: Rs.{current_stored_sl:.2f})" + Colors.ENDC)
                    else:
                        # Keep the previous trailing stop-loss (it cannot go down)
                        # Mark trailing SL as active
                        trailing_sl_active_dict[symbol] = True
                        print(Colors.YELLOW + f"  [TRAILING STOP-LOSS ACTIVATED] {symbol}: P&L positive ({pnl_percent:.2f}%) - SL maintained at Rs.{current_stored_sl:.2f} (new would be Rs.{new_trailing_sl:.2f})" + Colors.ENDC)
                else:
                    # First time setting trailing stop-loss for this symbol
                    trailing_stop_loss_dict[symbol] = new_trailing_sl
                    # Mark trailing SL as active
                    trailing_sl_active_dict[symbol] = True
                    print(Colors.GREEN + f"  [TRAILING STOP-LOSS ACTIVATED] {symbol}: P&L positive ({pnl_percent:.2f}%) & Final P&L at SL positive ({pnl_at_trailing_sl_percent:.2f}%) - Initial SL: Rs.{new_trailing_sl:.2f}" + Colors.ENDC)
                
                # Check if current price has dropped below the trailing stop-loss
                effective_sl = current_stored_sl if current_stored_sl is not None else new_trailing_sl
                if current_price < effective_sl:
                    print(Colors.RED + f"  [TRAILING STOP-LOSS TRIGGERED] {symbol}: Price (Rs.{current_price:.2f}) < Trailing SL (Rs.{effective_sl:.2f}) - Closing position!" + Colors.ENDC)
                    # Clear the trailing stop-loss for this symbol since position is closed
                    del trailing_stop_loss_dict[symbol]
                    del trailing_sl_active_dict[symbol]
                    return close_position(symbol, net_qty, exchange)
            else:
                # Final P&L at trailing SL would be negative, don't activate trailing SL yet
                print(Colors.YELLOW + f"  [TRAILING STOP-LOSS NOT ACTIVATED] {symbol}: P&L positive ({pnl_percent:.2f}%) but Final P&L at SL would be negative ({pnl_at_trailing_sl_percent:.2f}%)" + Colors.ENDC)
        
        return False
        
    except Exception as e:
        print(Colors.RED + f"  [ERROR] Error in trading logic for {symbol}: {e}" + Colors.ENDC)
        return False


def get_exchange_from_position(position_df, symbol):
    """
    Determine the exchange for a symbol from position data.
    """
    try:
        # Try to get exchange from position data
        symbol_data = position_df[position_df['trading_symbol'] == symbol]
        if not symbol_data.empty:
            # Try to extract exchange from trading_symbol (e.g., 'NSE_RELIANCE')
            ts = symbol_data['trading_symbol'].iloc[0]
            if 'BSE_' in ts:
                return "BSE"
            return "NSE"  # Default to NSE for positions
    except:
        pass
    return "NSE"


def is_time_to_close_positions():
    """
    Check if current time is 15:15 or later.
    Market closes at 15:30, so we close all positions at 15:15.
    
    Returns:
        True if it's time to close positions, False otherwise
    """
    now = datetime.now()
    current_time = now.time()
    
    # Market close time is 15:30, so we close at 15:15
    close_time_hour = 15
    close_time_minute = 15
    
    # Convert times to minutes for comparison
    current_minutes = current_time.hour * 60 + current_time.minute
    close_minutes = close_time_hour * 60 + close_time_minute
    
    return current_minutes >= close_minutes


def close_all_positions(position_df, unique_symbols):
    """
    Close all open positions (auto-square off at 15:15).
    
    Parameters:
        position_df: DataFrame containing position data
        unique_symbols: List of unique trading symbols
    
    Returns:
        List of symbols that were closed
    """
    closed_list = []
    
    print(Colors.YELLOW + Colors.BOLD + "\n*** MARKET CLOSING TIME (15:15) - AUTO SQUARE OFF INITIATED ***" + Colors.ENDC)
    print(Colors.YELLOW + f"Current Time: {datetime.now().strftime('%H:%M:%S')}" + Colors.ENDC)
    print()
    
    for symbol in unique_symbols:
        try:
            # Calculate position details
            pnl_data = calculate_position_pnl(position_df, symbol)
            
            # Skip if no net position
            if pnl_data['net_qty'] == 0:
                continue
            
            # Only close long positions (net_qty > 0)
            if pnl_data['net_qty'] > 0:
                exchange = pnl_data.get('exchange', get_exchange_from_position(position_df, symbol))
                
                print(Colors.YELLOW + f"  Closing position for {symbol}: {pnl_data['net_qty']} shares..." + Colors.ENDC)
                
                success = close_position(symbol, pnl_data['net_qty'], exchange)
                
                # Clear the trailing stop-loss for this symbol since position is closed
                if symbol in trailing_stop_loss_dict:
                    del trailing_stop_loss_dict[symbol]
                if symbol in trailing_sl_active_dict:
                    del trailing_sl_active_dict[symbol]
                
                if success:
                    closed_list.append(symbol)
                    print(Colors.GREEN + f"    ✓ {symbol} closed successfully" + Colors.ENDC)
                else:
                    print(Colors.RED + f"    ✗ Failed to close {symbol}" + Colors.ENDC)
            
            time.sleep(1)  # Rate limiting
            
        except Exception as e:
            print(Colors.RED + f"  [ERROR] Failed to close position for {symbol}: {e}" + Colors.ENDC)
            continue
    
    return closed_list


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
        
        # Step 1B: Check if it's time to auto-close positions (15:15)
        if is_time_to_close_positions():
            closed_symbols = close_all_positions(position_df, unique_symbols)
            if closed_symbols:
                print(Colors.GREEN + f"\n  Successfully closed {len(closed_symbols)} positions" + Colors.ENDC)
            # After closing, wait a moment and continue to next iteration
            time.sleep(2)
            continue
        
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
                exchange = pnl_data.get('exchange', get_exchange_from_position(position_df, symbol))
                current_price = get_current_price(symbol, exchange)
                
                if current_price is None:
                    current_price = pnl_data['cost_price']
                
                # Calculate P&L and trending amounts
                current_value = current_price * abs(pnl_data['net_qty'])
                invested_value = pnl_data['cost_price'] * abs(pnl_data['net_qty'])
                
                # Calculate charges for the position (for sell side estimation)
                # Buy charges (already paid when buying)
                buy_charges = calculate_charges(abs(pnl_data['net_qty']), pnl_data['cost_price'], True, exchange)
                # Sell charges (estimated when closing at current price)
                sell_charges = calculate_charges(abs(pnl_data['net_qty']), current_price, False, exchange)
                
                # Total charges (buy charges + estimated sell charges)
                total_charges = buy_charges['total_charges'] + sell_charges['total_charges']
                
                # P&L calculation
                if pnl_data['net_qty'] > 0:  # Long position
                    gross_pnl = (current_price - pnl_data['cost_price']) * pnl_data['net_qty']
                    pnl = gross_pnl - total_charges  # Net P&L after charges
                    pnl_percent = ((current_price / pnl_data['cost_price']) - 1) * 100 if pnl_data['cost_price'] > 0 else 0
                else:  # Short position
                    gross_pnl = (pnl_data['cost_price'] - current_price) * abs(pnl_data['net_qty'])
                    pnl = gross_pnl - total_charges  # Net P&L after charges
                    pnl_percent = ((pnl_data['cost_price'] / current_price) - 1) * 100 if current_price > 0 else 0
                
                # Trending amount
                trending = current_value - invested_value
                trending_percent = ((current_value / invested_value) - 1) * 100 if invested_value > 0 else 0
                
                # Check and execute trading logic (Stop-loss and Trailing Stop)
                position_closed = check_and_execute_trading_logic(
                    pnl_data=pnl_data,
                    current_price=current_price,
                    symbol=symbol,
                    exchange=exchange
                )
                
                # Store result
                results.append({
                    'Symbol': symbol,
                    'Qty': pnl_data['net_qty'],
                    'Avg Buy Price': round(pnl_data['cost_price'], 2),
                    'Current Price': round(current_price, 2),
                    'Invested Value': round(invested_value, 2),
                    'Current Value': round(current_value, 2),
                    'Gross P&L': round(gross_pnl, 2),
                    'Total Charges': round(total_charges, 2),
                    'Net P&L': round(pnl, 2),
                    'Net P&L %': round(pnl_percent, 2),
                    'Trending': round(trending, 2),
                    'Trending %': round(trending_percent, 2),
                    'Position Closed': position_closed
                })
                
            except Exception as e:
                print(Colors.RED + f"Error processing {symbol}: {e}" + Colors.ENDC)
                continue
        
        # Step 4: Display results in a table
        '''print(Colors.BLUE + "-" * 80 + Colors.ENDC)
        print(Colors.BOLD + Colors.GREEN + "  POSITION SUMMARY" + Colors.ENDC)
        print(Colors.BLUE + "-" * 80 + Colors.ENDC)'''
        
        if results:
            # Create DataFrame from results
            results_df = pd.DataFrame(results)
            
            # Sort by Net P&L (descending)
            results_df = results_df.sort_values('Net P&L', ascending=False)
            
            # Display settings
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.float_format', '{:.2f}'.format)
            
            # Print header row - WITH CHARGES
            print()
            print(Colors.BOLD + f"{'Symbol':<12} {'Qty':>6} {'Avg Price':>12} {'Current':>12} "
                  f"{'Inv Value':>12} {'Curr Value':>12} {'Gross P&L':>12} {'Charges':>12} {'Net P&L':>12} {'%':>8}" + Colors.ENDC)
            print(Colors.BLUE + "-" * 130 + Colors.ENDC)
            
            # Print each row with color coding
            for _, row in results_df.iterrows():
                net_pnl_color = Colors.GREEN if row['Net P&L'] >= 0 else Colors.RED
                net_pnl_str = f"{net_pnl_color}{row['Net P&L']:>12.2f}{Colors.ENDC}"
                net_pnl_pct_str = f"{net_pnl_color}{row['Net P&L %']:>7.2f}%{Colors.ENDC}"
                
                print(f"{Colors.BOLD}{row['Symbol']:<12}{Colors.ENDC} "
                      f"{row['Qty']:>6} "
                      f"{row['Avg Buy Price']:>12.2f} "
                      f"{Colors.BOLD}{row['Current Price']:>12.2f}{Colors.ENDC} "
                      f"{row['Invested Value']:>12.2f} "
                      f"{row['Current Value']:>12.2f} "
                      f"{row['Gross P&L']:>12.2f} "
                      f"{Colors.RED}{row['Total Charges']:>12.2f}{Colors.ENDC} "
                      f"{net_pnl_str} {net_pnl_pct_str}")
            
            print(Colors.BLUE + "-" * 130 + Colors.ENDC)
            
            # Calculate totals
            total_invested = results_df['Invested Value'].sum()
            total_current = results_df['Current Value'].sum()
            total_gross_pnl = results_df['Gross P&L'].sum()
            total_charges = results_df['Total Charges'].sum()
            total_net_pnl = results_df['Net P&L'].sum()
            total_trending = results_df['Trending'].sum()
            total_pnl_percent = ((total_current / total_invested) - 1) * 100 if total_invested > 0 else 0
            
            # Show closed positions summary
            closed_positions = results_df[results_df['Position Closed'] == True]
            if not closed_positions.empty:
                print()
                print(Colors.RED + Colors.BOLD + "  *** POSITIONS CLOSED THIS CYCLE ***" + Colors.ENDC)
                for _, row in closed_positions.iterrows():
                    print(Colors.RED + f"    - {row['Symbol']}: Sold {row['Qty']} shares at Rs.{row['Current Price']}" + Colors.ENDC)
                print()
            
            # Color total Net P&L
            total_pnl_color = Colors.GREEN if total_net_pnl >= 0 else Colors.RED
            
            print(Colors.BOLD)
            print(f"{'TOTAL':<12} {'':<6} {'':<12} {'':<12} "
                  f"{total_invested:>12.2f} {total_current:>12.2f} "
                  f"{total_gross_pnl:>12.2f} {Colors.RED}{total_charges:>12.2f}{Colors.ENDC} "
                  f"{total_pnl_color}{total_net_pnl:>12.2f}{Colors.ENDC} "
                  f"{total_pnl_color}{total_pnl_percent:>7.2f}%{Colors.ENDC}")
            print(Colors.BLUE + "-" * 130 + Colors.ENDC)
            
            # Summary indicators
            print()
            if total_net_pnl >= 0:
                print(Colors.GREEN + f"  Total Net Profit: Rs.{total_net_pnl:,.2f} ({total_pnl_percent:.2f}%)" + Colors.ENDC)
            else:
                print(Colors.RED + f"  Total Net Loss: Rs.{abs(total_net_pnl):,.2f} ({total_pnl_percent:.2f}%)" + Colors.ENDC)
            
            print(Colors.YELLOW + f"  Portfolio Value: Rs.{total_current:,.2f} | Trending: Rs.{total_trending:,.2f} | Total Charges: Rs.{total_charges:,.2f}" + Colors.ENDC)
            
        else:
            print(Colors.YELLOW + "  No open positions to display." + Colors.ENDC)
        
        print()
        '''print(Colors.BLUE + "=" * 80 + Colors.ENDC)
        print(Colors.YELLOW + "  Next update in 2 seconds... (Press Ctrl+C to stop)" + Colors.ENDC)
        print(Colors.BLUE + "=" * 80 + Colors.ENDC)'''
        
        # Wait 2 seconds before next update
        time.sleep(1)


# Run the main function
if __name__ == "__main__":
    main()
