from django.urls import path, include

from  .views import products , product_detail
urlpatterns = [
    path('product/', products ),
    path('product/<int:id>' ,  product_detail)
]