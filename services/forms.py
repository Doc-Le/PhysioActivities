
from django import forms
from .models import Service, Clinician, ServiceDate, ServicePage, ServiceTime

class ServiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label="Service *", required=True)
    clinician = forms.ModelChoiceField(queryset=Clinician.objects.all(), label="Clinician *", required=True)
    date = forms.ModelChoiceField(queryset=ServiceDate.objects.all(), label="Date *", required=True)
    time = forms.ModelChoiceField(queryset=ServiceTime.objects.all(), label="Time *", required=True)
    
    class Meta:
        model = ServicePage
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
