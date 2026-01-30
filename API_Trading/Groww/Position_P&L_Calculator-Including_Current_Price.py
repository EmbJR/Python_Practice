from growwapi import GrowwAPI
import pandas as pd
import time as tm

# Groww API Credentials (Replace with your actual credentials)
API_AUTH_TOKEN = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3Njk4MTk0MDAsImlhdCI6MTc2OTc2MjQyMywibmJmIjoxNzY5NzYyNDIzLCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCJiOWFkYTJjZC0zMDk3LTQwMWItYTdmMS01YjlmMWZlY2U0MGVcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcImM0NzhkYjU1LTcyNjYtNDA1Zi1iYTQ5LWIxMjEyY2Y2ZjZhZVwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcIm9yZGVyLWJhc2ljLGxpdmVfZGF0YS1iYXNpYyxub25fdHJhZGluZy1iYXNpYyxvcmRlcl9yZWFkX29ubHktYmFzaWNcIixcInNvdXJjZUlwQWRkcmVzc1wiOlwiMjQwNToyMDE6MjAxZjoyODVkOjUwOGE6NTFlMjo0NWIwOjM4OTMsMTYyLjE1OC4yMjcuNDYsMzUuMjQxLjIzLjEyM1wiLFwidHdvRmFFeHBpcnlUc1wiOjE3Njk4MTk0MDAwMDB9IiwiaXNzIjoiYXBleC1hdXRoLXByb2QtYXBwIn0.hzmdv3gbAPKq9AKXnWcJ8nUrlNZVyQhAuOAzNdNChG4lGdgoiCkGy2dtmATzvoKD6Oib_O0JYiLqyj9__WF-rA"
 
 # Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)

'''
LTP_Reliance = "NSE_RELIANCE"
print(groww.get_ltp(exchange_trading_symbols=LTP_Reliance, segment=groww.SEGMENT_CASH))
'''


tm.sleep(1)
print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
position_response = groww.get_positions_for_user()

PositionDataFrame = pd.DataFrame(position_response['positions'])
#print(PositionDataFrame.columns)
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
        #print(symbol)

        #Below lines creates the 2 new columns in the table for calculated prices for buy and sell with quantity
        #Also it will export the data to CSV document if the "symbol.to_csv()" line is uncommented.
        symbol['Total_credit_Price'] = symbol['credit_price'].fillna(0) * symbol['credit_quantity'].fillna(0)
        symbol['Total_debit_Price'] = symbol['debit_price'].fillna(0) * symbol['debit_quantity'].fillna(0)
        #symbol.to_csv(f"converted_prices{PositionName}.csv")
        
        exchangename = symbol['exchange']
        #print(f">>>>>>>>>>>>>>>> {exchangename} <<<<<<<<<<<<<<<<<<<<<<<<")
        if 'NSE' not in exchangename.values:
            symbolMod = f"BSE_{PositionName}"
        else:
            symbolMod = f"NSE_{PositionName}"
        LTP_OfSymbol = groww.get_ltp(exchange_trading_symbols=symbolMod, segment=groww.SEGMENT_CASH)


        # Calculate sum of credit_quantity or Buy pricing
        total_credit_price = symbol['Total_credit_Price'].sum()
        total_credit_Average = total_credit_price / total_credit_quantity

        total_debit_quantity = 0
        # Check if debit quantity information is available
        if total_debit_quantity == 0:
            # Use current price as debit price and credit quantity as debit quantity
            total_debit_Average = LTP_OfSymbol[symbolMod]  # Get LTP from API
            total_debit_quantity = total_credit_quantity  # Use credit quantity as debit quantity
            print(">>> Using Current Price as Debit Price <<<")
            print(f">>> Using Credit Quantity as Debit Quantity <<<")
        else:
            # Use actual debit price and quantity
            total_debit_Average = symbol['Total_debit_Price'].sum() / total_debit_quantity

        # Check if debit quantity information is available
        if total_credit_quantity == 0:
            # Use current price as debit price and credit quantity as debit quantity
            total_credit_Average = LTP_OfSymbol[symbolMod]  # Get LTP from API
            total_credit_quantity = total_debit_quantity  # Use credit quantity as debit quantity
            print(">>> Using Current Price as Debit Price <<<")
            print(f">>> Using Credit Quantity as Debit Quantity <<<")
        else:
            # Use actual debit price and quantity
            total_credit_Average = symbol['Total_credit_Price'].sum() / total_credit_quantity


        # Calculate ProfitPer based on available data
        PL_Persent = ((total_debit_Average / total_credit_Average) - 1) * 100
        #Total profit and loss calculations in Ruppe
        PL_Ammount = symbol['Total_credit_Price'].sum()*(PL_Persent/100)

        print('Total Average buy price      = ', total_credit_Average)
        print('Total buy Qty                = ', total_credit_quantity)

        print('Total Average sell price     = ', total_debit_Average)
        print('Total sellQty                = ', total_debit_quantity)

        print(f"Total P&L persent            = {PL_Persent}")
        print(f"Total P&L Ammount            = {PL_Ammount}")