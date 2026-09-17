from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from sports.views import (
    home,
    teams,
    team_detail,
    player_detail,
    news,
    news_detail,
    standings,
    fixtures_results,
    gallery,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("teams/", teams, name="teams"),

    path(
        "teams/<int:team_id>/",
        team_detail,
        name="team_detail"
    ),
    path(
        "players/<int:player_id>/",
        player_detail,
        name="player_detail"
    ),
path("news/", news, name="news"),
path("news/<int:news_id>/", news_detail, name="news_detail"),
path("standings/", standings, name="standings"),
path("fixtures-results/", fixtures_results, name="fixtures_results"),
path("gallery/", gallery, name="gallery"),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )