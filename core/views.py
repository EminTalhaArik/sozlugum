from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from core.forms import SignUpForm
from .models import Dictionary, Term


def index(request):
    dictionaries = Dictionary.objects.all()
    context = {
        'dictionaries': dictionaries,
    }
    return render(request, 'core/index.html', context)


def get_terms_of_dictionary(request, slug):
    dictionary = Dictionary.objects.get(slug=slug)
    terms = Term.objects.filter(dictionary=dictionary)

    context = {
        'dictionary': dictionary,
        'terms': terms
    }

    return render(request, 'core/terms.html', context)


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'
