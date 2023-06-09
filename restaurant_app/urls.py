from django.urls import path
from restaurant_app import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('home',views.home,name='home'),
    path('products',views.products,name='products'),
    path('products1',views.products1,name='products1'),
    path('cart',views.cart,name='cart'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('aboutus1',views.aboutus1,name='aboutus1'),
    path('contactus',views.contactus,name='contactus'),
    path('contactus1',views.contactus1,name='contactus1'),
    path('checkout',views.checkout,name='checkout'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('product_detail',views.product_detail,name='product_detail'),
    path('product_detail1',views.product_detail1,name='product_detail1'),
    path('home_page1',views.home_page1,name='home_page1'),





]