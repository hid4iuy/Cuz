from django import forms
from.models import CANDIDATE

class CandidateForm(forms.ModelForm):
    class Meta:
        model = CANDIDATE
        fields = ['name','nameKN','sex','birthYMD','partyCd','mail','link']
    # name = forms.CharField(label='name')
    # nameKN = forms.CharField(label='C')
    # SEX_CHOICES=[
    #     (0, '男性'),
    #     (1, '女性'),
    #     (2, 'other')
    #     ]
    # sex = forms.ChoiceField(label='sex',choices=SEX_CHOICES)
    # birthYMD = forms.DateField(label='birthYMD')
    # partyCd = forms.CharField(label='partyCd')
    # mail = forms.EmailField(label='mail')
    # link = forms.CharField(label='リンク')
