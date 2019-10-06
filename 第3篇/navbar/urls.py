from django.urls import path

from navbar import views

urlpatterns = [
    path('add/', views.NavItemCreateView.as_view(), name='navbar-add'),
    path('list/', views.NavItemListView.as_view(), name='navbar-list'),
    path('<int:pk>/update/', views.NavItemUpdateView.as_view(), name='navbar-update'),
    path('<int:pk>/delete/', views.NavItemDeleteView.as_view(), name='navbar-delete'),
]
