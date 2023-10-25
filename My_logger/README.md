### How to use it:
* Make sure, you have all dependencies requirements --> you can use `Pipfil`.
* For pipenv users just type `pipenv install`

     
### Available classes:
1. LogEntry class -> LogEntry(date: datetime, level: str, msg: str)
  * This class is not inted to use by user. It is internally uses by ProfillLoger and ProfilLoggerReader classes.
    
2. JSONHandler(file_path: str) class, CSVHandler(file_path: str) class, SQLLiteHandler(file_path: str) class and FileHandler(file_path: str) class
  * All 4 classes implements ABC class Handler
  * They are responsible for create specified file, save given data to file and for retrive data from file.
  * From User point of view only concern is decided to which file he wants to save/retrive data and initialize choosen class/-es

  ```
  from my_python_logger.handlers import JSONHandler, CSVHandler, SQLLiteHandler, FileHandler
  
  json_handler = JSONHandler("logs.json")
  csv_handler = CSVHandler("logs.csv")
  sql_handler = SQLLiteHandler("logs.sqllite")
  file_handler = FileHandler("logs.txt")
  ```
  
3. ProfilLogger(handlers: List[Handler]) class
  * "Main" class responsible for creating logs. Implements internally logic for creating LogEntry objects, saving them to proper files and also determined minimal log level (like in standard python logger there are 5 log levels: 
      * "DEBUG"
      * "INFO"
      * "WARNING"
      * "ERROR"
      * "CRITICAL"
  * Followed methods are intended to be used by User:
    * when initialize class User should pass List of Handlers to specify to which file formats logs will be saved (see previous point about Handlers classes)
    * set_log_level(level: str)
      * By default ProfilLogger set "WARNING" level.
      * You can choose only from listed above 5 log level. Typing anything else will result rasing TypeError.
    * debug(msg: str) --> save to file log with "DEBUG" level
    * info(msg: str) --> save to file log with "INFO" level
    * warning(msg: str) --> save to file log with "WARNING" level
    * error(msg: str) --> save to file log with "ERROR" level
    * critical(msg: str) --> save to file log with "CRITICAL" level

```
  from my_python_logger.profil_logger import ProfilLogger
  
  logger = ProfilLogger([json_handler, csv_handler, sql_handler, file_handler])
  logger.set_log_level("INFO") # Pass arg different than "debug", "info", "warning", "error", "critical" 
  # will result raising TypeError (passing arg is automatically .upper() before checking)
  
  logger.info("Some info message")
  logger.warning("Some warning message")
  logger.debug("Some debug message")
  logger.critical("Some critical message")
  logger.error("Some error message")
  
  # In this case 4 from these message will be saved to: logs.json, logs.csv, logs.sqllite and logs.txt files --> 
  # debug message will be ignored due to to low log level"
```

4. ProfilLoggerReader(handler: Handler) class
     * class responsible for filtred via logs.
     * Followed methods are intended to be used by User:
          * when initialize class User should pass Handler to specify from which file format logs will be read (see 2. about Handlers classes)
          * find_by_text(text: str, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> List[LogEntry]
               * return list of LogEntries that contains given message and fulfil date constraints.
          * find_by_regex(regex: str, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> List[LogEntry]
               * return list of LogEntries that match to given regex and fulfil date constraints.
          * groupby_level(start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> Dict[str, List[LogEntry]]
               * return dict of log_levels as key and list with LogEntries as values which fulfil given date constraints.
          * groupby_month(start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> Dict[str, List[LogEntry]]
               * return dict of months as key and list with LogEntries as values which fulfil given date constraints.

```
  from my_python_logger.profil_logger_reader import ProfilLoggerReader
  from datetime import datetime
  
  logger_reader = ProfilLoggerReader(handler=json_handler)
  
  start_date = datetime(2021, 6, 19, 23, 55)
  end_date = datetime(2021, 7, 21, 22, 25)
  
  found_by_text = logger_reader.find_by_text("message", start_date=start_date)
  found_by_regex = logger_reader.find_by_regex("\w{3} message", end_date=end_date)
  grouped_by_level = logger_reader.groupby_level(start_date, end_date)
  grouped_by_month = logger_reader.groupby_month()
```
         

