from django.contrib.auth import forms
from .models import User

class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "picture", "password1", "password2")
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user