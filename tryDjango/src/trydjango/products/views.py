from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.

# def product_create_view(request):
#     if request.method == "GET":
#         my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     title = request.POST.get('title')
#     print(title)
#     # Product.objects.Create(title=title)
#     return render(request, "products/product_create.html", {})

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = { 'form': form }
    return render(request, "products/product_create.html", context)

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description
#     # }
#     context = { 'product': obj }
#     return render(request, "products/product_detail.html", context)

def render_initial_data_view(request):
    obj = Product.objects.get(id=1)
    if request.method == "GET":
        form = ProductForm(request.GET or None, initial = { 'title':obj.title, 'description': obj.description, 'price': obj.price })   
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, id):
    # obj = get_object_or_404(Product, id=id)

    # alternate way to write the above statement
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "product": obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "product": obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    querySet = Product.objects.all()
    context = {
        "object_list" : querySet
    }
    return render(request, "products/product_list.html", context)

def product_update_view(request, id):
    obj = Product.objects.get(id=id)
    if request.method == 'GET':
        form = ProductForm(request.GET or None, instance=obj)
    if request.method == 'POST':
        form = ProductForm(request.POST or None)  
        if form.is_valid():
            obj.title = form.cleaned_data['title']
            obj.description = form.cleaned_data['description']
            obj.price = form.cleaned_data['price']
            obj.save()
    context = {
        'form': form
    }
    return render(request, "products/product_update.html", context)
    
