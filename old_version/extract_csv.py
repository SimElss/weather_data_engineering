

import csv
import requests

URL = "https://archive-api.open-meteo.com/v1/archive"

cities = {
    "Namur": (50.4674, 4.8720),
    "Bruxelles": (50.8503, 4.3517),
    "Liege": (50.6326, 5.5797)
}

with open("weather_belgium.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "city",
        "datetime",
        "temperature",
        "precipitation"
    ])

    for city, (latitude, longitude) in cities.items():

        print("============= \n")

        print(f"Extraction pour {city}...")

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": "2026-10-01",
            "end_date": "2026-10-07",
            "hourly": "temperature_2m,precipitation",
            "timezone": "Europe/Brussels"
        }

        response = requests.get(
            URL,
            params=params,
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        hourly = data["hourly"]
        count = 0
        temperatures = []

        missing = 0

        for dt, temp, rain in zip(
            hourly["time"],
            hourly["temperature_2m"],
            hourly["precipitation"],
            strict=True
        ):

            if temp is None:
                missing += 1
                continue


            temperatures.append(temp)

            writer.writerow([
                city,
                dt,
                temp,
                rain
            ])

            count += 1



        print(f"{city}: {count} lignes enregistrées")
        print(f"Températures manquantes: {missing}")



        if temperatures:
            moyenne = sum(temperatures) / len(temperatures)
            minimum = min(temperatures)
            maximum = max(temperatures)

            print(f"Ville : {city}")
            print(f"Température moyenne : {moyenne:.2f} °C")
            print(f"Température minimale : {minimum:.2f} °C")
            print(f"Température maximale : {maximum:.2f} °C")
        else:
            print(f"Aucune température disponible pour {city}")
    

print("\nPipeline terminé !")