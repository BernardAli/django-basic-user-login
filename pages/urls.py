from django.urls import path
from .views import index_view, signup_view, login_view, logout_view, posts, counter


urlpatterns = [
    path('', index_view, name='index'),
    path('signup', signup_view, name='signup'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('post/<str:id>/', posts, name='post'),
    path('posts/', counter, name='posts')
]