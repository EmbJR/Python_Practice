from growwapi import GrowwAPI
import pandas as pd
# Groww API Credentials (Replace with your actual credentials)
#API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjI1NTc5OTQ0MjUsImlhdCI6MTc2OTU5NDQyNSwibmJmIjoxNzY5NTk0NDI1LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCJhMzE1YzI5ZS0xODVmLTRmZDgtYjU5OS02OGFkN2VjZjA2YjdcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjFlYzcyMTRkLWI5YjktNGVkMy05MTc5LWIzNzFlZDUwYTZkMVwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcImF1dGgtdG90cFwiLFwic291cmNlSXBBZGRyZXNzXCI6XCIyNDA1OjIwMToyMDFmOjI4NWQ6OTE4NjphZDdmOjkwMmU6NDJkZSwxNzIuNzAuMjE5Ljg4LDM1LjI0MS4yMy4xMjNcIixcInR3b0ZhRXhwaXJ5VHNcIjoyNTU3OTk0NDI1NTMzfSIsImlzcyI6ImFwZXgtYXV0aC1wcm9kLWFwcCJ9.ohqRZR7JGZj4qWtcwqM8HnpGrHTW6i1mVWo6dhEWqKwa8DHlSeMEG--DJjg0wcBJyLb9pt1oxX7KGLUXV9-l5Q"

API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3Njk2NDY2MDAsImlhdCI6MTc2OTYwMTcyNiwibmJmIjoxNzY5NjAxNzI2LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCIxMWEzYmJlNC05ZjYwLTRhOGUtODA2YS05MTRmYTE2NTE1NjlcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjY2MDQ2NmUwLWE5ZDQtNGQ0MS1hMzcyLWNlMzNkOThmNzg5Y1wiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOjkxODY6YWQ3Zjo5MDJlOjQyZGUsMTcyLjcwLjIxOC4yMywzNS4yNDEuMjMuMTIzXCIsXCJ0d29GYUV4cGlyeVRzXCI6MTc2OTY0NjYwMDAwMH0iLCJpc3MiOiJhcGV4LWF1dGgtcHJvZC1hcHAifQ.SQwzWdnIJd5Fk0K26BgdmGuLQNf0FlEZaVc8YK581L1HplXAauYmKZGX-mV2HAcy3ApB3nuSoI9Pc4bZjRJqaw"
 
 # Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)

'''
LTP_Reliance = "NSE_RELIANCE"
print(groww.get_ltp(exchange_trading_symbols=LTP_Reliance, segment=groww.SEGMENT_CASH))
'''

holdings_response = groww.get_holdings_for_user()
HoldingData = pd.DataFrame( holdings_response['holdings'] )
print(HoldingData.head(10))

StockNamesPD = HoldingData['trading_symbol']
# I have the panda database named "StockNamesPD". I want to list all of the parameters all coloumn data in this database
# So I convert it to a list
# Example:-
StockNames = list(HoldingData.columns)
print(StockNames)

for symbol in StockNamesPD:
    
    Exchange = HoldingData[HoldingData['trading_symbol'] == symbol]['tradable_exchanges']
    ExchangeList = Exchange.tolist()
    if ExchangeList is not None and len(ExchangeList) > 0:
        if 'NSE' not in ExchangeList[0]:
            symbolMod = f"BSE_{symbol}"
        else:
            symbolMod = f"NSE_{symbol}"
        #print({symbol}, {symbolMod})

        LTP_All_Stocks = groww.get_ltp(exchange_trading_symbols=symbolMod, segment=groww.SEGMENT_CASH)
        AveragePrice = HoldingData[HoldingData['trading_symbol'] == symbol]['average_price']
        Quantity = HoldingData[HoldingData['trading_symbol'] == symbol]['quantity']
        profit_loss = ((float(LTP_All_Stocks[symbolMod]) / float(AveragePrice.tolist()[0]))*100) - 100
        #print(type(LTP_All_Stocks))
        #print({symbol}, {LTP_All_Stocks}, {AveragePrice.tolist()[0]}, {Quantity.tolist()[0]}, profit_loss)
        print({symbol}, "           ", profit_loss, '%')