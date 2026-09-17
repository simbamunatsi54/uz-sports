from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=150)
    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE,
        related_name="teams"
    )
    logo = models.ImageField(upload_to="teams/", blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="players"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    jersey_number = models.PositiveIntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to="players/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Coach(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="coaches"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="Head Coach")
    photo = models.ImageField(upload_to="coaches/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Venue(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("live", "Live"),
        ("completed", "Completed"),
        ("postponed", "Postponed"),
    ]

    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="home_fixtures"
    )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="away_fixtures"
    )
    venue = models.ForeignKey(
        Venue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="upcoming"
    )

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"


class Result(models.Model):
    fixture = models.OneToOneField(
        Fixture,
        on_delete=models.CASCADE,
        related_name="result"
    )
    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.fixture}: {self.home_score} - {self.away_score}"


class LeagueTable(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    played = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    drawn = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    points = models.IntegerField(default=0)

    class Meta:
        ordering = ["-points", "-won"]

    def __str__(self):
        return self.team.name


class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True
    )
    content = models.TextField()
    author = models.CharField(max_length=150, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery/")
    caption = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title

class PlayerStatistic(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="statistics",
    )

    season = models.CharField(
        max_length=50,
        blank=True,
    )

    competition = models.CharField(
        max_length=150,
        blank=True,
    )

    statistic = models.CharField(
        max_length=100,
    )

    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    unit = models.CharField(
        max_length=30,
        blank=True,
    )

    class Meta:
        ordering = ["statistic"]

    def __str__(self):
        return f"{self.player} - {self.statistic}: {self.value}"