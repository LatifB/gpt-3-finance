from django import forms

commodity_choices = (
    ("SILVER", "SILVER"),
    ("GOLD", "GOLD"),
)

class CommoditiesForm(forms.Form):
    commodity_field = forms.MultipleChoiceField(choices = commodity_choices)