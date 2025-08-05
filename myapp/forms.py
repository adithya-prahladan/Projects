from django import forms
from django.contrib.auth.models import User  #User is build-in
from django.contrib.auth.forms import UserCreationForm 
from .models import Student

class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
       # fields = ['name','email','course']  or  fields = '__all__'
       
       
class RegisterForm(UserCreationForm): # the class name RegisterForm is not a build-in one
    email = forms.EmailField(required=True) #  'required' for validation
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']