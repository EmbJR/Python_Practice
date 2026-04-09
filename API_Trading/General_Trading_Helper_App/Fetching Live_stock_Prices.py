import yfinance as yf
import time
from datetime import datetime
import sys

def track_iex_price():
    """
    Track and print the live market price of IEX (Indian stock) every 5 seconds.
    IEX is listed on NSE (National Stock Exchange of India).
    """
    ticker = "IEX.NS"  # IEX stock on NSE (National Stock Exchange, India)
    
    print(f"Tracking IEX stock price (Updated every 5 seconds)")
    print(f"Ticker: {ticker}")
    print("-" * 70)
    
    try:
        while True:
            try:
                # Fetch the stock data
                stock = yf.Ticker(ticker)
                data = stock.history(period='1d')
                
                # Get current price
                current_price = stock.info.get('currentPrice') or stock.info.get('ask')
                
                # If current price not available, use last trade price
                if not current_price and len(data) > 0:
                    current_price = data['Close'].iloc[-1]
                
                # Get additional information
                previous_close = stock.info.get('previousClose', 'N/A')
                change = current_price - previous_close if current_price and previous_close != 'N/A' else 'N/A'
                change_percent = (change / previous_close * 100) if change != 'N/A' else 'N/A'
                
                # Print the information with timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] IEX Price: ₹{current_price:.2f} | Previous Close: ₹{previous_close:.2f} | Change: ₹{change:.2f} ({change_percent:.2f}%)" if change_percent != 'N/A' else f"[{timestamp}] IEX Price: ₹{current_price:.2f}")
                
            except Exception as e:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] Error fetching price: {str(e)}")
            
            # Wait for 5 seconds before fetching again
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n" + "-" * 70)
        print("Price tracking stopped by user (Ctrl+C)")
        sys.exit(0)

if __name__ == "__main__":
    track_iex_price()
