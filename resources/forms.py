from .models import Suggestion
from django import forms


# Suggestion URLField
suggestion_url = forms.URLField(
    label="Include URL for your Suggestion",
    widget = forms.URLInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Please add your link'
        }
    )
)
