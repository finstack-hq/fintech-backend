from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.account, name="account"),
    path("kyc-reg/", views.kyc_registration, name="kyc-reg"),
    path("sender-form/", views.sender_registration, name="sender-form"),
    path("receiver-form/", views.receiver_registration, name="receiver-form"),
    path("convert-reg/", views.convert_registration, name="convert-reg"),
    path("support/", views.support_view, name="support"),
    path('account/kyc-reg/money-exchange/', views.money_exchange_view, name='money-exchange'),
]



