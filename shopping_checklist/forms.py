from django import forms
from django.forms import ModelForm

from shopping_checklist.models import ShoppingChecklist


class CreateForm(ModelForm):
    # fields we want to include and customize in our form
    quantity = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Quantity',
                                                               'class': 'form-control',
                                                               }))
    item_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={
                                                              'class': 'form-control',
                                                              'list':'itemList',
                                                              'placeholder':"Type to search...",
                                                              }))

    class Meta:
        model = ShoppingChecklist
        fields = ['quantity', 'item_name']