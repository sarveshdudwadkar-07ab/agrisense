from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['rating', 'message']

        widgets = {
            'rating': forms.Select(choices=[
                (5, "⭐⭐⭐⭐⭐ Excellent"),
                (4, "⭐⭐⭐⭐ Good"),
                (3, "⭐⭐⭐ Average"),
                (2, "⭐⭐ Poor"),
                (1, "⭐ Bad")
            ]),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your experience using AgriSense...'
            })
        }