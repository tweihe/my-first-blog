from django import forms

from .models import Essay

#class EssayMaker(forms.ModelForm):

#    class Meta:
#        model = Essay
#        fields = ('length', 'complexity',)

class EssayMaker(forms.Form):
    length = forms.IntegerField()
    complexity = forms.IntegerField()
