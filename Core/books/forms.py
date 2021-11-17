from django import forms
from .models import Book


class AddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author', 'coverpage')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'coverpage': forms.FileInput(attrs={'class': 'form-control'}),
        }