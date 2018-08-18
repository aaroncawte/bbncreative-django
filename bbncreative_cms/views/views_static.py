from django.shortcuts import render


def privacy(request):
    return render(
        request,
        "static_pages/privacy.html",
        {
            "page_title": "Privacy Policy",
            "show_back_to_home": True,
        }
    )
