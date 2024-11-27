from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Address


class UserRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    birthday = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'phone_number', 'birthday', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'        
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'zip_code']
        labels = {
            'street': 'خیابان',
            'city': 'شهر',
            'state': 'استان',
            'zip_code': 'کد پستی',
        }

