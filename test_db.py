
import psycopg
from getpass import getpass

password = getpass("Mot de passe PostgreSQL : ")

try:
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="weather_db",
        user="weather_user",
        password=password
    ) as conn:

        print("Connexion PostgreSQL réussie !")

        with conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) FROM weather_observations;"
            )

            resultat = cur.fetchone()
            print("Nombre d'observations :", resultat[0])


except psycopg.Error as error:
    print("Erreur PostgreSQL :", error)
