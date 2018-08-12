from django.shortcuts import render


def aaron(request):
    return render(
        request,
        "static_pages/aaron.html",
        {
            "page_title": "About Aaron",
            "show_back_to_home": True,
        }
    )


def privacy(request):
    return render(
        request,
        "static_pages/privacy.html",
        {
            "page_title": "Privacy Policy",
            "show_back_to_home": True,
        }
    )


def test_page(request):
    return render(
        request,
        "static_pages/test.html",
        {
            "page_title": "Test Page",
            "show_back_to_home": True,
        }
    )