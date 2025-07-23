
from typing import Any
from django import forms
# from django.forms.widgets import _OptAttrs
from .models import Share

class CustomClearableFile(forms.widgets.ClearableFileInput) :
    template_name = 'widgets/clearbleFileInput.html'

    def get_context(self, name: str, value: Any, attrs: dict[str, Any] | None) -> dict[str, Any]:
        
        context = super().get_context(name, value, attrs)
        return context

class ShareForm(forms.ModelForm) :
    class Meta :
        model = Share 
        fields = ['title','share_content','cover_image']
        widgets = {
            'title': forms.Textarea(attrs={
                'class': "text-input  bg-green-100 outline-none p-2 border border-transparent hover:border-green-500",
                'required': True 
                }),
            'cover_image' : CustomClearableFile(attrs={
                'class': "file-input",
                'required': False 
                }),
            'share_content': forms.Textarea(attrs={
                'class': "text-input bg-green-100 outline-none p-2 border border-transparent hover:border-green-500",
                'required': True 
                }),
        }