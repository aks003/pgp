from django import forms
from django.forms import Form, ModelForm, fields
from main.models import deliverables_db

class DeliverablesForm(ModelForm):
    class Meta:
        model = deliverables_db
        fields= '__all__'

    def save(self, commit=True):
        deliverable = super().save(commit=False)
        if commit:
            deliverable.save()
        return deliverable
