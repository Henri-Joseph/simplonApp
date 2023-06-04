from django import forms
from visiteCandidats.models import Candidats

class CandidatFrom(forms.ModelForm):
    class Meta:
        model=Candidats
        fields = "__all__"
