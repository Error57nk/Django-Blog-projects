from django import forms


class BioForm(forms.ModelForm):
    name = forms.CharField(
        label="Full Name:",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
