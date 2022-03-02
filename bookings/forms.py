from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('service', 'clinician', 'datetime',
                  'total',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'service': 'Select Service',
            'clinician': 'Select Clinician',
            'datetime': 'Select Date and Time',
            'total': 'Total',
        }

        self.fields['service'].widget.attrs['autofocus'] = True
        self.fields['total'].widget.attrs['readonly'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            if self.fields[field].required:
                label = f'{placeholder} *'
            else:
                label = placeholder
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = label
