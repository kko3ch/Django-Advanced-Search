from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm

def product_search(request):
    products = Product.objects.all()
    form = ProductSearchForm(request.GET)

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if search_query:
            products = products.filter(name__icontains=search_query)

        if min_price:
            products = products.filter(price__gte=min_price)

        if max_price:
            products = products.filter(price__lte=max_price)

    # Add price sorting
    sort_by_price = request.GET.get('sort_by_price')
    if sort_by_price:
        if sort_by_price == 'asc':
            products = products.order_by('price')
        elif sort_by_price == 'desc':
            products = products.order_by('-price')

    return render(request, 'search/product_list.html', {'products': products, 'form': form})
