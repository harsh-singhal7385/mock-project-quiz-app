from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields =['question','option_a','option_b','option_c','option_d','marks','answer']
        options = [(option, option) for option in ['a','b','c','d']]
        widgets = {
            'question':forms.TextInput(attrs={'class':'form-control'}),
            'option_a':forms.TextInput(attrs={'class':'form-control'}),
            'option_b':forms.TextInput(attrs={'class':'form-control'}),
            'option_c':forms.TextInput(attrs={'class':'form-control'}),
            'option_d':forms.TextInput(attrs={'class':'form-control'}),
            'marks':forms.NumberInput(attrs={'class':'form-control'}),
            'answer':forms.Select(attrs={'class':'form-control'}, choices=options),
        }





class QuizForm(forms.ModelForm):
    class Meta:
        model = AddQuiz
        fields = ['subject_name', 'instructor_name','category','quiz_time']

        widgets = {
            'subject_name':forms.TextInput(attrs={'class':'form-control'}),
            'instructor_name':forms.TextInput(attrs={'class':'form-control'}),
            'quiz_time':forms.NumberInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
        }
