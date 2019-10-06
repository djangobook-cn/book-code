from django.urls import path
from management import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_img/', views.add_img, name='add_img'),
    path('book_list/<str:category>/', views.book_list, name='book_list'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail')
]
