# Crypto Price Analytics Platform

This project is a full-stack, containerized application that scrapes historical cryptocurrency price data (such as Bitcoin), stores it in a PostgreSQL database, performs data cleaning and analysis with pandas, visualizes the results with matplotlib, and provides both web and desktop graphical interfaces for exploration and export.

## Features

- **Web Scraping:** Collects historical crypto price data from public sources.
- **Database Storage:** Uses PostgreSQL to persist all collected data.
- **FastAPI Backend:** Exposes RESTful API endpoints for raw data, cleaned/analysed data, and image plots.
- **Data Cleaning & Analysis:** Cleans and processes data with pandas (e.g., removes missing values, computes rolling averages, descriptive stats).
- **Visualization:** Generates and serves matplotlib plots (e.g., price over time, rolling mean).
- **Export:** CSV export of dataset.
- **Web Frontend:** Simple web interface (React or any frontend framework) for visual exploration.
- **Kivy GUI:** Desktop application (Python/Kivy) for direct API interaction from a GUI.
- **Containerized:** Uses Docker and Docker Compose for easy deployment of all services.

## Architecture

```
[ Scraper ] --> [ FastAPI Backend ] <--> [ PostgreSQL ]
          |             |                  |
          |             v                  |
          |        [ Kivy GUI ]            |
          |             |                  |
          |         [ Web Frontend ] <-----+
```

## API Endpoints

- `POST /scrape/` — Trigger web scraping and store data.
- `GET /raw/` — Get all raw price data from the database.
- `GET /analysed/` — Get cleaned, analysed data and descriptive statistics.
- `GET /plot/` — Get a matplotlib plot (PNG) showing cleaned data and rolling averages.
- `GET /export/csv/` — Download all data as CSV.

## Quickstart

### 1. Clone and Configure

```bash
git clone <your-repo-url>
cd project-root
```

Edit environment variables in `docker-compose.yml` as needed (database user, password, etc).

### 2. Build and Run

```bash
docker compose up --build
```

### 3. Services

- **Backend API:** [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
- **Frontend:** [http://localhost:3000](http://localhost:3000)
- **Kivy GUI:** Run inside the backend container (see below).

### 4. Kivy GUI Usage

To launch the Kivy GUI (requires X11/VNC if using Docker):

```bash
docker exec -it <backend-container-name> python backend/kivy_gui/app.py
```

Or, run the Kivy app locally by copying `backend/kivy_gui` to your desktop machine and running:

```bash
pip install kivy requests
python app.py
```

## Example Workflow

1. `POST /scrape/`: Collect historical price data.
2. `GET /raw/`: See raw database records.
3. `GET /analysed/`: View cleaned data and statistics (e.g., mean, min, max, rolling average).
4. `GET /plot/`: Download a chart of the cleaned and analysed data.
5. `GET /export/csv/`: Download the full dataset as CSV.

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, pandas, matplotlib, requests, BeautifulSoup4
- **Database:** PostgreSQL
- **Web Frontend:** React (can be replaced with any SPA)
- **Desktop GUI:** Kivy (Python)
- **Containerization:** Docker, Docker Compose

## Customization

- Change the scraping logic in `scraper.py` to target any cryptocurrency or data source.
- Extend data analysis with more complex pandas operations or new visualizations in matplotlib.
- Swap out the frontend for your preferred framework.

## Author

Student project for Wahid Hamdi

---

**Note:** For Kivy GUI usage inside Docker, ensure your host supports X11 or use a VNC setup. Otherwise, run the Kivy desktop client on your local machine.
