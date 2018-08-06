from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="What's Your Name?", max_length=255)
    email = forms.EmailField(label="What's your email address?")
    subject = forms.CharField(label="What do you want to talk about?", max_length=255)
    body = forms.Textarea()
