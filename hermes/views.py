from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'hermes/post_list.html'


class ArchivePostListView(PostListView):
    pass


class PostDetail(DetailView):
    context_object_name = 'post'
    model = Post
    template_name = "hermes/post_detail.html"
