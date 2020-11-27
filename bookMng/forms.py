from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Request
from .models import Review
from .models import UserCart

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = [
            'name',
            'web',
        ]

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'rating',
            'review',
        ]

class SearchForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
        ]
        # widget = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Search'})
        # }