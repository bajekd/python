import csv
import json
import os
import sqlite3
from abc import ABC, abstractmethod
from typing import List

from .log_entry import LogEntry


class Handler(ABC):
    @abstractmethod
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._file_exists = self._check_if_file_already_exists()

    def _check_if_file_already_exists(self) -> bool:
        return os.path.isfile(self._file_path)

    @abstractmethod
    def save_data_to_file(self, log_entry: LogEntry) -> None:
        pass

    @abstractmethod
    def retrive_data_from_file(self) -> List[dict[str, str, str, str, str, str]]:
        pass


class JSONHandler(Handler):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        if not self._file_exists:
            with open(self._file_path, "w") as json_file:
                file_data = []
                json.dump(file_data, json_file)

    def save_data_to_file(self, log_entry: LogEntry) -> None:
        with open(self._file_path, "r") as json_file:
            file_data = json.load(json_file)

        with open(self._file_path, "w") as json_file:
            file_data.append({"date": log_entry.date, "level": log_entry.level, "msg": log_entry.msg})
            json.dump(file_data, json_file, indent=2)

    def retrive_data_from_file(self) -> List[dict[str, str, str, str, str, str]]:
        with open(self._file_path, "r") as json_file:
            file_data = json.load(json_file)

        return file_data


class CSVHandler(Handler):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
        self.header_names = ["date", "level", "msg"]

        if not self._file_exists:
            with open(self._file_path, "w") as csv_file:
                writer = csv.DictWriter(csv_file, self.header_names)
                writer.writeheader()

    def save_data_to_file(self, log_entry: LogEntry) -> None:
        with open(self._file_path, "a") as csv_file:
            writer = csv.DictWriter(csv_file, self.header_names)
            writer.writerow({"date": log_entry.date, "level": log_entry.level, "msg": log_entry.msg})

    def retrive_data_from_file(self) -> List[dict[str, str, str, str, str, str]]:
        result = []

        with open(self._file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                result.append(row)

        return result


class SQLLiteHandler(Handler):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        if not self._file_exists:
            connection = sqlite3.connect(self._file_path)
            cur = connection.cursor()
            cur.execute("""CREATE table logs(id integer PRIMARY KEY, data text, level text, msg text)""")
            connection.commit()
            connection.close()

    def save_data_to_file(self, log_entry: LogEntry) -> None:
        connection = sqlite3.connect(self._file_path)
        cur = connection.cursor()
        cur.execute(
            """ INSERT INTO logs (data, level, msg) VALUES(:data, :level, :msg);""",
            {
                "data": log_entry.date,
                "level": log_entry.level,
                "msg": log_entry.msg,
            },
        )
        connection.commit()
        connection.close()

    def retrive_data_from_file(self) -> List[dict[str, str, str, str, str, str]]:
        result = []

        connection = sqlite3.connect(self._file_path)
        cur = connection.cursor()
        cur.execute("SELECT * FROM logs")

        rows = cur.fetchall()  # [(1, '2021-07-05 14:37:32', 'INFO', 'Some info message'), ...]

        for row in rows:
            entry = {}
            entry["date"] = row[1]
            entry["level"] = row[2]
            entry["msg"] = row[3]

            result.append(entry)

        return result


class FileHandler(Handler):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def save_data_to_file(self, log_entry: LogEntry) -> None:
        with open(self._file_path, "a") as text_file:
            text_file.write(f"Date: {log_entry.date}, Level: {log_entry.level}, Msg: {log_entry.msg}\n")

    def retrive_data_from_file(self) -> List[dict[str, str, str, str, str, str]]:
        result = []

        with open(self._file_path, "r") as text_file:
            for line in text_file:
                entry = {}

                line = line.split(",")
                date = line[0].split(": ")[1]
                level = line[1].split(": ")[1]
                msg = line[2].split(": ")[1].replace("\n", "")

                entry["date"] = date
                entry["level"] = level
                entry["msg"] = msg

                result.append(entry)

        return result
