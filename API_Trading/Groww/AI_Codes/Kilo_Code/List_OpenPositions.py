''' I need to write the python code to list all of the open positions in the portfolios and also list down its P&L considering all the government charges in india.
I am using Groow API for this.'''

Here's a Python script that uses the Groow API to list all open positions in your portfolios and calculate the P&L (Profit and Loss) considering all government charges in India:

import requests
import json

# Replace these with your actual Groow API credentials
GROOW_API_KEY = 'eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3NzEyODgyMDAsImlhdCI6MTc3MTIxNzM5OSwibmJmIjoxNzcxMjE3Mzk5LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCI0YTUzNDhkZi1lZTc1LTQ2NmUtODQxOC1jZjIwYzdiMjc5NjlcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjU2N2QzMjhhLWFmZDAtNDFkZC04OGUyLWFiMDdkNjYzNGFhOFwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOmVjMDQ6NDFmOjhkMDg6N2Q5MSwxNzIuNzAuMjE5Ljg3LDM1LjI0MS4yMy4xMjNcIixcInR3b0ZhRXhwaXJ5VHNcIjoxNzcxMjg4MjAwMDAwfSIsImlzcyI6ImFwZXgtYXV0aC1wcm9kLWFwcCJ9.pCSSsYEcqVthtllSnZM8bRIwdErBUdm9aiDt7BBGenwWNheh93tjSHGB7C6wPTksITkTiYrc054Emhqln_6DJQ'
GROOW_API_SECRET = 'your_api_secret_here'
BASE_URL = 'https://api.groow.in/v1'

# Headers for API requests
headers = {
    'Content-Type': 'application/json',
    'X-API-KEY': GROOW_API_KEY,
    'X-API-SECRET': GROOW_API_SECRET
}

def get_open_positions():
    """Fetch all open positions from Groow API"""
    endpoint = f"{BASE_URL}/positions"
    params = {
        'status': 'open'  # Only fetch open positions
    }

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching positions: {e}")
        return None

def calculate_pnl_with_charges(positions):
    """Calculate P&L for all open positions considering government charges"""
    total_pnl = 0
    for position in positions:
        # Assuming the position has 'quantity', 'buy_price', 'sell_price', and 'charges' fields
        pnl = (position['sell_price'] - position['buy_price']) * position['quantity'] - position['charges']
        total_pnl += pnl
    return total_pnl
    
def main():
    # Get all open positions
    positions = get_open_positions()
    if not positions:
        print("No open positions found or error occurred.")
        return

    # Print all open positions
    print("Open Positions:")
    for position in positions:
        print(f"Symbol: {position['symbol']}, Quantity: {position['quantity']}, "
              f"Buy Price: {position['buy_price']}, Sell Price: {position['sell_price']}, "
              f"Charges: {position['charges']}")

    # Calculate and print P&L with charges
    pnl = calculate_pnl_with_charges(positions)
    print(f"\nTotal P&L (after government charges): {pnl}")

if __name__ == "__main__":
    main()
"""List all open positions and calculate P&L after government charges."""