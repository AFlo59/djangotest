from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CryptoApiForm
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

@login_required
def api_page(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.getenv('API_KEY'),
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = response.json()
        print(data)  # Print the data for debugging purposes

        # Pass the data to the template context
        context = {'form': CryptoApiForm(), 'data': data}
        return render(request, "main/api_page.html", context=context)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

        # If an error occurs, render the page with an empty data context
        return render(request, "main/api_page.html", context={'form': CryptoApiForm()})

def home_page(request):
    return render(request, 'main/home_page.html')

def about_page(request):
    return render(request, 'main/about_page.html')

def contact_page(request, test):
    context = {'test': test}
    return render(request, 'main/contact_page.html', context=context)

@login_required
def special_page(request):
    return render(request, "main/special_page.html")

