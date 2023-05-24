from django import forms
from captcha.fields import CaptchaField
from .models import Subscriber


# class SubscribePostForm(forms.Form):
#     first_name = forms.CharField(max_length=25)
#     last_name = forms.CharField(max_length=25)
#     email = forms.EmailField()
#     phone = forms.CharField(max_length=12, required=False)
#     city = forms.CharField(max_length=100, required=False)
#     state = forms.CharField(max_length=20, required=False)
#     zip = forms.CharField(max_length=12, required=False)
#     capthca = CaptchaField()
class SubscribePostForm(forms.ModelForm):
    # capthca = CaptchaField()
    class Meta:
        model = Subscriber
        fields = ['first_name', 'last_name', 'email',
                  'phone', 'city','state', 'zip']
        widgets = {
            'first_name' : forms.TextInput(attrs= {'placeholder': 'First Name'}),
            'last_name' : forms.TextInput(attrs= {'placeholder': 'Last Name'}),
            'email' : forms.TextInput(attrs= {'placeholder': 'Email Address'}),
            'phone' : forms.TextInput(attrs= {'placeholder': 'Phone'}),
            'city' : forms.TextInput(attrs= {'placeholder': 'City'}),
            'state' : forms.TextInput(attrs= {'placeholder': 'State'}),
            'zip' : forms.TextInput(attrs= {'placeholder': 'Zip'}),

        }
        
    def clean_email(self):
        data = self.cleaned_data['email']
        if Subscriber.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data
    