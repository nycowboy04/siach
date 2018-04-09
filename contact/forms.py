from django import forms

class ContactForm(forms.Form):
    first_name=forms.CharField(max_length=200, required=True)
    last_name=forms.CharField(max_length=200, required=True)
    from_email=forms.EmailField(required=True)
    subject=forms.CharField(max_length=200, required=True)
    message=forms.CharField(widget=forms.Textarea, required=True)
