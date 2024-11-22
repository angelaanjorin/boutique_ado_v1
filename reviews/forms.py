from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for Review Model - Add / Edit
    """

    class Meta:
        model = Review
        fields = ('review', 'rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets placeholder values
        placeholders = {
            'review': 'Your Review',
            'rating': 0
        }