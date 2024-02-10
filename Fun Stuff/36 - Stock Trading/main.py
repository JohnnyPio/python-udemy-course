import os

import pandas
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

news_url = "https://newsapi.org/v2/top-headlines"
news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(stock_url, stock_params).json()
historical_data = response.get("Time Series (Daily)")
current_key = next(iter(historical_data))
keys = list(historical_data.keys())
current_index = keys.index(current_key)
most_recent_close = float(historical_data.get(current_key).get("4. close"))
for key in historical_data:
    current_day_open = float(historical_data.get(key).get("1. open"))
    if abs(current_day_open - most_recent_close) / most_recent_close >= 0.05:
        ## STEP 2: Use https://newsapi.org
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
        news_response = requests.get(news_url, news_params)
        news = news_response.json().get("articles")
        for new in news[:2]:
            title = new.get("title")
            print(str(current_key) + " " + title)
    current_key = keys[current_index + 1]
    current_day_close = float(historical_data.get(key).get("4. close"))
    most_recent_close = current_day_close

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
