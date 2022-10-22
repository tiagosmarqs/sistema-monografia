from django import forms
from . models import Coorientador

class CoorientadorForm(forms.ModelForm):
    class Meta:
        model = Coorientador
        fields = "__all__"