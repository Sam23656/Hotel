from django import forms

from Hotel_Admin.models import Service


class ReservationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField()
    email = forms.EmailField()
    person_count = forms.IntegerField()
    start_time = forms.DateField(widget=forms.SelectDateWidget)
    end_time = forms.DateField(widget=forms.SelectDateWidget)

    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

