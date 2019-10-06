from django.urls import path
from link import views

urlpatterns = [
    path('add/', views.LinkCreateView.as_view(), name='link-add'),
    path('list/', views.LinkListView.as_view(), name='link-list'),
    path('<int:pk>/update/', views.LinkUpdateView.as_view(), name='link-update'),
    path('<int:pk>/delete/', views.LinkDeleteView.as_view(), name='link-delete')
]
