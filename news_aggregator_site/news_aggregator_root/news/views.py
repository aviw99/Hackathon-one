from django.shortcuts import render
from .api_funcs import get_by_date, generate_dates, extract_data, order_by
from datetime import date, timedelta
from django.http import HttpResponse
from .forms import OrderForm

# Create your views here.

def yesterday_news(request) -> HttpResponse:
    
    today = date.today()
    yesterday = today - timedelta(days=1)
    url = get_by_date(yesterday)
    news_data = extract_data(url)
    
    if request.method == 'POST':
        form_clicked = OrderForm(request.POST)
        if form_clicked.is_valid():
            order_key = form_clicked.cleaned_data['key']
            news_data = order_by(news_data, order_key)

    
    order_form = OrderForm()
    context = {'articles': news_data, 'form': order_form} 
    
    return render(request, 'yesterday_news.html', context)


