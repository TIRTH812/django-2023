from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User

class ManagerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'age', 'salary')

    @transaction.atomic
    def save(self):
        # print('enter')
        user = super().save(commit=False)
        user.is_manager1 = True
        user.save()
        # print('exit')
        return user   
    
class DeveloperRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'age', 'salary')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_devleopr = True
        user.save()
        return user