# CampusPlay

A college OTT platform backend — think Netflix, but for your campus.
Students can browse lecture recordings, fest performances, sports events,
and short films. Built with PostgreSQL (Supabase), Python, and Streamlit.

> Live database hosted on Supabase (Mumbai) — data persists across devices and sessions.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Database | PostgreSQL 18 (Supabase Cloud) |
| Backend | Python, psycopg2, SQLAlchemy |
| Data | Pandas |
| Frontend | Streamlit |
| Charts | Plotly |
| Security | python-dotenv |
| Version Control | Git + GitHub |

---

## Features

- **Analytics Dashboard**
  - Most watched videos (bar chart)
  - Watches by category (pie chart)
  - Top rated videos (table)
  - Most active students (table)

- **Video Library**
  - Browse all videos with category
  - Add new videos with category selection

- **Students**
  - View all registered students
  - Add new students with plan selection
  - Duplicate email detection

- **Ratings**
  - View all ratings with student and video info
  - Add ratings with review
  - Prevents duplicate ratings per student per video

---

## Database Schema

7 tables with full relational design:

```
plans          → subscription tiers (Free, Student Premium, Faculty)
categories     → content types (Lectures, Fest, Sports, Short Films)
students       → platform users linked to plans
videos         → content library linked to categories
subscriptions  → student + plan relationship tracking
watch_history  → every student watch event recorded
ratings        → student reviews with composite unique constraint
```

---

## Project Structure

```
campusplay/
├── .env                    # database credentials (not in repo)
├── .gitignore              # protects .env and cache files
├── requirements.txt        # all dependencies
├── README.md
├── backend/
│   ├── connection.py       # psycopg2 + SQLAlchemy engine
│   ├── students.py         # student CRUD operations
│   ├── videos.py           # video CRUD operations
│   ├── ratings.py          # ratings management
│   └── analytics.py        # dashboard analytics queries
└── frontend/
    └── app.py              # Streamlit web application
```

---

## How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Shauryagupta4/campusplay_backend.git
cd campusplay
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment**

Create a `.env` file in the project root:
```
DB_HOST=your_supabase_host
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_supabase_password
```

Get these values from your Supabase project → Connect → Direct Connection.

**4. Run the app**
```bash
streamlit run frontend/app.py
```

---

## requirements.txt

```
psycopg2-binary
pandas
python-dotenv
streamlit
plotly
sqlalchemy
```

---

## Key Concepts Implemented

- Normalized relational database design (3NF)
- Foreign key constraints and referential integrity
- Junction tables for many-to-many relationships
- Composite unique constraints
- Parameterized queries (SQL injection prevention)
- Error handling with rollback on constraint violations
- SQLAlchemy engine for Pandas integration
- Environment variable based credential management
- Cloud PostgreSQL with Supabase (Mumbai region)

---

## What I Learned

- Designing multi-table relational databases from scratch
- Writing complex SQL queries with JOINs and aggregations
- Connecting Python to PostgreSQL using psycopg2
- Reading database data into Pandas DataFrames
- Building interactive dashboards with Streamlit and Plotly
- Deploying PostgreSQL to cloud using Supabase
- Production practices — environment variables, error handling, rollback

---

## Author

Built by ***SHAURYA GUPTA*** — 2nd Year AIML Student
Part of PostgreSQL learning journey from SQLite to cloud-hosted production database.
