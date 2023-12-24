from django.forms import ModelForm

from .models import Task


# ### Este form Solo crea los   Inputs

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']

