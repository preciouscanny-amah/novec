from django.shortcuts import render
from .models import Post
   

def home(request):
    text = {
        'skill' : Post.objects.all()
    }
    return render(request, 'pouch/home.html', text)

def about(request):
    return render(request, 'pouch/about.html')
 