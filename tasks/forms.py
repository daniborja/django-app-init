from django import forms

from .models import Task


# ### Este form Solo crea los   Inputs

class TaskForm(forms.ModelForm): # inheritance ModelForm
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        # ## custom styles in inputs
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'important': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
        }

