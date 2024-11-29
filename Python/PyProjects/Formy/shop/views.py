from django.shortcuts import render
from .models import Person
from .forms import PersonForm


# def index(request):
#     return render(request, "index.html")

def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        form = PersonForm()
        return render(request, "index.html", {"form": form})
