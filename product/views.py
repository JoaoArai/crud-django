from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Produtos

class ProdutosListView(ListView):
    model = Produtos
    template_name = 'produto-list.html'

class ProdutosDetailView(DetailView):
    model = Produtos
    template_name = 'produto-detail.html'
    
class ProdutosCreateView(CreateView):
    model = Produtos
    template_name = 'produtos-form.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('produto-list')

class ProdutosDeleteView(DeleteView):
    model = Produtos
    template_name = 'produto-confirm-delete.html'
    success_url = reverse_lazy('produto-list')

class ProdutosUpdateView(UpdateView):
    model = Produtos
    template_name = 'produtos-form.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('produto-list')
 
