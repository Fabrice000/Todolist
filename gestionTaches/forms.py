from django import forms
from .models import Taches


class tachesForm(forms.ModelForm):
    # finish = forms.BooleanField(label='' ,widget=forms.CheckboxInput(attrs={
    #     "class":"col-lg-3 col-md-3 col-sm-3 form-check-input",
    #     "name":"level"
    # }))
    CATEGORIES_CHOICES = (
        ('Programmation', 'Programmation'),
        ('Travail', 'Travail'),
        ('Sport', 'Sport'),
        ('Personnel', 'Personnel'),
        ('Education', 'Education'),
        ('Divertissement', 'Divertissement'),
        ('Evenement', 'Evenement'),

    )
    PRIORITY_CHOICES = (
        ('low','low'),
        ('normal','normal'),
        ('high','high'),
    )
    

    categories =forms.ChoiceField(label='', choices=CATEGORIES_CHOICES)

    name = forms.CharField(label='', widget=forms.TextInput(attrs=
        {
            "class":"form-control form-control-sm form-control-md",
            "name":"name",
            "placeholder":"Que voulez vous faire?"
        }
    ))
    description = forms.CharField(label='', required=False,widget=forms.TextInput(attrs={
            "class":"form-control form-control-sm form-control-md",
            "name":"name",
            "placeholder":"Description"
    }))
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES,label='')
    class Meta:
        model = Taches
        fields = ('categories','name','description','priority')
