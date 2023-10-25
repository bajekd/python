from datetime import datetime


class LogEntry:
    def __init__(self, date: datetime, level: str, msg: str) -> None:
        self.date = date
        self.level = level
        self.msg = msg

    def __str__(self) -> str:
        return (
            f"Entry log: date: {datetime.strftime(self.date, '%Y-%m-%d %H:%M:%S')}, "
            f"level: {self.level}, "
            f"msg: {self.msg}"
        )
