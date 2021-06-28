
from django.urls import path
from . import views

urlpatterns = [
   
    path('products',views.home_view),
    path('products/<int:id>',views.product_detail_view),
    path('api/products/1',views.product_api_detail)
    
]