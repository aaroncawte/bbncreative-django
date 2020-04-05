# For the contact form

from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template

from bbncreative import secrets
from bbncreative_cms.forms import ContactForm
from bbncreative_cms.views import view_functions


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # reCaptcha Validation
            recaptcha_response = request.POST.get("g-recaptcha-response")
            result = view_functions.get_recaptcha(recaptcha_response)

            # On successful validation
            if result["success"]:
                template = get_template("contact_template.txt")
                context = {
                    "contact_name": form.cleaned_data["name"],
                    "contact_email": form.cleaned_data["email"],
                    "form_content": form.cleaned_data["body"],
                }
                content = template.render(context)
                email = EmailMessage(
                    subject="[Website] " + form.cleaned_data["subject"],
                    body=content,
                    from_email="aaron@bbncreative.co",
                    to=["aaron@bbncreative.co"],
                    reply_to=[form.cleaned_data["email"]],
                    headers={"Content-Type": "text/plain"},
                )
                email.send()
                return HttpResponseRedirect("/contact-thanks")
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Your reCAPTCHA attempt failed. Please try again!",
                )

    form = ContactForm()

    return render(
        request,
        "static_pages/contact.html",
        {
            "page_title": "Get In Touch",
            "show_back_to_home": True,
            "form": form,
            "recaptcha_site_key": secrets.RECAPTCHA_SITE_KEY,
        },
    )


def contact_thanks(request):
    return render(
        request,
        "static_pages/contactThanks.html",
        {"page_title": "Thank you!", "show_back_to_home": True},
    )
