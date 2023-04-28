from django import forms

class OrderForm(forms.Form):
    CHOICES = [
        ('Source', 'Source'),
        ('Title', 'Title')
    ]
    key = forms.ChoiceField(choices=CHOICES)