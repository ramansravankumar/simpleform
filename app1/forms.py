from django import forms
from .models import Person
import re
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        dob_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        if not dob_pattern.match(str(dob)):
            raise forms.ValidationError("Please enter a valid date of birth in the format yyyy-mm-dd.")
        return dob