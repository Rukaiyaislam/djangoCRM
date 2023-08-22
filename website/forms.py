from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Widget
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email-address'}))
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}), max_length=20 )
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}), max_length=20)
    password1 = forms.CharField(label="password",widget=forms.TextInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="password again",widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
       model = User
       fields = ('username','first_name','last_name','email','password1','password2')
   

    def __init__(self, *args, **kwargs):
       super(SignUpForm, self).__init__(*args, **kwargs)

       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['username'].widget.attrs['placeholder'] = 'User Name'
       self.fields['username'].label = ''
       self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

       self.fields['password1'].widget.attrs['class'] = 'form-control'
       self.fields['password1'].widget.attrs['placeholder'] = 'Password'
       self.fields['password1'].label = ''
       self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

       self.fields['password2'].widget.attrs['class'] = 'form-control'
       self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
       self.fields['password2'].label = ''
       self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

#Add record class
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'First name'}), max_length=20, label="" )
    last_name = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Last name'}), max_length=20, label="")
    email = forms.EmailField(required=False,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Email-address'}),label="")
    address = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Address'}),label="")
    phone = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Phone'}), label="")
    city = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'City'}), label="")
    zipcode = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}), label="")
    state = forms.CharField(required=False,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'State'}), label="")
    

    class Meta:
        model = Record
        exclude = ('user',)

    
   
        