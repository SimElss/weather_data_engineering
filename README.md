# Weather Data Engineering Pipeline

A simple ETL pipeline built with Python and PostgreSQL.

## Project

This project collects historical weather data for three Belgian cities (Namur, Brussels and Liège) using the Open-Meteo API.

The pipeline follows three steps:

1. **Extract** weather data from the API.
2. **Transform** the data into structured observations.
3. **Load** the observations into PostgreSQL.

The database uses UPSERT to avoid duplicate records.

## Technologies

- Python
- Open-Meteo API
- PostgreSQL
- SQL
- Git

## Database (PostgreSQL)

The project uses a PostgreSQL database named weather_db.

The SQL script sql/schema.sql creates the weather_observations table, which stores:

City

Observation date and time

Temperature (°C)

Precipitation (mm)

To create the table, first create the database and a user with the required permissions, then run:

psql -h localhost -U weather_user -d weather_db -f sql/schema.sql

A unique constraint on (city, observed_at) prevents duplicate observations.

## Run the project

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the PostgreSQL database, then run:

```bash
python3 pipeline.py
```

## Next steps

- Add logging
- Add automated tests
- Use Docker
- Automate the pipeline