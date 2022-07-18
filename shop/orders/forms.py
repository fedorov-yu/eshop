from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'post_code', 'city', 'address', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'wpcf7'}),
            'last_name': forms.TextInput(attrs={'class': 'wpcf7'}),
            'email': forms.EmailInput(attrs={'class': 'wpcf7'}),
            'phone': forms.TextInput(attrs={'class': 'wpcf7'}),
            'post_code': forms.TextInput(attrs={'class': 'wpcf7'}),
            'city': forms.TextInput(attrs={'class': 'wpcf7'}),
            'address': forms.TextInput(attrs={'class': 'wpcf7'}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'wpcf7'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'wpcf7',}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'wpcf7', 'rows': 3}))