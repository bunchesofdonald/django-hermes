from django.urls import re_path

from .views import (
    ArchivePostListView,
    AuthorPostListView,
    CategoryPostListView,
    PostDetail,
    PostListView,
)
from .feeds import LatestPostFeed

urlpatterns = [
    re_path(
        regex=r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w-]+)/$',
        view=PostDetail.as_view(),
        name='hermes_post_detail',
    ),

    re_path(
        regex=r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        view=ArchivePostListView.as_view(),
        name='hermes_archive_year_month_day',
    ),

    re_path(
        regex=r'^(?P<year>\d+)/(?P<month>\d+)/$',
        view=ArchivePostListView.as_view(),
        name='hermes_archive_year_month',
    ),

    re_path(
        regex=r'^(?P<year>\d+)/$',
        view=ArchivePostListView.as_view(),
        name='hermes_archive_year',
    ),

    re_path(
        regex=r'categories/(?P<slug>.+)/$',
        view=CategoryPostListView.as_view(),
        name='hermes_category_post_list',
    ),

    re_path(
        regex=r'authors/(?P<author>.+)/$',
        view=AuthorPostListView.as_view(),
        name='hermes_author_post_list',
    ),

    re_path(
        regex=r'^$',
        view=PostListView.as_view(),
        name='hermes_post_list',
    ),
    re_path(
        regex=r'^feed/$',
        view=LatestPostFeed(),
        name='hermes_post_feed'
    ),
)
