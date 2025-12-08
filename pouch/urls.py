from django.urls import path
from .views import ( 
    PostlistView, PostDetailView, PostCreateView, UpdateView, DeleteView, UserPostlistView
)
from . import views

urlpatterns = [
    path('', PostlistView.as_view(), name='home page'),
    path('user/<str:username>/', UserPostlistView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='Delete-post'),  
    path('about/', views.about, name='About...'),
]

