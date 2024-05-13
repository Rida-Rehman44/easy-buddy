from django.forms import inlineformset_factory, ModelForm, TextInput

from shopping_checklist.models import ShoppingChecklist, ShoppingItem


class ChecklistForm(ModelForm):
    class Meta:
        model = ShoppingChecklist
        fields = ['name', 'group']  # Include any other fields you want to edit


class ShoppingItemForm(ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['quantity', 'item_name', 'bought']
        widgets = {
            'quantity': TextInput(attrs={'placeholder': 'Quantity', 'class': 'form-control'}),
            'item_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Type to search...',
                                          'list': 'itemList'}),
        }


ShoppingItemFormSet = inlineformset_factory(ShoppingChecklist, ShoppingItem, form=ShoppingItemForm, extra=1)