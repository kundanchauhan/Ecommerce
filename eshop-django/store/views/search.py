from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.category import Category


class Search(View):
    def get(self, request):
        search = request.GET.get('search')
        
        print(search)
        products = Product.get_all_products().filter(name__icontains =search)
        print("product",products)
        categories = Category.get_all_categories()
        data = {}
        data['products'] = products
        data['categories'] = categories
        
        return render(request, 'search.html', data)
