from .models import CustomUser
from django import forms
  
class Register(forms.ModelForm):
    password = forms.CharField(max_length=12,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    confirm_password = forms.CharField(max_length=12,widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    class Meta():
        model = CustomUser
        fields = ['username','email','password']
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Full Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Email'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password didn\'t matched.')
        return cleaned_data