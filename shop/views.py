from types import NoneType

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .forms import ProductFilterForm, SupplierForm
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
# Create your views here.

def product_list(request):
    list_product = Product.objects.all()
    context = {
        'product_list': list_product
    }
    return render(request, 'shop/product/catalog.html', context)

def product_list_with_filter(request):
    list_product = Product.objects.all()
    if request.GET != None:
        product_form = ProductFilterForm(request.GET)
    else:
        product_form = ProductFilterForm()

    if product_form.is_valid():
        if product_form.cleaned_data.get('name') != "":
            list_product = list_product.filter(name__icontains=product_form.cleaned_data.get('name'))
        if product_form.cleaned_data.get('min_price'):
            list_product = list_product.filter(price__gte=product_form.cleaned_data.get('min_price'))
        if product_form.cleaned_data.get('max_price'):
            list_product = list_product.filter(price__lte=product_form.cleaned_data.get('max_price'))

        context = {
            'list_product': list_product,
            'form': product_form
        }
        return render(request, 'shop/product/catalog_filter.html', context)


def get_one_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, 'shop/product/one_product_table.html', context)


def get_one_filter_product(request):
    find_product = Product.objects.filter(is_exists=request.GET.get('is_ex'))
    context = {
        'find_product': find_product
    }
    return render(request, 'shop/product/query_filter_product.html', context)

def get_more_filter_product(request):
    find_product = Product.objects.filter(
        price__lte=request.GET.get('max_price'),
        price__gt=request.GET.get('min_price')
    )
    context = {
        'find_product': find_product
    }
    return render(request, 'shop/product/query_filter_product.html', context)


class ListSupplier(ListView):
    model = Supplier
    template_name = 'shop/supplier/supplier_list.html'
    allow_empty = True
    paginate_by = 1


class CreateSupplier(CreateView):
    model = Supplier
    extra_context = {
        'action': 'Создать'
    }
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm


class UpdateSupplier(UpdateView):
    model = Supplier
    extra_context = {
        'action': 'Изменить'
    }
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm


class DetailSupplier(DetailView):
    model = Supplier
    template_name = 'shop/supplier/supplier_detail.html'


class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = 'shop/supplier/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')




