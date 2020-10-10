from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'

        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_object_or_404(Product, pk=self.kwargs['pk']).name

        return context

def checkout(request):
    return render(request, 'checkout.html')
