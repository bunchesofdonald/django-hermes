import hashlib

from django.views.decorators.http import condition
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator

from .models import Post


def latest_post(request, *args, **kwargs):
    return Post.objects.latest().modified_on


def get_etag(request, *args, **kwargs):
    post_modified_on = str(latest_post(request, *args, **kwargs))
    return hashlib.md5(
        "-".join(('blog', post_modified_on)).encode('utf-8')
    ).hexdigest()


@method_decorator(
    condition(last_modified_func=latest_post, etag_func=get_etag),
    name='get'
)
class PostListView(ListView):
    """Base Post List View."""
    context_object_name = 'posts'
    model = Post
    template_name = 'hermes/post_list.html'

    def get_queryset(self):
        return self.model.objects.published()


class CategoryPostListView(PostListView):
    """Displays posts from a specific Category"""
    def get_queryset(self):
        category_slug = self.kwargs.get('slug', '')
        return self.model.objects.in_category(category_slug)


class ArchivePostListView(PostListView):
    """Displays posts from a specific Year/Month/Day"""
    def get_queryset(self):
        year = self.kwargs.get('year', None)
        month = self.kwargs.get('month', None)
        day = self.kwargs.get('day', None)

        return self.model.objects.created_on(year=year, month=month, day=day)


class AuthorPostListView(PostListView):
    """Displays posts from a specific Author"""
    def get_queryset(self):
        author = self.kwargs.get('author', '')
        return self.model.objects.by(author)


class PostDetail(DetailView):
    context_object_name = 'post'
    model = Post
    template_name = "hermes/post_detail.html"
