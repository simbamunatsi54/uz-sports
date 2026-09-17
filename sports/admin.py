from django.contrib import admin
from .models import (
    Sport,
    Team,
    Player,
    Coach,
    Venue,
    Fixture,
    Result,
    LeagueTable,
    News,
    Gallery,
    PlayerStatistic,
)


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "sport")
    list_filter = ("sport",)
    search_fields = ("name",)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "team",
        "position",
        "jersey_number",
    )
    list_filter = ("team", "position")
    search_fields = ("first_name", "last_name")


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "team",
        "role",
    )
    list_filter = ("team", "role")
    search_fields = ("first_name", "last_name")


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    search_fields = ("name", "location")


@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = (
        "home_team",
        "away_team",
        "sport",
        "date",
        "time",
        "status",
    )
    list_filter = ("sport", "status", "date")
    search_fields = (
        "home_team__name",
        "away_team__name",
    )


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "fixture",
        "home_score",
        "away_score",
    )


@admin.register(LeagueTable)
class LeagueTableAdmin(admin.ModelAdmin):
    list_display = (
        "team",
        "sport",
        "played",
        "won",
        "drawn",
        "lost",
        "points",
    )
    list_filter = ("sport",)
    ordering = ("-points", "-won")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "published_at",
    )
    list_filter = ("published_at",)
    search_fields = ("title", "content")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "uploaded_at",
    )
    search_fields = ("title", "caption")

@admin.register(PlayerStatistic)
class PlayerStatisticAdmin(admin.ModelAdmin):
    list_display = (
        "player",
        "statistic",
        "value",
        "unit",
        "season",
        "competition",
    )

    list_filter = (
        "season",
        "competition",
        "statistic",
    )

    search_fields = (
        "player__first_name",
        "player__last_name",
        "statistic",
        "competition",
    )