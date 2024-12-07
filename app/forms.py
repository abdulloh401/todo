from django import forms
from app.models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control'}),
        }
