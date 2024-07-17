# transformers/forms.py

from django import forms
from .models import Transformer

class TransformerForm(forms.ModelForm):
    class Meta:
        model = Transformer
        fields = ['name', 'voltage', 'location', 'manufacturer', 'operation_year', 'image_url']
        # forms.py

class SerialNumberForm(forms.Form):
    serial_number = forms.CharField(label='Serial Number', max_length=100)

class FileUploadForm(forms.Form):
    file = forms.FileField()
# class UploadFileForm(forms.Form):
#     file = forms.FileField()


