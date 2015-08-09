from django.views.generic import ListView, DetailView

from .models import Post


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
