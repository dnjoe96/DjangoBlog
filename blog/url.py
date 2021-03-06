from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),  # using function  # without tag
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),  # using function  # with tag
    # path('', views.PostListView.as_view(), name='post_list'),  # using classed based views
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
path('feed/', LatestPostsFeed(), name='post_feed'),
]
