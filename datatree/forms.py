from django import forms
from datatree.models import Relation
from django.forms import formset_factory

class AppendPeople(forms.Form):
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name",
        })
    )


class AppendChild(AppendPeople):
    pass


class TakeIdForm(forms.Form):
    child_id = forms.IntegerField(
        min_value=1,
        )
    parent_id = forms.IntegerField(
        min_value=1,
        )
class DeleteForm(forms.Form):
    child_id = forms.IntegerField(
        min_value=1,
        )