from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="What's Your Name?",
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "Your name here"
        })
    )

    email = forms.EmailField(
        label="What's your email address?",
        widget=forms.TextInput(attrs={
            "placeholder": "Your email address here"
        })
    )

    subject = forms.CharField(
        label="What do you want to talk about?",
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "I've got a great idea!"
        })
    )

    body = forms.CharField(
        label="Tell me all about it!",
        widget=forms.Textarea(attrs={
            "placeholder": "Ideas go here..."
        })
    )
