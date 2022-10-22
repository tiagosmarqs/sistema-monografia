from django import forms
from . models import Orientador

class OrientadorForm(forms.ModelForm):
    class Meta:
        model = Orientador
        fields = "__all__"