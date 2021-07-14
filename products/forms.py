from django import forms


class ProductForm(forms.Form):
    name = forms.CharField()
    desc = forms.CharField()
    price = forms.DecimalField()
