
#builtin form definition

from django import forms
from book.models import book

class bookform(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'