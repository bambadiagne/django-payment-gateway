from django import forms
from django.forms.fields import CharField
from  django.core.validators import RegexValidator
from .models import User

# Create your models here.


class UserForm(forms.ModelForm):
    password = CharField(
    max_length=128,
    required=True,
    validators=[
        RegexValidator(
            regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9]{6,}$',
            message='Format de mot de passe incorrect',
            code='invalid_format'
        ),
    ]
)
    class Meta:
        model=User
        fields=["first_name","last_name","email","password"]
