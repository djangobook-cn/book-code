from django.urls import path
from article import views

urlpatterns = [
    path('category/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('category/list/', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('category/<int:pk>/list/', views.CategoryArticleListView.as_view(), name='category-article-list'),

    path('blog/add/', views.BlogCreateView.as_view(), name='blog-add'),
    path('blog/<int:pk>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/<int:pk>/detail/$', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog/list/list/backend/', views.BackendBlogListView.as_view(), name='blog-list-backend'),

    path('pure_page/add/', views.PurePageCreateView.as_view(), name='pure-page-add',),
    path('pure_page/<int:pk>/update/', views.PurePageUpdateView.as_view(), name='pure-page-update'),
    path('pure_page/<int:pk>/delete/', views.PurePageDeleteView.as_view(), name='pure-page-delete'),
    path('pure_page/list/backend/', views.PurePageListView.as_view(), name='pure-page-list'),

    path('upload/', views.image_upload_view, name='image-upload')
]
