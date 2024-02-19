from django.shortcuts import render, redirect
from account.models import KYC, Account, SENDUSER, RECEIVEUSER, CURRENCY_CONVERTOR
from account.forms import KYCForm, SENDERForm, RECEIVERForm, CURRENCY_CONVERTOR_Form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.forms import CreditCardForm
from core.models import CreditCard, Notification, Transaction
from core.views import currency_data

from django.http import JsonResponse

import requests
import json
import os

       


# @login_required
def account(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You need to submit your kyc")
            return redirect("account:kyc-reg")
        
        account = Account.objects.get(user=request.user)
    else:
        messages.warning(request, "You need to login to access the dashboard")
        return redirect("userauths:sign-in")

    context = {
        "kyc":kyc,
        "account":account,
    }
    return render(request, "account/account.html", context)

@login_required
def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None
    
    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "KYC Form submitted successfully, In review now.")
            return redirect("account:account")
    else:
        form = KYCForm(instance=kyc)
    context = {
        "account": account,
        "form": form,
        "kyc": kyc,
    }
    return render(request, "account/kyc-form.html", context)

@login_required
def sender_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        sent = SENDUSER.objects.get(user=user)
    except:
        sent = None
    
    if request.method == "POST":
        form = SENDERForm(request.POST, request.FILES, instance=sent)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "Sender Form submitted successfully, In review now.")
            return redirect("account:receiver-form")
    else:
        form = SENDERForm(instance=sent)
    context = {
        "account": account,
        "form": form,
        "sent": sent   }
    return render(request, "account/sender-form.html", context)


@login_required
def receiver_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        receive = RECEIVEUSER.objects.get(user=user)
    except:
        receive = None
    
    if request.method == "POST":
        form = RECEIVERForm(request.POST, request.FILES, instance=receive)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "Receiver Form submitted successfully, In review now.")
            return redirect("account:dashboard")
    else:
        form = RECEIVERForm(instance=receive)
    context = {
        "account": account,
        "form": form,
        "receive": receive,
    }
    return render(request, "account/receiver-form.html", context)


@login_required
def convert_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        convert = CURRENCY_CONVERTOR.objects.get(user=user)
    except:
        convert = None
    
    if request.method == "POST":
        form = CURRENCY_CONVERTOR_Form(request.POST, request.FILES, instance=convert)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "Convertion Form submitted successfully, In review now.")
            # return redirect("account:account")
            return redirect("account:sender-form")
    else:
        form = CURRENCY_CONVERTOR_Form(instance=convert)
    context = {
        "account": account,
        "form": form,
        "convert": convert   }
    return render(request, "account/convert-reg.html", context)



def dashboard(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You need to submit your kyc")
            return redirect("account:kyc-reg")
        
        recent_transfer = Transaction.objects.filter(sender=request.user, transaction_type="transfer", status="completed").order_by("-id")[:1]
        recent_recieved_transfer = Transaction.objects.filter(reciever=request.user, transaction_type="transfer").order_by("-id")[:1]


        sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="transfer").order_by("-id")
        reciever_transaction = Transaction.objects.filter(reciever=request.user, transaction_type="transfer").order_by("-id")

        request_sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="request")
        request_reciever_transaction = Transaction.objects.filter(reciever=request.user, transaction_type="request")
        
        
        account = Account.objects.get(user=request.user)
        credit_card = CreditCard.objects.filter(user=request.user).order_by("-id")

        if request.method == "POST":
            form = CreditCardForm(request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user 
                new_form.save()
                
                Notification.objects.create(
                    user=request.user,
                    notification_type="Added Credit Card"
                )
                
                card_id = new_form.card_id
                messages.success(request, "Card Added Successfully.")
                return redirect("account:dashboard")
        else:
            form = CreditCardForm()

    else:
        messages.warning(request, "You need to login to access the dashboard")
        return redirect("userauths:sign-in")

    context = {
        "kyc":kyc,
        "account":account,
        "form":form,
        "credit_card":credit_card,
        "sender_transaction":sender_transaction,
        "reciever_transaction":reciever_transaction,

        'request_sender_transaction':request_sender_transaction,
        'request_reciever_transaction':request_reciever_transaction,
        'recent_transfer':recent_transfer,
        'recent_recieved_transfer':recent_recieved_transfer,
    }
    return render(request, "account/dashboard.html", context)



# def SupportView(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#     if request.user.is_authenticated:
#         messages.warning(request, "You are already logged In")
#         return redirect("account:support")
        
#     return render(request, "account/support.html")

@login_required
def support_view(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        convert = CURRENCY_CONVERTOR.objects.get(user=user)
    except:
        convert = None
    
    if request.method == "POST":
        form = CURRENCY_CONVERTOR_Form(request.POST, request.FILES, instance=convert)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "Convertion Form submitted successfully, In review now.")
            # return redirect("account:account")
            return redirect("account:sender-form")
    else:
        form = CURRENCY_CONVERTOR_Form(instance=convert)
    context = {
        "account": account,
        "form": form,
        "convert": convert   }
    return render(request, "account/support.html", context)




@login_required
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
    # return render(request, "account/kyc-reg/money-exchange.html")
