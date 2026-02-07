from django.urls import path
from . import views

urlpatterns=[
    path('products/add/',views.ProductCreateView.as_view(),name='add_product'),
    path('product/list/',views.ProductListView.as_view(),name='products_list'),
    path('product/detail/<int:pk>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('Product/update/<int:pk>/',views.ProductUpdateView.as_view(),name='update_product'),
    path('Product/delete/<int:pk>/',views.ProductDeleteView.as_view(),name='product_delete'),
]