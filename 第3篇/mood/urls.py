from django.urls import path
from mood import views


urlpatterns = [
    path('add/', views.MoodCreateView.as_view(), name='mood-add'),
    path('list/', views.MoodListView.as_view(), name='mood-list'),
    path('<int:pk>/update/', views.MoodUpdateView.as_view(), name='mood-update'),
    path('<int:pk>/delete/', views.MoodDeleteView.as_view(), name='mood-delete'),
    path('timeline/', views.MoodTimeLineView.as_view(), name='mood-time-line')
]