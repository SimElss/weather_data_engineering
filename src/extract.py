
import requests

URL = "https://archive-api.open-meteo.com/v1/archive"

CITIES = {
    "Namur": (50.4674, 4.8720),
    "Bruxelles": (50.8503, 4.3517),
    "Liege": (50.6326, 5.5797),
}

def extract():
    """Récupère les données météo brutes depuis Open-Meteo."""
    results = {}

    for city, (latitude, longitude) in CITIES.items():
        print(f"Extraction pour {city}...")

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": "2026-10-01",
            "end_date": "2026-10-07",
            "hourly": "temperature_2m,precipitation",
            "timezone": "Europe/Brussels",
        }

        response = requests.get(
            URL,
            params=params,
            timeout=30,
        )
        response.raise_for_status()

        results[city] = response.json()

    return results


if __name__ == "__main__":
    data = extract()
    print(f"Extraction terminée : {len(data)} villes.")