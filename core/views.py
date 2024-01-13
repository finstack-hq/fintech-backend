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

def index(request):
     return render(request, "core/index.html")

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
