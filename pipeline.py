
from src.extract import extract
from src.transform import transform
from src.load import load


def main():
    print("=== Démarrage du pipeline ETL ===")

    raw_data = extract()

    observations = transform(raw_data)

    load(observations)

    print("=== Pipeline ETL terminé ===")


if __name__ == "__main__":
    main()
