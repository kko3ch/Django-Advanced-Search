from django import forms

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(required=False)
    min_price = forms.DecimalField(min_value=0, required=False)
    max_price = forms.DecimalField(min_value=0, required=False)
