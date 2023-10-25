import copy
import re
from datetime import datetime
from typing import Dict, List, Optional

from .handlers import Handler
from .log_entry import LogEntry


class ProfilLoggerReader:
    def __init__(self, handler: Handler) -> None:
        self._handler = handler
        self._data = self._transform_data_to_log_entries(self._handler.retrive_data_from_file())

    def _transform_data_to_log_entries(self, file_data: List[dict[str, str, str, str, str, str]]):
        result = []

        for entry in file_data:
            date = datetime.strptime(entry["date"], "%Y-%m-%d %H:%M:%S")
            level = entry["level"]
            msg = entry["msg"]

            result.append(LogEntry(date, level, msg))

        return result

    def _validate_input_date(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> None:
        if start_date and end_date:
            if not isinstance(start_date, datetime):
                raise TypeError(f"start_date must be a datetime object! --> is {type(start_date)}")
            if not isinstance(end_date, datetime):
                raise TypeError(f"end_date must be a datetime object! --> is {type(end_date)}")

            if start_date > end_date:
                raise TypeError("Given start_date is after end_date!")
            if end_date < start_date:
                raise TypeError("Given end_date is before start_date!")

        elif start_date:
            if not isinstance(start_date, datetime):
                raise TypeError(f"start_date must be a datetime object! --> is {type(start_date)}")

        elif end_date:
            if not isinstance(end_date, datetime):
                raise TypeError(f"end_date must be a datetime object! --> is {type(end_date)}")

        else:
            pass

    def _filter_by_date(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> List[dict[str, str, str, str, str, str]]:
        self._validate_input_date(start_date, end_date)
        result = []

        if start_date and end_date:
            for entry_log in self._data:
                if start_date <= entry_log.date <= end_date:
                    result.append(entry_log)

            return result

        elif start_date:
            for entry_log in self._data:
                if entry_log.date >= start_date:
                    result.append(entry_log)

            return result

        elif end_date:
            for entry_log in self._data:
                if entry_log.date <= end_date:
                    result.append(entry_log)

            return result

        else:
            result = copy.deepcopy(self._data)
            return result

    def find_by_text(
        self, text: str, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> List[LogEntry]:
        result = []
        logs_filtred_by_date = self._filter_by_date(start_date, end_date)

        for entry_log in logs_filtred_by_date:
            if text in entry_log.msg:
                result.append(entry_log)

        return result

    def find_by_regex(
        self, regex: str, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> List[LogEntry]:
        result = []
        logs_filtred_by_date = self._filter_by_date(start_date, end_date)
        pattern = regex

        for entry_log in logs_filtred_by_date:
            if re.search(pattern, entry_log.msg, flags=re.I):
                result.append(entry_log)

        return result

    def groupby_level(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, List[LogEntry]]:
        data_filtred_by_date = self._filter_by_date(start_date, end_date)
        result = {"DEBUG": [], "INFO": [], "WARNING": [], "ERROR": [], "CRITICAL": []}

        for entry_log in data_filtred_by_date:
            result[entry_log.level].append(entry_log)

        return result

    def groupby_month(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, List[LogEntry]]:
        data_filtred_by_date = self._filter_by_date(start_date, end_date)
        result = {
            "January": [],
            "February": [],
            "March": [],
            "April": [],
            "May": [],
            "June": [],
            "July": [],
            "August": [],
            "September": [],
            "October": [],
            "November": [],
            "December": [],
        }

        for entry_log in data_filtred_by_date:
            current_month = entry_log.date.strftime("%B")
            result[current_month].append(entry_log)

        return result
