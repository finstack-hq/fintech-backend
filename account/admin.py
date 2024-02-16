from django.contrib import admin
from account.models import Account, KYC, SENDUSER, RECEIVEUSER, CURRENCY_CONVERTOR
# from userauths.models import User
from userauths.models import CustomUser
from import_export.admin import ImportExportModelAdmin
# from .admin import ImportExportModelAdmin

class AccountAdminModel(ImportExportModelAdmin):
    list_editable = ['account_status', 'account_balance', 'kyc_submitted', 'kyc_confirmed'] 
    list_display = ['user', 'account_number' ,'account_status', 'account_balance', 'kyc_submitted', 'kyc_confirmed'] 
    list_filter = ['account_status']

class KYCAdmin(ImportExportModelAdmin):
    search_fields = ["full_name"]
    list_display = ['user', 'full_name', 'gender', 'identity_type', 'date_of_birth'] 

class SENDERAdmin(ImportExportModelAdmin):
    search_fields = ["full_name"]
    list_display = ['user', 'full_name', 'transaction_type', 'transaction_origin', 'mobile', 'other'] 

class RECEIVERAdmin(ImportExportModelAdmin):
    search_fields = ["full_name"]
    list_display = ['user', 'full_name', 'transaction_type', 'transaction_origin', 'other'] 

class CONVERTORAdmin(ImportExportModelAdmin):
    search_fields = ["full_name"]
    list_display = ['user', 'full_name',  'amount', 'currency_from', 'currency_to'] 


admin.site.register(Account, AccountAdminModel)
admin.site.register(KYC, KYCAdmin)
admin.site.register(SENDUSER, SENDERAdmin)
admin.site.register(RECEIVEUSER, RECEIVERAdmin)
admin.site.register(CURRENCY_CONVERTOR, CONVERTORAdmin)





