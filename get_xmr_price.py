#!/usr/bin/env python3
import json
import sys
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

credentials_path = sys.argv[1]
#print(f"Opening credentials file: {credentials_path}")
with open(credentials_path) as cred_file:
    creds = json.load(cred_file)

client = Client(creds["api_key"], creds["secret_key"])

xmr_price = float(client.get_avg_price(symbol='XMRUSDT')['price'])
print(f"Monero: ${xmr_price:.2f}")

binance_monero = float(client.get_asset_balance(asset='XMR')['free'])
wallet_monero = 0.325595831374
total_usdt = xmr_price * (binance_monero + wallet_monero)
print(f"Worth: ${total_usdt:.2f}")

