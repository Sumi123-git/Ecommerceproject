from django.urls import path
from shopapp import views
app_name = 'shopapp'

urlpatterns = [
    # path('',views.commerce,name='commerce')
    path('', views.allproductcategory, name='allproductcategory'),
    path('<slug:c_slug>/', views.allproductcategory, name='allproductcategory'),
    path('<slug:c_slug>/<slug:product_slug>/', views.Productdetail, name='productdetail'),
]
