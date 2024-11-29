from django.shortcuts import render

def index(request):
    return render(request, "store/index.html")


def cart(request):
    return render(request, "store/cart.html")


def category(request):
    return render(request, "store/category.html")


def checkout(request):
    return render(request, "store/checkout.html")


def contact(request):
    return render(request, "store/contact.html")


def login(request):
    return render(request, "store/login.html")


def register(request):
    return render(request, "store/register.html")


def confirmation(request):
    return render(request, "store/confirmation.html")



