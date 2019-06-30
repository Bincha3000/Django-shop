from django.shortcuts import render, render_to_response

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from cart.forms import CartAddProductForm

from .models import Category, Product

class CatalogView(TemplateView):
    template_name = 'products_list/products.html'

    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        context = {
            'category': category,
            'categories':categories,
            'products': products,
        }
        return render(request, self.template_name, context)

class ProductDetailView(TemplateView):
    template_name = 'products_list/product_detail.html'

    def get(self, request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug)
        cart_product_form = CartAddProductForm()
        return render_to_response(self.template_name,
                                 {'product': product,
                                  'cart_product_form': cart_product_form})