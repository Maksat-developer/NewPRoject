from django.shortcuts import render
from .models import Post



def index(request):
    
    posts = Post.objects.all
    context = {
    'posts': posts
}

    return render(request=request, 
                  template_name='blog/index.html',
                  context=context)

def about(request):
    return render(request=request, 
                  template_name='blog/about.html', 
                  context={'title': 'about'}
                  )
