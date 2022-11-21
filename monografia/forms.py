from django import forms
from . models import Monografia
from bootstrap_datepicker_plus.widgets import DatePickerInput

class MonografiaForm(forms.ModelForm):
    class Meta:
        model = Monografia
        fields = "__all__"
        widgets = {
            "data": DatePickerInput(),
        }