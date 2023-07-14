from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for the contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject of contacting us',
            'message': 'Your Message',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'message':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'   
            self.fields[field].label = False