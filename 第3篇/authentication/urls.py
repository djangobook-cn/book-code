from django.urls import path

from authentication import views

urlpatterns = [
    path('user/login/', views.LoginView.as_view(), name='user-login'),
    path('user/logout/', views.LogoutView.as_view(), name='user-logout')
]
