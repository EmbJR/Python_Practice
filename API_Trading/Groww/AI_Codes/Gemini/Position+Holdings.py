import time
from rich.live import Live
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
from growwapi import GrowwAPI

# --- SETUP ---
API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3NzEyODgyMDAsImlhdCI6MTc3MTIxNzM5OSwibmJmIjoxNzcxMjE3Mzk5LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCI0YTUzNDhkZi1lZTc1LTQ2NmUtODQxOC1jZjIwYzdiMjc5NjlcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjU2N2QzMjhhLWFmZDAtNDFkZC04OGUyLWFiMDdkNjYzNGFhOFwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOmVjMDQ6NDFmOjhkMDg6N2Q5MSwxNzIuNzAuMjE5Ljg3LDM1LjI0MS4yMy4xMjNcIixcInR3b0ZhRXhwaXJ5VHNcIjoxNzcxMjg4MjAwMDAwfSIsImlzcyI6ImFwZXgtYXV0aC1wcm9kLWFwcCJ9.pCSSsYEcqVthtllSnZM8bRIwdErBUdm9aiDt7BBGenwWNheh93tjSHGB7C6wPTksITkTiYrc054Emhqln_6DJQ"
groww = GrowwAPI(API_AUTH_TOKEN)

def calculate_net_intraday(gross_pnl, turnover, orders):
    # Simplified Intraday Tax Logic (0.025% Sell STT + Brokerage + GST)
    taxes = (orders * 20) + (turnover * 0.00015) + ((orders * 20) * 0.18)
    return gross_pnl - taxes, taxes

def generate_dashboard():
    layout = Layout()
    layout.split_row(
        Layout(name="intraday"),
        Layout(name="holdings")
    )

    # --- INTRADAY SECTION ---
    intra_table = Table(title="Live Intraday (Net)")
    intra_table.add_column("Symbol")
    intra_table.add_column("Net P&L", justify="right")
    
    pos_res = groww.get_positions_for_user()
    total_intra_net = 0
    if pos_res.get('status') == 'SUCCESS':
        for pos in pos_res['payload']['positions']:
            symbol, qty, avg = pos['trading_symbol'], pos['quantity'], pos['net_price']
            ltp = groww.get_ltp(groww.SEGMENT_CASH, f"NSE-{symbol}").get('last_price', 0)
            
            gross = (ltp - avg) * qty
            turnover = (avg + ltp) * abs(qty)
            net, _ = calculate_net_intraday(gross, turnover, 2)
            
            color = "green" if net >= 0 else "red"
            intra_table.add_row(symbol, f"[{color}]₹{net:.2f}[/{color}]")
            total_intra_net += net

    # --- HOLDINGS SECTION ---
    hold_table = Table(title="Demat Holdings")
    hold_table.add_column("Stock")
    hold_table.add_column("Unrealized P&L", justify="right")
    
    hold_res = groww.get_holdings_for_user()
    total_hold_pnl = 0
    if hold_res.get('status') == 'SUCCESS':
        for item in hold_res['payload']['holdings']:
            symbol, qty, avg = item['trading_symbol'], item['quantity'], item['average_price']
            ltp = groww.get_ltp(groww.SEGMENT_CASH, f"NSE-{symbol}").get('last_price', 0)
            
            pnl = (ltp - avg) * qty
            color = "green" if pnl >= 0 else "red"
            hold_table.add_row(symbol, f"[{color}]₹{pnl:.2f}[/{color}]")
            total_hold_pnl += pnl

    # Update Layout
    layout["intraday"].update(Panel(intra_table, subtitle=f"Total Net: ₹{total_intra_net:.2f}"))
    layout["holdings"].update(Panel(hold_table, subtitle=f"Total P&L: ₹{total_hold_pnl:.2f}"))
    
    return layout

if __name__ == "__main__":
    with Live(generate_dashboard(), refresh_per_second=1) as live:
        while True:
            time.sleep(5) # Refresh every 5 seconds
            live.update(generate_dashboard())
