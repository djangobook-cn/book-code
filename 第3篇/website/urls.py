from django.urls import path

from website import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('dashboard/', views.DashboardOverviewView.as_view(), name='dashboard'),
]
