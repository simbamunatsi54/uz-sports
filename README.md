# UZ Sports

> A centralized sports management and information platform for the University of Zimbabwe.

UZ Sports is a Django-powered web application designed to bring University of Zimbabwe sporting activities into one modern, accessible platform.

The platform provides a central place for students, athletes, staff, and supporters to view teams, players, fixtures, results, standings, sports news, and sporting activities.

---

## Features

### 🏟️ Sports & Teams

* Browse sports offered by the university
* View registered teams
* Team profiles and descriptions
* Team logos and visual identity

### 👥 Players & Coaches

* Player profiles
* Player positions and jersey numbers
* Player photographs
* Coach information
* Team rosters

### 📅 Fixtures & Results

* Upcoming fixtures
* Completed matches
* Match dates and venues
* Match results
* Sport-based filtering

### 📊 League Standings

* Competition tables
* Team positions
* Matches played
* Wins, draws and losses
* Points and other statistical information

### 📰 Sports News

* University sports news
* Match reports
* Announcements
* Featured sporting stories

### 🖼️ Sports Gallery

* Sports photographs
* Team and match imagery
* Sporting-event highlights

### ⚙️ Administration

The Django administration interface allows authorized administrators to manage:

* Sports
* Teams
* Players
* Coaches
* Fixtures
* Results
* News
* Gallery content
* League standings

---

## Technology Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* JavaScript

### Database

* SQLite during development
* Django ORM

### Development Tools

* PyCharm
* Git
* GitHub

---

## Project Structure

```text
uz-sports/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── sports/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── teams.html
│   └── ...
│
├── static/
│   └── css/
│       └── style.css
│
├── media/
│   └── ...
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/uz-sports.git
cd uz-sports
```

Replace `YOUR-USERNAME` with the GitHub account that owns the repository.

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv uz
```

Activate it:

```bash
uz\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Apply migrations

```bash
python manage.py migrate
```

---

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

---

### 6. Start the development server

```bash
python manage.py runserver
```

Open the development site at:

```text
http://127.0.0.1:8000/
```

The Django administration panel is available at:

```text
http://127.0.0.1:8000/admin/
```

---

## Static & Media Files

The project uses Django's static-file system.

Static files are stored in:

```text
static/
```

For example:

```text
static/css/style.css
```

The project uses:

```python
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

Uploaded media such as team logos and player photographs are stored under:

```text
media/
```

---

## Development

After making changes to the project:

```bash
git add .
git commit -m "Describe your changes"
git push
```

Example:

```bash
git add .
git commit -m "Improve fixtures and results page"
git push
```

---

## Current Sports

The platform is designed to support multiple university sports, including:

* Rugby
* Football
* Cricket
* Tennis
* Chess
* Athletics
* Volleyball
* Basketball

Additional sports can be added through the Django administration interface.

---

## Project Goals

UZ Sports aims to provide:

1. A centralized source of university sports information.
2. Easier access to fixtures and results.
3. Better visibility for university teams and athletes.
4. A structured digital record of sporting activities.
5. A scalable foundation for future sports-related features.

---

## Future Development

Potential future improvements include:

* Live match updates
* Automated league-table calculations
* Player statistics
* Match notifications
* Search functionality
* Advanced sport and team filtering
* Mobile-first improvements
* REST API integration
* User accounts
* Athlete performance tracking
* Progressive Web App support
* Deployment to a production server

---

## Contributing

Contributions and suggestions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/your-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add your feature"
```

5. Push your branch.

```bash
git push origin feature/your-feature
```

6. Open a Pull Request.

---

## License

This project is currently intended as a University of Zimbabwe sports platform and development project.

License information can be added when the project's distribution and ownership requirements have been finalized.

---

## Author

**Simbarashe Munatsi**

UZ Sports
University of Zimbabwe

---

## Project Status

**Active Development**

UZ Sports is currently under development, with the core Django structure, sports management, teams, fixtures, results, news, standings, and frontend components being developed incrementally.
