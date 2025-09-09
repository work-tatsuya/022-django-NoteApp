from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 初期表示での help_text を全て消す
        for fieldname in self.fields:
            self.fields[fieldname].help_text = ""
