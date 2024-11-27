from django.urls import path
from .views import register_view, test_view, login_view, home_page, continue_shopping

urlpatterns = [
    path('register/', register_view, name='register'),
    path('test/', test_view, name='test'),
    path('login/', login_view, name='login'),
    path('home/', home_page, name='home_page'),
    path('continue-shopping/', continue_shopping, name='continue_shopping'),
]
