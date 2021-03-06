from django import forms
from django.forms import ModelForm
from .models import Activity, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class SignUpForm(forms.Form):
#     username = forms.CharField(help_text="Enter a Username")
#     email = forms.EmailField(help_text="Enter Email")
#     password = forms.CharField(help_text="Enter Password", widget=forms.PasswordInput)


# class CreateActivityForm(forms.Form):
#     title = forms.CharField(help_text="Enter activity title")
#     description = forms.CharField(help_text="Enter activity description", widget=forms.Textarea)
#     # todo - address lookup
#     address = forms.CharField(help_text="Enter activity address")
#     # todo - date time validation
#     date = forms.DateField(help_text="Enter Date (dd/mm/yy)", required=False)
#     # tags - are they going to be an array of tags or a series of boolean values? Currently thinking an array,
#     # but need to look into python a little more
#     # todo - image upload


class CreateActivity(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {'tags': forms.CheckboxSelectMultiple}


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter your email')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class ProfileFormAvatar(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


class ProfileFormPostcode(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['postcode', 'radius']


class SaveFavourite(forms.Form):
    id_id = forms.CharField()