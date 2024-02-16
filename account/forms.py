from django import forms 
from account.models import KYC, SENDUSER, RECEIVEUSER, CURRENCY_CONVERTOR
from django.forms import ImageField, FileInput, DateInput

class DateInput(forms.DateInput):
    input_type = 'date'

class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    image = ImageField(widget=FileInput)
    signature = ImageField(widget=FileInput)

    class Meta:
        model = KYC
        fields = [ 'full_name', 'image', 'marrital_status', 'gender', 'identity_type', 'identity_image', 'date_of_birth', 'signature', 'country', 'state', 'city', 'mobile', 'fax']
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder":"Full Name"}),
            "mobile": forms.TextInput(attrs={"placeholder":"Mobile Number"}),
            "fax": forms.TextInput(attrs={"placeholder":"Fax Number"}),
            "country": forms.TextInput(attrs={"placeholder":"Country"}),
            "state": forms.TextInput(attrs={"placeholder":"State"}),
            "city": forms.TextInput(attrs={"placeholder":"City"}),
            'date_of_birth':DateInput
        }

class SENDERForm(forms.ModelForm):
    # identity_image = ImageField(widget=FileInput)
    # image = ImageField(widget=FileInput)
    # signature = ImageField(widget=FileInput)

    class Meta:
        model = SENDUSER
        # fields = [ 'full_name', 'image', 'marrital_status', 'gender', 'identity_type', 'identity_image', 'date_of_birth', 'signature', 'country', 'state', 'city', 'mobile', 'fax']
        fields = ['full_name', 'account_number', 'transaction_type', 'transaction_origin', 'mobile', 'other']
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder":"Full Name"}),
            "mobile": forms.TextInput(attrs={"placeholder":"Your Whatsapp Number"}),
            "account_number": forms.TextInput(attrs={"placeholder":"Account Number"}),
            "other": forms.TextInput(attrs={"placeholder":"other"})
            # "state": forms.TextInput(attrs={"placeholder":"State"}),
            # "city": forms.TextInput(attrs={"placeholder":"City"}),
            # 'date_of_birth':DateInput
        }

class RECEIVERForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    # image = ImageField(widget=FileInput)
    # signature = ImageField(widget=FileInput)

    class Meta:
        model = RECEIVEUSER
        fields = [ 'full_name', 'identity_image', 'account_number', 'transaction_type', 'transaction_origin', 'other']
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder":"Full Name"}),
            "account_number": forms.TextInput(attrs={"placeholder":"Account Number"}),
            "other": forms.TextInput(attrs={"placeholder":"other"})
            # "full_name": forms.TextInput(attrs={"placeholder":"Full Name"}),
            # "mobile": forms.TextInput(attrs={"placeholder":"Mobile Number"}),
            # "fax": forms.TextInput(attrs={"placeholder":"Fax Number"}),
            # "country": forms.TextInput(attrs={"placeholder":"Country"}),
            # "state": forms.TextInput(attrs={"placeholder":"State"}),
            # "city": forms.TextInput(attrs={"placeholder":"City"}),
            # 'date_of_birth':DateInput
        }


class CURRENCY_CONVERTOR_Form(forms.ModelForm):
    # identity_image = ImageField(widget=FileInput)
    # image = ImageField(widget=FileInput)
    # signature = ImageField(widget=FileInput)

    class Meta:
        model = CURRENCY_CONVERTOR
        fields = [ 'full_name', 'amount', 'currency_to', 'currency_from']
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder":"Full Name"}),
            "amount": forms.TextInput(attrs={"placeholder":"Enter amount to convert."}),
            # "result": forms.TextInput(attrs={"placeholder":"Results from conversion"}),
            # "currency_to": forms.TextInput(attrs={"placeholder":"currency_to"}),
            # "currency_from": forms.TextInput(attrs={"placeholder":"currency_from"}),
            # "currency_data": forms.TextInput(attrs={"placeholder":"currency_data"}),
            # "country": forms.TextInput(attrs={"placeholder":"Country"}),
            # "state": forms.TextInput(attrs={"placeholder":"State"}),
            # "city": forms.TextInput(attrs={"placeholder":"City"}),
            # 'date_of_birth':DateInput
        }
