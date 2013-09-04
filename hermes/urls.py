from django.conf.urls import patterns, url

from .views import ArchivePostListView, PostListView, PostDetail, CategoryPostListView
from .feeds import LatestPostFeed

urlpatterns = patterns('',
    url(
        regex=r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w-]+)/$',
        view=PostDetail.as_view(),
        name='hermes_post_detail',
    ),

    url(
        regex=r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        view=ArchivePostListView.as_view(),
        name='hermes_archive_year_month_day',
    ),

    url(
        regex=r'^(?P<year>\d+)/(?P<month>\d+)/$',
        view=ArchivePostListView.as_view(),
        name='hermes_archive_year_month',
    ),

    url(
        regex=r'^(?P<year>\d+)/$',
        view=ArchivePostListView.as_view(),
        name='hermes_archive_year',
    ),

    url(
        regex=r'categories/(?P<slug>.+)/$',
        view=CategoryPostListView.as_view(),
        name='hermes_category_post_list',
    ),

    url(
        regex=r'^$',
        view=PostListView.as_view(),
        name='hermes_post_list',
    ),
    url(
        regex=r'^feed/$',
        view=LatestPostFeed(),
        name='hermes_post_feed'
    ),
)
