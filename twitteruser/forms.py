from django import forms
from twitteruser.models import CustomUser


class ChangePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_pic']
