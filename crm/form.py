from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200, required=True)
    phone = forms.CharField(label='Phone', max_length=200, required=True,
                            widget=forms.TextInput(attrs={'class': 'my_form', 'id': 'myFormId'}))
