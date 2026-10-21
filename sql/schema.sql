CREATE TABLE IF NOT EXISTS weather_observations (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    observed_at TIMESTAMP NOT NULL,
    temperature_c DOUBLE PRECISION NOT NULL,
    precipitation_mm DOUBLE PRECISION,
    UNIQUE (city, observed_at)
);