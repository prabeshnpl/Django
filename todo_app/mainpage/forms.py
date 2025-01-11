from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    class Meta():

        model = Tasks
        fields = ['task']
        widgets = {
            'task':forms.TextInput(attrs={
                'class':'input_bar',
                'id':'input_bar',
                'placeholder':'What needs to be done!'
                })
        }

class UpdateTaskForm(forms.ModelForm):
    class Meta():
        model = Tasks
        fields = ['task']
        widgets = {
            'task':forms.TextInput(attrs={
                'class':'update_task-input',
                'placeholder':'Update'
                })
        }