from django.urls import path
import blog.views as blog_views


urlpatterns = [
    # path('list/', blog_views.blog_list),
    # path('detail/<int:blog_id>/', blog_views.blog_detail),
    path('list/', blog_views.BlogListView.as_view()),
    path('detail/<int:pk>/', blog_views.BlogDetailView.as_view()),
]
