import sys
import requests
import json

try:
    bit_price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = bit_price.json()

    for currency, tem in o['bpi'].items():
        if currency == 'USD':
            bitcoin_price = float(tem['rate'].replace(',', ''))
            try:
                usd_amount = float(sys.argv[1])
                bitcoin_value = bitcoin_price * usd_amount
                print(f'Bitcoin price (USD): {bitcoin_price}')
                print(f'Equivalent Bitcoin value for {usd_amount} USD: {bitcoin_value:,.4f}')
            except ValueError:
                print("Invalid input. Please enter a valid numeric value for USD.")
            except IndexError:
                print("Pls enter any int in command argument")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
