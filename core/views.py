from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#      return render(request, "core/index.html")

# def contact(request):
#     return render(request, "core/contact.html")

# def about(request):
#     return render(request, "core/about.html")

from django.contrib import admin
from core.models import Transaction, CreditCard, Notification

# from django.shortcuts import render
import requests
import json
import os

def currency_data():
    """ All countries currency data"""
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'currencies.json')
    with open(file_path, "r") as f:
        currency_data = json.loads(f.read())
    return currency_data

def money_exchange_view(request):
      if request.method == "POST":

        # Get data from the html form
        amount = float(request.POST.get('amount'))
        currency_from = request.POST.get("currency_from")
        currency_to = request.POST.get("currency_to")

        # Get currency exchange rates 
        url = f"https://paylio.wiredmartians.com/api/v1/rates/{currency_from}"
        response = requests.get(url).json()
        # Converter
        if response:
            # Get currency exchange of the target
            ex_target =  response["rates"][currency_to]

            # Mltiply by the amount
            result = ex_target * amount

            # Set 2 decimal places
            result = "{:.2f}".format(result)
            amount = "{:.2f}".format(amount)
            context = {
            "result":result, 
            "amount":amount,
            "currency_to":currency_to, 
            "currency_from":currency_from,
            "currency_data":currency_data()
            }

            # return render(request, "index.html", context)
            return render(request, "account/kyc-reg/money-exchange.html", context)
    
    # return render(request, "core/index.html", {"currency_data":currency_data()})
      return render(request, "account/kyc-reg/money-exchange.html", {"currency_data":currency_data()})

# def index(request):
#      return render(request, "core/index.html")

def index(request):
    
    if request.method == "POST":

        # Get data from the html form
        amount = float(request.POST.get('amount'))
        currency_from = request.POST.get("currency_from")
        currency_to = request.POST.get("currency_to")

        # Get currency exchange rates 
        url = f"https://paylio.wiredmartians.com/api/v1/rates/{currency_from}"
        response = requests.get(url).json()
        # Converter
        if response:
            # Get currency exchange of the target
            ex_target =  response["rates"][currency_to]

            # Mltiply by the amount
            result = ex_target * amount

            # Set 2 decimal places
            result = "{:.2f}".format(result)
            amount = "{:.2f}".format(amount)
            context = {
            "result":result, 
            "amount":amount,
            "currency_to":currency_to, 
            "currency_from":currency_from,
            "currency_data":currency_data()
            }

            # return render(request, "index.html", context)
            return render(request, "core/index.html", context)
        
   
    return render(request, "core/index.html", {"currency_data":currency_data()})

class TransactionAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'status', 'transaction_type']
    list_display = ['user', 'amount', 'status', 'transaction_type', 'reciever', 'sender']


class CreditCardAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'card_type']
    list_display = ['user', 'amount', 'card_type']
    

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'notification_type', 'amount' ,'date']

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(Notification, NotificationAdmin)
