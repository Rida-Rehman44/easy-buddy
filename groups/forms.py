from django.forms import inlineformset_factory, ModelForm, TextInput
from shopping_checklist.models import ShoppingChecklist, ShoppingItem
from django import forms
from .models import BulletinBoardMessage

class BulletinBoardMessageForm(forms.ModelForm):
    class Meta:
        model = BulletinBoardMessage
        fields = ['content', 'image', 'video']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your message here...'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')

        # Check if either image or video is provided
        if not image and not video:
            raise forms.ValidationError("You must provide either an image or a video.")
        return cleaned_data


class ChecklistForm(ModelForm):
    class Meta:
        model = ShoppingChecklist
        fields = ['name', 'event']  # Include any other fields you want to edit


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