from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('products_list')

class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_product.html'
    context_object_name = 'product' 


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('products_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('products_list')