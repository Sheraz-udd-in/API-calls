from django.urls import path, include

from  .views import *
urlpatterns = [
    path('product/', products ),
    path('product/<int:id>' ,  product_detail),
    path('product/<int:id>/update', product_update),
    path('product/<int:id>/delete',product_delete),
    
]