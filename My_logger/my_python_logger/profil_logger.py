from datetime import datetime
from typing import List

from .handlers import Handler
from .log_entry import LogEntry


class ProfilLogger:
    def __init__(self, handlers: List[Handler]) -> None:
        self._handlers = handlers
        self._log_level = "WARNING"

    @property
    def handlers(self) -> List[Handler]:
        return self._handlers

    @handlers.setter
    def handlers(self, handlers: List[Handler]) -> None:
        self._handlers = handlers

    def _is_log_to_save(self, log_entry_level: str, min_log_level_to_save: str) -> bool:
        TRANSLATION_TABLE = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}

        min_log_level_to_save = TRANSLATION_TABLE.get(min_log_level_to_save, 100)
        log_entry_level = TRANSLATION_TABLE.get(log_entry_level, 0)

        return log_entry_level >= min_log_level_to_save

    def _validate_log_level(self, level: str) -> None:
        possible_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if level not in possible_log_levels:
            raise ValueError(
                f"Given log level -> {level} is not permitted to use!"
                f" Avaible options are: 'DEBUG', 'INFO', 'WARNING', 'ERROR' or 'CRITICAL'"
            )

    def _save(self, level: str, msg: str) -> None:
        if self._is_log_to_save(level, self._log_level):
            log_entry = LogEntry(self._get_current_date(), level, msg)

            for handler in self.handlers:
                handler.save_data_to_file(log_entry)

    def _get_current_date(self) -> datetime:
        current_date = datetime.now()

        return current_date.strftime("%Y-%m-%d %H:%M:%S")

    def set_log_level(self, level: str) -> None:
        level = level.upper()
        self._validate_log_level(self, level)
        self._log_level = level

    def debug(self, msg: str) -> None:
        level = "DEBUG"
        self._save(level, msg)

    def info(self, msg: str) -> None:
        level = "INFO"
        self._save(level, msg)

    def warning(self, msg: str) -> None:
        level = "WARNING"
        self._save(level, msg)

    def error(self, msg: str) -> None:
        level = "ERROR"
        self._save(level, msg)

    def critical(self, msg: str) -> None:
        level = "CRITICAL"
        self._save(level, msg)
