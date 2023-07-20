from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Record, Deal

# Form for contacts
class AddRecordForm(forms.ModelForm):
    LIFE_CYCLE_CHOICES = (
        ('Lead', 'Lead'),
        ('Subcriber', 'Subcriber'),
        ('Customer', 'Customer'),
    )
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    life_cycle_stage = forms.ChoiceField(choices=LIFE_CYCLE_CHOICES, required=True, widget=forms.widgets.Select(attrs={"placeholder":"Lifecycle Stage", "class":"form-control"}), label="")
    note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Note", "class": "form-control", "rows": 6}),  # Set rows attribute to determine the number of visible lines
        label=""
    )

    class Meta:
        model = Record
        exclude = ("user",)

# Form for deals
class AddDealForm(forms.ModelForm):
    deal_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Deal name", "class":"form-control"}), label="")
    pipeline = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Pipeline", "class":"form-control"}), label="")
    deal_owner = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Deal owner", "class":"form-control"}), label="")
    close_day = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"Close day", "class":"form-control", 'type': 'date'}), label="")
    amount = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount", "class":"form-control"}), label="")
    
    class Meta:
        model = Deal
        exclude = ("user",)

# form for notes in contacts
class AddNoteForm(forms.ModelForm):
    note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Note", "class": "form-control", "rows": 6}),  # Set rows attribute to determine the number of visible lines
        label=""
    )

    class Meta:
        model = Record
        fields = ['note']
        exclude = ("user",)