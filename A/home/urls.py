from django.urls import path, include
from . import views

app_name = 'home'

bucket_urls =[
    path('', views.BucketView.as_view(), name='bucket'),
    path('delete_obj_bucket/<str:key>/', views.DeleteBucketObject.as_view(),name='delete_obj_bucket'),
]
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('bucket/', include(bucket_urls)),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]