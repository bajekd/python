import time
from datetime import datetime

from my_python_logger.handlers import CSVHandler, FileHandler, JSONHandler, SQLLiteHandler
from my_python_logger.profil_logger import ProfilLogger
from my_python_logger.profil_logger_reader import ProfilLoggerReader

json_handler = JSONHandler("logs.json")
csv_handler = CSVHandler("logs.csv")
sql_handler = SQLLiteHandler("logs.sqlite")
file_handler = FileHandler("logs.txt")

logger = ProfilLogger(handlers=[json_handler, csv_handler, sql_handler, file_handler])
logger.set_log_level("WARNING")

for _ in range(30):
    logger.debug("Some debug message")
    logger.info("Some info message")
    logger.warning("Some warning message")
    logger.error("Some error message")
    logger.critical("Some critical message")
    time.sleep(1)
    # The logs are stores in logs.json, logs.csv, logs.sqlite and logs.txt

log_readers = {
    "json_handler": ProfilLoggerReader(handler=json_handler),
    "csv_handler": ProfilLoggerReader(handler=csv_handler),
    "sql_handler": ProfilLoggerReader(handler=sql_handler),
    "file_handler": ProfilLoggerReader(handler=file_handler),
}

found_by_text = {"json_handler": None, "csv_handler": None, "sql_handler": None, "file_handler": None}
found_by_regex = {"json_handler": None, "csv_handler": None, "sql_handler": None, "file_handler": None}
grouped_by_level = {"json_handler": None, "csv_handler": None, "sql_handler": None, "file_handler": None}
grouped_by_month = {"json_handler": None, "csv_handler": None, "sql_handler": None, "file_handler": None}


start_date = datetime(2021, 6, 28, 13, 55)
end_date = datetime(2021, 7, 28, 15, 55)
for key in log_readers.keys():
    found_by_text[key] = log_readers[key].find_by_text("error message", start_date=start_date)
    found_by_regex[key] = log_readers[key].find_by_regex("[r,l]{1} message", end_date=end_date)
    grouped_by_level[key] = log_readers[key].groupby_level(start_date, end_date)
    grouped_by_month[key] = log_readers[key].groupby_month()
