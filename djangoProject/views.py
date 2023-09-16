from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, "home.html", {})

def header(request):
    return render(request, "header.html", {})

def contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact.html", context)


def resume(request):
    return render(request, "resume.html", {})

def expertise(request):
    return render(request, "expertise.html", {})

def about(request):
    return render(request, "about.html", {})