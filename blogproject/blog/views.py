from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import BlogArticle
from user.models import CustomUser
from .forms import BlogCreateForm


class BlogsListView(ListView):
    queryset = BlogArticle.objects.all()
    template_name = 'blog/bloglist.html'
    context_object_name = 'blogs'


class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogCreateForm
    template_name = 'blog/blogcreate.html'
    success_url = reverse_lazy('blog:blog-list')
    login_url = 'user:login'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            form.save()
            return redirect(self.success_url)


class UserBlogListView(LoginRequiredMixin, ListView):
    """
    List blogs related to a particular logged in user.
    """
    model = BlogArticle
    template_name = 'user/userblogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_in_user = CustomUser.objects.get(email=self.request.user.email)
        blogs = BlogArticle.objects.filter(author=logged_in_user)
        context['blogs'] = blogs
        return context

