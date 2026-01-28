from growwapi import GrowwAPI

api_key = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjI1NTc5OTQ0MjUsImlhdCI6MTc2OTU5NDQyNSwibmJmIjoxNzY5NTk0NDI1LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCJhMzE1YzI5ZS0xODVmLTRmZDgtYjU5OS02OGFkN2VjZjA2YjdcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiYzVkZjhiMGUtZTg5Ni00MmIyLWEzYjUtNzg5MmNiMDllMGY0XCIsXCJkZXZpY2VJZFwiOlwiZDFjZmEzZjgtMzFmYS01ZjcwLWJjN2MtMjUxMDA0ZTU1MGQxXCIsXCJzZXNzaW9uSWRcIjpcIjFlYzcyMTRkLWI5YjktNGVkMy05MTc5LWIzNzFlZDUwYTZkMVwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYksxMnV6S0FTTkdXV3VYZGtEdy9jSEZSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcImF1dGgtdG90cFwiLFwic291cmNlSXBBZGRyZXNzXCI6XCIyNDA1OjIwMToyMDFmOjI4NWQ6OTE4Njp4YWQ3OmFkOWU6NDDdkOSwxNzIuNzAuMjE5Ljk3LDM1Ljk3Mi4yMy4xMTlcIixcInR3b0ZhRXhwaXJ5VHNcIjoyNTU3OTk0NDI1NTMzfSIsImlzcyI6ImFwZXgtYXV0aC1wcm9kLWFwcCJ9.ohqRZR7JGZj4qWtcwqM8HnpGrHTW6i1mVWo6dhEWqKwa8DHlSeMEG--DJjg0wcBJyLb9pt1oxX7KGLUXV9-l5Q"
secret = "CefogWoUcp75gG3nG*GF$_VKT6B"
 
access_token = GrowwAPI.get_access_token(api_key=api_key, secret=secret)
# Use access_token to initiate GrowwAPI
groww = GrowwAPI(access_token)
print("✅ Ready to Groww")

# =====================
# STEP 2: Place BUY Order
# =====================

trading_symbol = "IDEA"  #Vodafone Idea Ltd
quantity = 1    #Set the quantity you want to buy 
 

#Ensure you have sufficient funds in your Groww account for this order

try:
    # Place a MARKET BUY order
    print(f"Placing MARKET BUY order for {trading_symbol}")
    buy_order_id = groww.place_order(
        trading_symbol=trading_symbol, 
        quantity=quantity, 
        validity=groww.VALIDITY_DAY,
        exchange=groww.EXCHANGE_NSE, 
        segment=groww.SEGMENT_CASH,
        product=groww.PRODUCT_MIS,
        order_type=groww.ORDER_TYPE_MARKET,
        transaction_type=groww.TRANSACTION_TYPE_BUY
    )

    print(f"✅ BUY order placed for {trading_symbol}. Order ID: {buy_order_id['groww_order_id']}") 
    # This will print the order ID of the placed order

except Exception as e: 
    print(f"❌ Failed to place BUY order: {e}")
    exit(1)

# =====================
# STEP 3: Wait 10 seconds
# =====================
print("⏳ Waiting for 10 secs before placing SELL order...")
time.sleep(10)

# =====================
# STEP 4: Place SELL Order
# =====================

#Place a MARKET SELL order
try:
    print(f"Placing MARKET SELL order for {trading_symbol}")

    sell_order_id = groww.place_order(
        trading_symbol=trading_symbol,
        quantity=quantity,
        validity=groww.VALIDITY_DAY,
        exchange=groww.EXCHANGE_NSE,
        segment=groww.SEGMENT_CASH,
        product=groww.PRODUCT_MIS,
        order_type=groww.ORDER_TYPE_MARKET,
        transaction_type=groww.TRANSACTION_TYPE_SELL
    )

    print(f"✅ SELL order placed for {trading_symbol}. Order ID: {sell_order_id['groww_order_id']}")  
    # This will print the order ID of the placed order

except Exception as e:
    print(f"❌ Failed to place SELL order: {e}")