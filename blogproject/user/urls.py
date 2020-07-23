from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileView
from blog.views import UserBlogListView


app_name = 'user'

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('myblogs/', UserBlogListView.as_view(), name='myblogs')
]