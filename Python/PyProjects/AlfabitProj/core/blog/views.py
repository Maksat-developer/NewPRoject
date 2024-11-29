from django.shortcuts import render

def index(request):
    return render(request,template_name='blog/index.html')



def reviews(request):
    return render(request, template_name='blog/reviews.html')
