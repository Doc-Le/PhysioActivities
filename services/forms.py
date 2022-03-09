
from django import forms

from .models import Service

class ServiceForm(forms.ModelForm):
    service = forms.ChoiceField(choices=[], label="Service *", required=True)
    clinician = forms.ChoiceField(choices=[], label="Clinician *", required=True)
    date = forms.ChoiceField(choices=[], label="Date *", required=True)
    time = forms.ChoiceField(choices=[], label="Time *", required=True)
    
    class Meta:
        model = Service
        fields = ('service', 'clinician', 'date', 'time',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'service': 'Choose Service ...',
            'clinician': 'Choose Clinician ...',
            'date': 'Choose Appointment Date ...',
            'time': 'Choose Appointment Time ...',
        }

        self.fields['service'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'form-control'
