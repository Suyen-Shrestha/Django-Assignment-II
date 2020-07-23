from django.urls import path
from .views import BlogsListView, BlogCreateView

app_name = 'blog'

urlpatterns = [
    path('list/', BlogsListView.as_view(), name='blog-list'),
    path('create/', BlogCreateView.as_view(), name='blog-create')
]