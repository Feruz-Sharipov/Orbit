from .models import Contect
from django import forms

class Contect(forms.ModelForm):
    class Meta:
        model = Contect
        fields = "__all__"