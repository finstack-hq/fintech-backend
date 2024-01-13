from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.account, name="account"),
    path("kyc-reg/", views.kyc_registration, name="kyc-reg"),

     path('kyc-reg/money-exchange.html', views.currency_data, name='money-exchange'),
]



