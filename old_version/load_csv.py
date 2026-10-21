
import csv
import psycopg
from getpass import getpass

password = getpass("Mot de passe PostgreSQL : ")

with psycopg.connect(
    host="localhost",
    dbname="weather_db",
    user="weather_user",
    password=password
) as conn:

    with conn.cursor() as cur:

        with open(
            "weather_belgium.csv",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                cur.execute(
                    """
                    INSERT INTO weather_observations
                    (city, observed_at,
                     temperature_c, precipitation_mm)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (city, observed_at)
                    DO UPDATE SET
                        temperature_c = EXCLUDED.temperature_c,
                        precipitation_mm = EXCLUDED.precipitation_mm
                    """,
                    (
                        row["city"],
                        row["datetime"],
                        row["temperature"],
                        row["precipitation"] or None
                    )
                )

    conn.commit()

print("Chargement terminé !")
