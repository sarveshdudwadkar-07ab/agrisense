from django import forms
from .models import ChatMessage


class ChatForm(forms.ModelForm):

    class Meta:
        model = ChatMessage
        fields = ['question', 'image']

        widgets = {
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ask your farming question...',
                'rows': 3
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }