from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# in each function view request is coming by default(request is first parameter)
def home_view(request, *args, **kwargs):
    print(*args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    my_context = {
        "my_text" : "this is about us",
        "my_number": 123,
        "this_is_true": True,
        "my_list": [123, 443, 1213, "string"],
        "html_tag": "<h1>Django</h1>"
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")