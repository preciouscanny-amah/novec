from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User


   

def home(request):
    context = {
        'skill' : Post.objects.all()
    }
    return render(request, 'pouch/home.html', context)

class PostlistView(ListView):
    model = Post
    template_name = 'pouch/home.html'
    context_object_name = 'skill'
    odering =['-posted_on']
    paginate_by = 3

class UserPostlistView(ListView):
    model = Post
    template_name = 'pouch/user_posts.html'
    context_object_name = 'skill'
    
   
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-posted_on')

class PostDetailView(DetailView):
    model = Post

 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

   


class UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user ==post.author:
            return True
        return False  


class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user ==post.author:
            return True
        return False    


    
def about(request):
    return render(request, 'pouch/about.html')
 