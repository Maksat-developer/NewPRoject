from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("category/", views.category, name="category"),
    path("checkout/", views.checkout, name="checkout"),
    path("confirmation/", views.confirmation, name="confirmation"),
    path("contact/", views.contact, name="contact"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    
]