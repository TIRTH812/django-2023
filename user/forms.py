from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class ManagerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager1 = True
        user.save()
        return user   
    
class DeveloperRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_devleopr = True
        user.save()
        return user