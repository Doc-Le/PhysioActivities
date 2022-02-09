from django.shortcuts import render

TEMPLATE_ROOT = 'signup/index.html'


def signup(request):
    """ Display the user's profile. """

    context = {}

    return render(request, TEMPLATE_ROOT, context)


def login(request):
    """ Display the user's profile. """

    context = {}

    return render(request, TEMPLATE_ROOT, context)
