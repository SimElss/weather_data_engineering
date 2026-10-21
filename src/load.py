
import os

import psycopg
from dotenv import load_dotenv


load_dotenv()


def load(observations):
    """Insère ou met à jour les observations dans PostgreSQL."""

    query = """
        INSERT INTO weather_observations
            (city, observed_at, temperature_c, precipitation_mm)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (city, observed_at)
        DO UPDATE SET
            temperature_c = EXCLUDED.temperature_c,
            precipitation_mm = EXCLUDED.precipitation_mm
    """

    with psycopg.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    ) as conn:

        with conn.cursor() as cur:
            for observation in observations:
                cur.execute(
                    query,
                    (
                        observation["city"],
                        observation["observed_at"],
                        observation["temperature_c"],
                        observation["precipitation_mm"],
                    ),
                )

    print(f"Chargement terminé : {len(observations)} observations traitées.")
