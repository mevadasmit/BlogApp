from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils import timezone


class Post(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to='images')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_likes')

    def __str__(self):
        return f"{self.title} And Added by {self.author}"

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return redirect('post-detail', kwargs={'pk': self.pk})


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.post.title} And Added by {self.post.author}"


class BlogComment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" Commented By : {self.user.username}"

    def get_comment_count(self):
        return self.comment.count


class ReplyComment(models.Model):
    comment_reply = models.ForeignKey(BlogComment, related_name='reply_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reply by {self.user}."