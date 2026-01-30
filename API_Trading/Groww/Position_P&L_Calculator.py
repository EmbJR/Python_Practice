from growwapi import GrowwAPI
import pandas as pd

# Groww API Credentials (Replace with your actual credentials)
API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3Njk3MzMwMDAsImlhdCI6MTc2OTY3MDg4NywibmJmIjoxNzY5NjcwODg3LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCI1OTBmN2M3OS1kOTlmLTRjMjEtYTI5My05NTg0ZTkxYjU0MWJcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjk2MGYxNWE0LTI3NTgtNGFjNi1iZDkyLTAxNGQ1NWEyNTFkM1wiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOmNkNDU6ZDI3OTo3NWVlOmM1YTYsMTcyLjcwLjIxOC42OSwzNS4yNDEuMjMuMTIzXCIsXCJ0d29GYUV4cGlyeVRzXCI6MTc2OTczMzAwMDAwMH0iLCJpc3MiOiJhcGV4LWF1dGgtcHJvZC1hcHAifQ.6g9BertHaWtJzhIQq30f47FYT4-VvWqOOigCgOpxIhUwMhswyVfmajWGTSXPMVSwrZ4BmZiFmx_5JFfbLN4xBA"
 
 # Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)

'''
LTP_Reliance = "NSE_RELIANCE"
print(groww.get_ltp(exchange_trading_symbols=LTP_Reliance, segment=groww.SEGMENT_CASH))
'''

position_response = groww.get_positions_for_user()

PositionDataFrame = pd.DataFrame(position_response['positions'])
print(PositionDataFrame.columns)
#PositionDataFrame.to_csv('positions.csv')  # Extract the CSV file

PositionList = PositionDataFrame['trading_symbol'].unique().tolist()

# Print unique position names
for PositionName in PositionList:
    #print(PositionName)
    symbol = PositionDataFrame[(PositionDataFrame['trading_symbol'] == PositionName) & 
                                (PositionDataFrame['product'] == groww.PRODUCT_MIS)].copy()
    total_credit_quantity = symbol['credit_quantity'].sum()
    total_debit_quantity = symbol['debit_quantity'].sum()

    if (total_credit_quantity > 0) or (total_debit_quantity > 0):

        print(f"-------------------------- {PositionName} -------------------------------")
        print(symbol)

        #Below lines creates the 2 new columns in the table for calculated prices for buy and sell with quantity
        #Also it will export the data to CSV document if the "symbol.to_csv()" line is uncommented.
        symbol['Total_credit_Price'] = symbol['credit_price'].fillna(0) * symbol['credit_quantity'].fillna(0)
        symbol['Total_debit_Price'] = symbol['debit_price'].fillna(0) * symbol['debit_quantity'].fillna(0)
        #symbol.to_csv(f"converted_prices{PositionName}.csv")
        
        # Calculate sum of credit_quantity or Buy pricing
        total_credit_price = symbol['Total_credit_Price'].sum()
        total_credit_quantity = symbol['credit_quantity'].sum()
        total_credit_Average = total_credit_price / total_credit_quantity

        # Calculate sum of debit_quantity or sell pricing
        total_debit_price = symbol['Total_debit_Price'].sum()
        total_debit_quantity = symbol['debit_quantity'].sum()
        total_debit_Average = total_debit_price / total_debit_quantity

        # Calculate the % change of perticular stock.
        ProfitPer = ((total_debit_Average/total_credit_Average) - 1) *100

        print('Total Average buy price      = ', total_credit_Average)
        print('Total buy Qty                = ', total_credit_quantity)

        print('Total Average sell price     = ', total_debit_Average)
        print('Total sellQty                = ', total_debit_quantity)

        print("Total P&L price              = ", (total_debit_price - total_credit_price))
        print(f"Total P&L persent            = {ProfitPer}")
       