from django.forms import ModelForm
from django.forms import PasswordInput
from .models import User,Task,Comment
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': PasswordInput(),
        }

class TaskForm(ModelForm):
    class Meta : 
        model = Task
        fields = '__all__'
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class ComentForm(ModelForm):
    class Meta :
        model = Comment
        fields = '__all__'