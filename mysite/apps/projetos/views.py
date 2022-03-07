from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CategoryForm, ProjetoForm
from .models import Category, Projeto
from django.contrib.auth.decorators import login_required

def add_category(request):
    template_name = 'apps/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, 'Categoria adicionada com sucesso')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)

def add_projeto(request):
    template_name = 'apps/add_projeto.html'
    context = {}
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            form.save_m2m()
            messages.success(request, 'Tarefa adicionada com sucesso')
        else:
            print(form.errors)
    form = ProjetoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_projeto(request):
    template_name = 'apps/list_projeto.html'
    context = {}
    projetos = Projeto.objects.filter(owner=request.user)
    context ['projetos'] = projetos
    return render(request, template_name, context)