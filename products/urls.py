from django.urls import path

from .views import (ProductListView,
 product_list_view,
 # ProductDetailView,
 # product_detail_view,
 # ProductFeaturedListView,
 # ProductFeaturedDetailView,
 ProductDetailSlugView,
 )
urlpatterns = [
    #product urls
    path('', ProductListView.as_view(), name='list'),
    # path('', product_list_view, name='list'),

    # path('products/<int:pk>/', ProductListView.as_view()),
    # path('products-fbv/<int:pk>/', product_detail_view),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
]
