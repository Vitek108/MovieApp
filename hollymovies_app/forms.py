from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import ModelChoiceField
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from hollymovies_app.models import Movie, Actor

def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized.")


class CapitalizedCharfield(forms.CharField):
    def validate(self, value):
        if value[0].islower():
            raise ValidationError("Value must be capitalized.")

    def clean(self, value): #string transformuje tak, jak chceme (přidá velké písmeno)
        return value.capitalized()


class ContactForm(forms.Form):
    name = CapitalizedCharfield()
    email = forms.EmailField()
    subject = forms.CharField(required=False, validators=[capitalized_validator])
    description = forms.CharField(widget=forms.Textarea) #není možnost použít nějaký textfield, je třeba použít widget = jak se forma bude zobrazovat


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["name", "description", "genres"]


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ["name", "movies"]


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]