import os

import pandas
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API_KEY
}

# response = requests.get(url, params=stock_params)
# stock_data = response.json()
# historical_data = stock_data.get("Time Series (Daily)")
# data_df = pandas.DataFrame.from_dict(historical_data)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo").json()
historical_data = response.get("Time Series (Daily)")
# print(historical_data)
first_key = next(iter(historical_data))
most_recent_open = float(historical_data.get(first_key).get("1. open"))
for key in historical_data:
    current_day_open = float(historical_data.get(key).get("1. open"))
    try:
        if (abs(current_day_open - most_recent_open) / most_recent_open >= 0.05):
            print(f"get news for {key}")
    except:
        print("No 5% swings")
    finally:
        most_recent_open = current_day_open

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
