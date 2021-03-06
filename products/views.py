from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product

from carts.models import Cart


class ProductFeaturedListView(ListView):
    template_name = "products/featured_list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured_detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/product_list.html"
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()



def product_list_view(request):
    objects = Product.objects.all()
    return render(request, "products/product_list.html", {'objects':objects})


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"


    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"


    def get_context_data(self, *args, **kwargs):
        context  =  super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("uhmmm")
        return instance

def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk=pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    context  = {
    'object': instance
    }
    return render(request, "products/product_detail.html", context)
