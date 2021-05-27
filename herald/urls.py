from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name='herald-home'),
    path('review/', PostListView.as_view(), name='herald-review'),
    path('review/new/', PostCreateView.as_view(), name='create-post'),
    path('review/<int:pk>/update/', PostUpdateView.as_view(), name='update-post'),
    path('review/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post'),
    path('get', views.chat, name='chat'),
]
