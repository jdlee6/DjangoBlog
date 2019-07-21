from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # create email field
    # takes an argument called required which would be set equal to a Boolean (True or False)
    # by default, required is set to True
    email = forms.EmailField()

    # gives us a nested namespace for configurations and keeps the configurations in one place
    # within the configuration, we're saying that the model that will be affected is the User model (for example if we do a form.save() it will save it to this user model)
    # the fields that we have in the list are the fields that we want in the form and in what order
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']