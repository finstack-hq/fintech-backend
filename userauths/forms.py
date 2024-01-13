# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from userauths.models import CustomUser
# from django.forms import ModelForm

# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         # fields = ['username', 'email', 'password1', 'password2']
#         fields = ['first_name', 'last_name', 'email', 'password1', 'password2']



from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import CustomUser

class UserRegisterForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    class Meta:
        model = CustomUser
        # fields = ['username', 'email', 'password1', 'password2']
        fields = ['email', 'password1', 'password2']






