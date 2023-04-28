import requests
from datetime import date, timedelta
from django.core.paginator import Paginator


def get_by_date(search_date: date) -> str:
    date_str = str(search_date)
    url_with_date = f"https://newsapi.org/v2/everything?q=Apple&from={date_str}&sortBy=popularity&apiKey=8f54a81462ca49b1877121daa8704e06"
    return url_with_date

def generate_dates(start_date: date, end_date: date) -> list[date]:
    dates_list = []
    current_date = start_date
    while current_date != end_date:
        dates_list.append(current_date)
        current_date = current_date + timedelta(days=1)
    return dates_list

def extract_data(url: str) -> dict:
    response = requests.get(url)
    data = response.json()
    articles = data['articles'][:10] #
    result = [] #
    for article in articles:
        result.append({'Source': article['source']['name'],'Author':article['author'],'Title':article['title'],'Description':article['description'],'Article':article['content'],'Url': article['url']})
    return result#

def order_by(news_data: list, key: str) -> list:

    order_func = lambda data: data[key].lower()
    news_data_ordered = sorted(news_data, key=order_func)

    return news_data_ordered


    # return data


# dates = generate_dates(date(2023, 4, 1), date(2023, 4, 28))

# urls = []

# for day in dates:
#     url = get_by_date(day)
#     urls.append(url)

# print(urls)


