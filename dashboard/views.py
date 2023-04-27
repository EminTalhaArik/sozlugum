from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import DictionaryForm, DictionaryCategoryForm, TermForm, TermCategoryForm
from core.models import Dictionary, DictionaryCategory, Term, TermCategory


@login_required
def index(request):
    dictionaries = Dictionary.objects.filter(created_by=request.user)

    context = {
        'dictionaries': dictionaries
    }

    return render(request, 'dashboard/index.html', context)


@login_required
def dictionary_detail(request, pk):
    context = {
        'pk': pk
    }
    return render(request, 'dashboard/details.html', context)


@login_required
def create_dictionary(request):
    if request.method == 'POST':
        form = DictionaryForm(request.POST, request.FILES)

        if form.is_valid():
            dictionary = form.save(commit=False)
            dictionary.created_by = request.user
            form.save()

            return redirect('dashboard:dictionary_detail', pk=dictionary.id)

    else:
        form = DictionaryForm

    context = {
        'form': form
    }

    return render(request, 'dashboard/form.html', context)


@login_required
def create_dictionary_category(request):
    if request.method == 'POST':
        form = DictionaryCategoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=False)

            return redirect('dashboard:index')

    else:
        form = DictionaryCategoryForm

    context = {
        'form': form
    }

    return render(request, 'dashboard/form.html', context)


@login_required
def create_term(request, dictionary_pk):
    if request.method == 'POST':
        form = TermForm(request.POST, request.FILES)

        if form.is_valid():
            term = form.save(commit=False)
            term.dictionary = Dictionary.objects.get(pk=dictionary_pk)
            form.save()

            return redirect('dashboard:index')

    else:
        form = TermForm

    context = {
        'form': form
    }

    return render(request, 'dashboard/form.html', context)


@login_required
def create_term_category(request, dictionary_pk):
    if request.method == 'POST':
        form = TermCategoryForm(request.POST, request.FILES)

        if form.is_valid():
            term_category = form.save(commit=False)
            term_category.dictionary = Dictionary.objects.get(pk=dictionary_pk)
            form.save()

            return redirect('dashboard:index')

    else:
        form = TermCategoryForm

    context = {
        'form': form
    }

    return render(request, 'dashboard/form.html', context)
