import csv
from pathlib import Path


class CsvReader:

    @staticmethod
    def read(file_path: str) -> list[dict]:

        with Path(file_path).open(
            mode="r",
            encoding="utf-8",
            newline=""
        ) as file:

            return list(csv.DictReader(file))