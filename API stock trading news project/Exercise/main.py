import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = "JDIR5HEC1AZL0PH4"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = { "function": "TIME_SERIES_DAILY",
               "symbol": STOCK_NAME,
               "apikey": api_key,
               }
news_apikey = "0a657becb0d84c8ca35a666a0a965b9d"
news_parameters = { "q": COMPANY_NAME,
                    "apiKey": news_apikey,
                    }
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
daily = data["Time Series (Daily)"]
daily_list = list(daily.items())
previous_day_closing_price = float(daily_list[0][1]["4. close"])


# Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = float(daily_list[1][1]["4. close"])

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_between_closing_price = abs(previous_day_closing_price - day_before_yesterday_closing_price)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (difference_between_closing_price/ day_before_yesterday_closing_price) * 100

#If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 5:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    news = news_data["articles"]
    recent_news = news[0:3]
    print(recent_news)
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

# Create a new list of the first 3 article's headline and description using list comprehension.
    news_list = [{"headline" : article["title"], "brief": article["description"]} for article in recent_news]
    print(news_list)
