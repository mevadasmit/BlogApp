from django.urls import path
from .views import (PostListView , PostDetailView , PostCreateView ,PostUpdateView ,
                    PostDeleteView ,UserPostListView, PostCreateImageview, PostDeleteImageview ,
                    LikePostsView,
                    CommentPostView ,ReplyCommentView, CommentDeleteView,ReplyDeleteView, About , Service)
urlpatterns = [
    path("", PostListView.as_view() , name = "blog-home"),
    path("user/<str:username>", UserPostListView.as_view() , name = "user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view() , name = "post-detail"),
    path('post/new/', PostCreateView.as_view() , name = "post-create"),
    path('post/<int:pk>/update', PostUpdateView.as_view() , name = "post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view() , name = "post-delete"),
    path('post/<int:pk>/add_image/', PostCreateImageview.as_view() , name = "add-post-image"),
    path('post/<int:pk>/delete_image/', PostDeleteImageview.as_view() , name = "delete-post-image"),
    path('post/<int:pk>/x', LikePostsView.as_view() , name = "like-post"),
    path('post/<int:pk>/comment/', CommentPostView.as_view() , name = "post-comment"),
    path('post/<int:pk>/comment/delete', CommentDeleteView.as_view() , name = "comment-delete"),
    path('post/<int:pk>/reply/', ReplyCommentView.as_view() , name = "comment-reply"),
    path('post/<int:pk>/reply/delete', ReplyDeleteView.as_view() , name = "delete-reply"),
    path("about/",About.as_view() , name = "blog-About"),
    path("service/", Service.as_view() , name ="blog-Service")
]
