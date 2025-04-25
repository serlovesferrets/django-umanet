from django import forms

from contatti.models import Contact


class ContattoForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    contents = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "testo"},))

    class Meta:
        model = Contact
        fields = "__all__"
