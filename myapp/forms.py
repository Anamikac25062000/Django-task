from django import forms
from .models import UploadFile, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class RegularFileUploadForm(forms.Form):
    title = forms.CharField(max_length=255)
    doc = forms.FileField()


class ModelFileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['title', 'doc']