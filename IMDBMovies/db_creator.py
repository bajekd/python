import sqlite3
import pathlib


class DbCreator:
    def __init__(self, db_path):
        self.db_path = pathlib.Path(db_path)

    def create_db(self):
        """Create sqlite db file in given location (path pass in constructor). Raise exception if in given
        path already exist some file. Beware - to work properly there need to exist ./database/ folder"""
        if self.db_path.is_file():
            full_path = self.db_path.resolve()
            raise Exception(f"In given path ({full_path}) some file already exists!")

        connection = sqlite3.connect(self.db_path)
        cur = connection.cursor()

        cur.execute(
            """CREATE table movies(
            id integer PRIMARY KEY,
            title text UNIQUE,
            year integer,
            runtime integer,
            genre text,
            director text,
            actors text,
            writer text,
            language text,
            country text,
            awards text,
            imdb_rating float,
            imdb_votes integer,
            box_office integer
        )"""
        )

        connection.commit()
        connection.close()
        print(
            f"Database in path: 'database/movies.db' has been created! Please read project ReadMe.md in order to learn avaible commands."
        )
