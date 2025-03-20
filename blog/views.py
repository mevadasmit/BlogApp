from django.shortcuts import get_object_or_404, reverse, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.models import User
from .models import Post, PostImage, BlogComment, ReplyComment
from .forms import PostImagesForm
from django.views import View
from django.contrib import messages


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 4


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        images = list(post.images.all())
        context['images'] = images
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'header_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', args=[self.object.pk])


class PostCreateImageview(LoginRequiredMixin, CreateView):
    model = PostImage
    form_class = PostImagesForm
    template_name = 'blog/add_image.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if post.author != self.request.user:
            return redirect('post-detail', pk=post.pk)
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context


class PostDeleteImageview(View):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        image = post.images.all()
        context = {'post': post, 'images': image}
        return render(request, 'blog/delete_image.html', context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        get_image = request.POST.getlist('delete_image')

        for i in get_image:
            if i.startswith('post_'):
                post.header_image.delete(save=True)
                post.header_image = None
                post.save()

            elif i.startswith('image_'):
                image_object = get_object_or_404(PostImage, id=i.split('_')[1])
                image_object.image.delete(save=True)
                image_object.delete()

        return redirect('post-detail', pk=pk)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'header_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', args=[self.object.pk])

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class LikePostsView(View):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('blog-home', pk=pk)


class CommentPostView(View):

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        get_comment = request.POST.get('comment')
        insert_comments = BlogComment(post=post, user=request.user, comment=get_comment)
        insert_comments.save()
        return redirect('post-detail', pk=post.pk)


class ReplyCommentView(View):

    def post(self, request, pk):
        comment = get_object_or_404(BlogComment, pk=pk)
        get_reply = request.POST.get('reply')
        reply_comment = ReplyComment(
            comment_reply=comment,
            user=request.user,
            reply=get_reply,
            post=comment.post)
        reply_comment.save()
        return redirect('post-detail', pk=comment.post.pk)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogComment
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)


class ReplyDeleteView(LoginRequiredMixin, DeleteView):
    model = ReplyComment
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)


class About(ListView):
    model = Post
    template_name = 'blog/about.html'


class Service(ListView):
    model = Post
    template_name = 'blog/services.html'
