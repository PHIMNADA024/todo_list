from django import forms
from ..models import Todo


class TodoForm(forms.ModelForm):
    """Form for creating and updating Todo items."""
    class Meta:
        model = Todo
        fields = ['title', 'status', 'photo']
