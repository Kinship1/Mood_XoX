from django.forms import forms,CharField,EmailField,PasswordInput,ChoiceField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from howsthexp.models import UserRegister,Song
from hashing import *


class RegisterForm(forms.Form):
    Name=CharField(max_length=100,label='Your Name')
    username=CharField(max_length=8,label='Username',help_text='What should we call you at moody')
    Email=EmailField()
    password=CharField(max_length=100,label='password',widget=PasswordInput)
    cnf_pass=CharField(max_length=100,label='Confirm Password',widget=PasswordInput)

    def clean_username(self):
        us=self.cleaned_data['username']
        if(UserRegister.objects.filter(username=us).exists()):
            raise ValidationError(_("that username is already taken"))
        return us


class LoginForm(forms.Form):
    username=CharField(max_length=10,label='Username')
    password=CharField(max_length=12,label='Password',widget=PasswordInput)

    def clean_password(self):
        us=self.cleaned_data['username']
        ps=self.cleaned_data['password']
        if UserRegister.objects.filter(username=us).exists():
            pass
        else:
            raise ValidationError(_("User name not UserRegistered"))
            return us

        actual=UserRegister.objects.get(username=us).password
        if verify_password(actual,ps) is False:
            raise ValidationError(_("Inavlid Password"))
        return ps



class ForgotPassForm(forms.Form):
    email=EmailField()

    def clean_email(self):
        us=self.cleaned_data['email']
        if UserRegister.objects.filter(email=us).exists():
            print(UserRegister.objects.filter(email=us))
            return us
        else:
            raise ValidationError(_("Sorry that email is not registered with us !! Try signup "))
        return us


class ResetPassForm(forms.Form):
    password=CharField(widget=PasswordInput(),max_length=12,label="new password")
    confirm=CharField(widget=PasswordInput(),max_length=12,label="Confirm password")

    def clean_confirm(self):
        pas=self.cleaned_data['password']
        cnf=self.cleaned_data['confirm']

        if len(pas)<6:
            raise ValidationError(_("Minimum 6 characters required"))

        if pas!=cnf:
            raise ValidationError(_("Please reconfirm your password"))
        return pas
