from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


#
# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)


# Widget input - тэга для колличества товара
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int,
                                      label='',
                                      widget=forms.NumberInput(attrs={
                                          'step': 1,
                                          'min': 1,
                                          'max': 20,
                                          'value': 1,
                                          'name': 'quantity',
                                          'title': 'Qty',
                                          'class': 'input-text qty text',
                                          'size': 4,
                                      },
                                      ))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
