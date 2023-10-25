import sqlite3
import re


class MovieFilter:
    @staticmethod
    def filter_by(db_path, condition):
        """"Returns filtered (by given criteria) list of movies (list of tuples - each tuple is record from db).
         Raises exception with appropriate message if soft_criteria is not valid."""
        connection = sqlite3.connect(db_path)
        cur = connection.cursor()

        # Validate columns - input provide by user // why not automatic validate? ->
        # https://stackoverflow.com/questions/42313051/python-sqlite3-execute-falied-when-using-placeholder-in-order-by
        # meta_group_1 (one occurrence, mandatory), meta_group_2 (up to 13 occurrences, optional) -> 14 tables in db
        pattern = re.compile(r'''
                    ( ([a-z_]{1,13})                     # column_name, meta-group_2 (optional)
                    (\s[<>!=]{1,2}\s|\sLIKE\s)           # operator\-s, meta-group_2 (optional)
                    ([a-zA-Z0-9%_']{1,15})               # value, meta-group_2 (optional)
                    (\sAND\s|\sOR\s) ){0,13}             # AND | OR, meta-group_2 (optional)
                    ([a-z_]{1,13})                       # column_name, meta-group_1
                    (\s[<>=!]{1,2}\s|\sLIKE\s)           # operator\-s, meta-group_1
                    ([a-zA-Z0-9%_']{1,15})               # value, meta-group_1
                  ''', re.X)
        if pattern.fullmatch(condition):
            query = f'''SELECT id, title, ifnull(year, 'N/A'), ifnull(runtime, 'N/A'), ifnull(genre, 'N/A'),
                    ifnull(director, 'N/A'), ifnull(actors, 'N/A'), ifnull(writer, 'N/A'), ifnull(language, 'N/A'),
                    ifnull(country, 'N/A'), ifnull(awards, 'N/A'), ifnull(imdb_rating, 'N/A'),
                    ifnull(imdb_votes, 'N/A'), ifnull(box_office, 'N/A') FROM movies WHERE {condition};'''
            cur.execute(query)
        else:
            raise Exception(f'Given filter_by() argument ( {condition} ) is illegal!')

        result = cur.fetchall()

        connection.close()

        return result


