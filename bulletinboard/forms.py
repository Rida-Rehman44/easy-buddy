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
