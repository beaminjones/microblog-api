from django.urls import path
from .views import LoginView, RegisterView, FollowUserView, CreatePostView, LikePostView, CommentPostView, FeedView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), 
    path('register/', RegisterView.as_view(), name='register'),
    path('follow/', FollowUserView.as_view(), name='follow_user'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('like_post/', LikePostView.as_view(), name='like_post'),
    path('comment_post/', CommentPostView.as_view(), name='comment_post'),
    path('feed/<int:user_id>/', FeedView.as_view(), name='feed'),
]
