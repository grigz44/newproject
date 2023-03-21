from django.urls import path
from acc import views as api_views

from acc import views

from rest_framework.routers import DefaultRouter




urlpatterns = [
    
    path('usereg/', api_views.usereg.as_view(), name="loginapi"),
    path('user/', api_views.usercreate.as_view(), name="logi"),
    path('product/', api_views.createproduct.as_view(), name=""),
    path('product/<Unique_id>', api_views.createproduct.as_view(), name=""),
    path('productimg/', api_views.productimg.as_view(), name=""),
    path('productadd/', api_views.addproduct.as_view(), name=""),
    
    
    
]