import time
from growwapi import GrowwAPI

# 1. SETUP YOUR CREDENTIALS
# Get your API Token from: https://groww.in/trade-api/docs
API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3NzEyODgyMDAsImlhdCI6MTc3MTIxNzM5OSwibmJmIjoxNzcxMjE3Mzk5LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCI0YTUzNDhkZi1lZTc1LTQ2NmUtODQxOC1jZjIwYzdiMjc5NjlcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjU2N2QzMjhhLWFmZDAtNDFkZC04OGUyLWFiMDdkNjYzNGFhOFwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOmVjMDQ6NDFmOjhkMDg6N2Q5MSwxNzIuNzAuMjE5Ljg3LDM1LjI0MS4yMy4xMjNcIixcInR3b0ZhRXhwaXJ5VHNcIjoxNzcxMjg4MjAwMDAwfSIsImlzcyI6ImFwZXgtYXV0aC1wcm9kLWFwcCJ9.pCSSsYEcqVthtllSnZM8bRIwdErBUdm9aiDt7BBGenwWNheh93tjSHGB7C6wPTksITkTiYrc054Emhqln_6DJQ"

# Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)

def track_live_pnl():
    print(f"{'Symbol':<15} | {'Qty':<8} | {'Avg Price':<12} | {'LTP':<10} | {'P&L':<10}")
    print("-" * 65)

    try:
        # 2. FETCH CURRENT POSITIONS
        response = groww.get_positions_for_user()
        
        if response.get('status') == 'SUCCESS':
            positions = response['payload']['positions']
            total_pnl = 0

            for pos in positions:
                symbol = pos['trading_symbol']
                qty = pos['quantity']
                avg_price = pos['net_price'] # Average buy price
                
                # 3. GET CURRENT MARKET PRICE (LTP)
                # We fetch LTP to calculate 'Trending' (Live) P&L
                market_data = groww.get_ltp(
                    segment=groww.SEGMENT_CASH, 
                    groww_symbol=f"NSE-{symbol}"
                )
                ltp = market_data.get('last_price', 0)

                # 4. CALCULATE P&L
                # P&L = (Current Price - Buy Price) * Quantity
                unrealized_pnl = (ltp - avg_price) * qty
                total_pnl += unrealized_pnl

                print(f"{symbol:<15} | {qty:<8} | {avg_price:<12.2f} | {ltp:<10.2f} | {unrealized_pnl:<10.2f}")

            print("-" * 65)
            print(f"TOTAL UNREALIZED P&L: ₹{total_pnl:.2f}")
        else:
            print("Error fetching positions:", response.get('message'))

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the tracker
if __name__ == "__main__":
    # You can wrap this in a while loop with a sleep timer for live updates
    track_live_pnl()