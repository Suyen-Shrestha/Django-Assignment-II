from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.views.generic import View, TemplateView, CreateView
from .forms import UserRegistrationForm, UserLoginForm


def home_view(request):
    return render(request, 'user/home.html')


class UserProfileView(TemplateView):
    template_name = 'user/profile.html'


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        if 'profile_pic' in self.request.FILES:
            form.instance.profile_pic = self.request.FILES['profile_pic']
            form.save()
            messages.success(self.request, f'User Registered Successfully!')
        return redirect(self.success_url)


class UserLoginView(View):
    form_class = UserLoginForm()
    template_name = 'user/login.html'
    success_url = reverse_lazy('user:profile')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f'Successfully logged in as {email}.')
                return HttpResponseRedirect(self.success_url)
            else:
                messages.error(request, 'The user is currently inactive.')
                return redirect('user:login')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('user:login')


class UserLogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logged out Successfully!')
        return redirect('user:login')



