
def transform(raw_data):
    """
    Transforme les réponses Open-Meteo en observations météo.

    Ignore les observations dont la température est absente.
    """
    observations = []

    for city, data in raw_data.items():
        hourly = data["hourly"]
        missing = 0

        for dt, temp, rain in zip(
            hourly["time"],
            hourly["temperature_2m"],
            hourly["precipitation"],
            strict=True,
        ):
            if temp is None:
                missing += 1
                continue

            observation = {
                "city": city,
                "observed_at": dt,
                "temperature_c": temp,
                "precipitation_mm": rain,
            }

            observations.append(observation)

        print(f"{city} : {missing} températures manquantes")

    return observations


if __name__ == "__main__":
    from src.extract import extract

    raw_data = extract()
    observations = transform(raw_data)

    print(f"\nTransformation terminée : {len(observations)} observations.")

    if observations:
        print("Première observation :", observations[0])
