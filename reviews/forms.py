from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Create form based on Review model"""

    class Meta:
        model = Review
        exclude = ('user', 'image_url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'One word description',
            'body': 'Go on, give us some more detail...',
        }

        for field in self.fields:
            if field in placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
