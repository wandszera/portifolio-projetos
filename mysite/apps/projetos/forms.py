from django import forms

from .models import Category, Projeto

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('owner',)

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        exclude = ('owner',)