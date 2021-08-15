from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from user.views import register, user_detail

urlpatterns = [
    path('user-detail/<int:pk>/', user_detail, name='user_detail'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='users/logout.html'
    ), name='logout'),
]