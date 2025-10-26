from django import forms


# Форма для добавления в корзину
class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=20, initial=1,
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
