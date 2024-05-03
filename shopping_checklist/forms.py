from django.forms import inlineformset_factory, ModelForm, TextInput

from shopping_checklist.models import ShoppingChecklist, ShoppingItem


class ShoppingItemForm(ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['quantity', 'item_name']
        widgets = {
            'quantity': TextInput(attrs={'placeholder': 'Quantity', 'class': 'form-control'}),
            'item_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Type to search...',
                                          'list': 'itemList'}),
        }


ShoppingItemFormSet = inlineformset_factory(ShoppingChecklist, ShoppingItem, form=ShoppingItemForm, extra=1)
