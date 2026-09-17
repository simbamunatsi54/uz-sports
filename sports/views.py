from django.shortcuts import render, get_object_or_404
from .models import Sport, Team, Fixture, Result, News, LeagueTable, Gallery, Player
from django.db import models

def home(request):
    sports = Sport.objects.all()

    upcoming_fixtures = (
        Fixture.objects
        .filter(status="upcoming")
        .select_related(
            "sport",
            "home_team",
            "away_team",
            "venue",
        )
        .order_by("date", "time")[:5]
    )

    recent_results = (
        Result.objects
        .select_related(
            "fixture",
            "fixture__sport",
            "fixture__home_team",
            "fixture__away_team",
            "fixture__venue",
        )
        .order_by(
            "-fixture__date",
            "-fixture__time",
        )[:5]
    )

    latest_news = News.objects.all()[:3]

    teams = (
        Team.objects
        .select_related("sport")
        .all()
    )

    gallery_items = (
        Gallery.objects
        .all()
        .order_by("-uploaded_at")[:7]
    )

    league_table = (
        LeagueTable.objects
        .select_related("sport", "team")
        .all()
        .order_by("-points", "-won")[:5]
    )

    return render(request, "home.html", {
        "sports": sports,
        "teams": teams,
        "upcoming_fixtures": upcoming_fixtures,
        "recent_results": recent_results,
        "latest_news": latest_news,
        "gallery_items": gallery_items,
        "league_table": league_table,
    })

def teams(request):
    sports = Sport.objects.all()

    teams = (
        Team.objects
        .select_related("sport")
        .prefetch_related("players", "coaches")
        .all()
    )

    sport_id = request.GET.get("sport")

    if sport_id:
        teams = teams.filter(sport_id=sport_id)

    return render(request, "teams.html", {
        "teams": teams,
        "sports": sports,
        "selected_sport": sport_id,
    })


def team_detail(request, team_id):
    team = get_object_or_404(
        Team.objects.select_related("sport"),
        id=team_id
    )

    players = team.players.all()
    coaches = team.coaches.all()

    context = {
        "team": team,
        "players": players,
        "coaches": coaches,
    }

    return render(request, "team_detail.html", context)
def news(request):
    news_list = News.objects.all()
    return render(request, "news.html",{"news_list": news_list})
def news_detail(request, news_id):
    article = get_object_or_404(News, id=news_id)
    return render(request, "news_detail.html", {"article": article})

def standings(request):
    sports = Sport.objects.all().order_by("name")
    selected_sport = request.GET.get("sport")

    table = []

    # A standings table only makes sense when a specific
    # sport has been selected.
    if selected_sport:

        completed_results = (
            Result.objects
            .filter(
                fixture__status="completed",
                fixture__sport_id=selected_sport,
            )
            .select_related(
                "fixture",
                "fixture__home_team",
                "fixture__away_team",
                "fixture__sport",
            )
        )

        team_ids = set()

        for result in completed_results:
            team_ids.add(result.fixture.home_team_id)
            team_ids.add(result.fixture.away_team_id)

        teams = (
            Team.objects
            .filter(id__in=team_ids)
            .select_related("sport")
        )

        for team in teams:

            team_results = completed_results.filter(
                models.Q(fixture__home_team=team) |
                models.Q(fixture__away_team=team)
            )

            played = 0
            won = 0
            drawn = 0
            lost = 0
            goals_for = 0
            goals_against = 0
            points = 0

            for result in team_results:

                fixture = result.fixture

                if fixture.home_team_id == team.id:
                    team_score = result.home_score
                    opponent_score = result.away_score
                else:
                    team_score = result.away_score
                    opponent_score = result.home_score

                played += 1
                goals_for += team_score
                goals_against += opponent_score

                if team_score > opponent_score:
                    won += 1
                    points += 3

                elif team_score == opponent_score:
                    drawn += 1
                    points += 1

                else:
                    lost += 1

            goal_difference = goals_for - goals_against

            table.append({
                "team": team,
                "sport": team.sport,
                "played": played,
                "won": won,
                "drawn": drawn,
                "lost": lost,
                "goals_for": goals_for,
                "goals_against": goals_against,
                "goal_difference": goal_difference,
                "points": points,
            })

        # Official-style ordering:
        # Points → Goal Difference → Goals For → Wins
        table.sort(
            key=lambda row: (
                row["points"],
                row["goal_difference"],
                row["goals_for"],
                row["won"],
            ),
            reverse=True,
        )

    context = {
        "sports": sports,
        "table": table,
        "league_table": table,
        "selected_sport": selected_sport,
    }

    return render(request, "standings.html", context)
def fixtures_results(request):
    sport_id = request.GET.get("sport")

    fixtures = (
        Fixture.objects
        .filter(status="upcoming")
        .select_related(
            "sport",
            "home_team",
            "away_team",
            "venue",
        )
        .order_by("date", "time")
    )

    results = (
        Result.objects
        .select_related(
            "fixture",
            "fixture__sport",
            "fixture__home_team",
            "fixture__away_team",
            "fixture__venue",
        )
        .order_by("-fixture__date", "-fixture__time")
    )

    # Filter fixtures and results by sport
    if sport_id:
        fixtures = fixtures.filter(sport_id=sport_id)
        results = results.filter(fixture__sport_id=sport_id)

    sports = Sport.objects.all().order_by("name")

    context = {
        "fixtures": fixtures,
        "results": results,
        "sports": sports,
        "selected_sport": sport_id,
    }

    return render(request, "fixtures_results.html", context)
def gallery(request):
    gallery_items = Gallery.objects.all()

    return render(
        request,
        "gallery.html",
        {"gallery_items": gallery_items}
    )
def player_detail(request, player_id):
    player = get_object_or_404(
        Player.objects.select_related(
            "team",
            "team__sport",
        ),
        id=player_id,
    )

    statistics = (
        player.statistics
        .all()
        .order_by(
            "season",
            "competition",
            "statistic",
        )
    )

    return render(
        request,
        "player_detail.html",
        {
            "player": player,
            "statistics": statistics,
        },
    )