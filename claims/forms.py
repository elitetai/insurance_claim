from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Claim
import datetime

TYPE_OF_LOSS = [
    ('1', 'Own Damage'), 
    ('2', 'Knock for Knock'), 
    ('3', 'Windscreen Damage'), 
    ('4', 'Theft'),
]
TRUE_FALSE_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
]

YEAR_CHOICES_LIST = []
YEAR_CHOICES_TUPLES = []
for year in range(1990, (datetime.datetime.now().year)):
    YEAR_CHOICES_LIST.append(year)
    YEAR_CHOICES_TUPLES.append((year,year))

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class ClaimForm(forms.ModelForm):
    vehicle_manufacture_year = forms.ChoiceField(choices=YEAR_CHOICES_TUPLES)
    date_and_time_of_accident = forms.DateTimeField(widget=DateInput)
    type_of_loss = forms.ChoiceField(choices=TYPE_OF_LOSS)
    police_report_lodged = forms.ChoiceField(widget=forms.RadioSelect, choices=TRUE_FALSE_CHOICES)
    anybody_injured = forms.ChoiceField(widget=forms.RadioSelect, choices=TRUE_FALSE_CHOICES, label='Anybody injured during the accident?')
    document_in_pdf_format = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))

    class Meta:
        model = Claim
        exclude = ['claim_approved','created_at', 'created_by']