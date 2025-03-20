from django.contrib import admin
from .models import Post , PostImage , BlogComment , ReplyComment

admin.site.register((Post , PostImage , BlogComment, ReplyComment))

# Register your models here.
