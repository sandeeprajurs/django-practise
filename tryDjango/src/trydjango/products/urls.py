from products.views import (
    product_create_view, 
    render_initial_data_view, 
    dynamic_lookup_view, 
    product_delete_view, 
    product_list_view,
    product_update_view
    )
from django.urls import path

urlpatterns = [
    path('', product_list_view, name='products_list'),
    path('<int:id>', dynamic_lookup_view, name='product_detail_view'),
    path('<int:id>/delete/', product_delete_view, name='product_delete'),
    path('<int:id>/update/', product_update_view, name='product_update'),
    path('create/', product_create_view, name="product_create_view"),
    path('initial/', render_initial_data_view)
]