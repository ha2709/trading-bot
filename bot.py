import alpaca_trade_api as tradeapi
import time

# Replace these values with your Alpaca API key and secret
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use 'https://api.alpaca.markets' for live trading

api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version='v2')

def get_account_information():
    account = api.get_account()
    return account

def get_latest_price(symbol):
    latest_price = api.get_latest_trade(symbol).price
    return latest_price

def place_market_order(symbol, quantity, side):
    api.submit_order(
        symbol=symbol,
        qty=quantity,
        side=side,
        type='market',
        time_in_force='gtc'
    )

def simple_trading_strategy(symbol):
    # Replace this strategy with your own logic
    current_price = get_latest_price(symbol)
    
    # For demonstration purposes, let's place a market order if the price is above $100
    if current_price > 100:
        place_market_order(symbol, 1, 'buy')
    else:
        place_market_order(symbol, 1, 'sell')

if __name__ == "__main__":
    symbol_to_trade = 'AAPL'  # Replace with the symbol you want to trade

    while True:
        try:
            account_info = get_account_information()
            print(f"Account Cash: ${account_info.cash}")

            simple_trading_strategy(symbol_to_trade)

            time.sleep(60)  # Sleep for 60 seconds before the next iteration
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # Sleep for 60 seconds in case of an error to avoid excessive API requests
