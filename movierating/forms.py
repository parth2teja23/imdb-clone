from django import forms
from .models import Rating, Comment

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'w-full px-3 py-2 rounded'})
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full p-2 bg-neutral-900 text-white border border-neutral-700 rounded',
                'placeholder': 'Write your comment...'
            }),
        }

