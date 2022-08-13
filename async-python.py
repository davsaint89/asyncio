import asyncio
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ALPHAVANTAGE_KEY")
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']
results = []

def run_tasks():
    for symbol in symbols:
        resp = requests.get(url.format(symbol, api_key))
        results.append(resp.json())

print("Timer started...")
start = time.time()
run_tasks()
end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
print(results)

