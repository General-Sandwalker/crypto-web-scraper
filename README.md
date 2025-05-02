# Crypto Web Scraper

A full-stack application for scraping, analyzing, and visualizing cryptocurrency price data.

## Features

- Web scraping of historical cryptocurrency prices (BTC, ETH, XMR)
- Persistent storage in PostgreSQL database
- RESTful API for accessing and manipulating data
- Interactive data visualization with Chart.js
- Modern responsive UI built with TailwindCSS

## Tech Stack

### Backend
- Python FastAPI
- SQLAlchemy ORM
- PostgreSQL database
- Beautiful Soup for web scraping
- Pandas for data manipulation
- Matplotlib for image generation

### Frontend
- Node.js with Express
- TailwindCSS for styling
- Chart.js for interactive charts
- Alpine.js for reactivity

## Project Structure

```
crypto-web-scraper/
├── backend/                  # Python FastAPI backend
│   ├── app/
│   │   ├── crud/             # Database operations
│   │   ├── models/           # SQLAlchemy models
│   │   ├── routes/           # API endpoints
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic
│   │   ├── db.py             # Database connection
│   │   └── main.py           # FastAPI application
│   ├── Dockerfile            # Backend Docker config
│   └── requirements.txt      # Python dependencies
├── frontend/                 # Node.js frontend
│   ├── public/               # Static assets
│   │   ├── css/              # Stylesheets
│   │   ├── js/               # JavaScript files
│   │   └── index.html        # Main HTML file
│   ├── index.mjs             # Express server
│   ├── package.json          # Node.js dependencies
│   └── Dockerfile            # 
└── docker-compose.yaml       # Docker Compose config
```

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js (for local development)
- Python 3.12 (for local development)

### Running the Application

1. Start the application using Docker Compose:
   ```bash
   docker-compose up
   ```

2. Access the frontend at:
   ```
   http://localhost:3000
   ```

3. Access the backend API at:
   ```
   http://localhost:8000
   ```

### Running Locally (Development)

#### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `GET /coins/` - List supported cryptocurrencies
- `POST /scrape/` - Trigger web scraping for new data
- `GET /raw/` - Get raw price data with filters
- `GET /export/csv/` - Export price data as CSV
- `GET /plot/` - Generate price chart image

## License

This project is licensed under the MIT License - see the LICENSE file for details.