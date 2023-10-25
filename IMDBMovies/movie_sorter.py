import sqlite3
import re


class MovieSorter:
    @staticmethod
    def sort_by(db_path, sort_criteria):
        """Returns sorted (by given criteria) list of movies (list of tuples - each tuple is record from db).
        Raises exception with appropriate message if soft_criteria is not valid."""

        connection = sqlite3.connect(db_path)
        cur = connection.cursor()

        # Manual validate sort_criteria - input provide by user // why not automatic validate? ->
        # https://stackoverflow.com/questions/42313051/python-sqlite3-execute-falied-when-using-placeholder-in-order-by
        # meta_group_1 (one occurrence, mandatory), meta_group_2 (up to 13 occurrences, optional) -> 14 tables in db
        pattern = re.compile(r'''
                    ( ([a-z_]{1,13})            # column name, meta_group_2 (optional)
                    (\s[acdes]{3,4})?           # asc/desc (optional), meta_group_2 (optional)
                    (,\s) ){,13}                # separator, meta_group_2 (optional),
                    ( ([a-z_]{1,13})            # column name, meta_group_1
                    (\s[acdes]{3,4})? )         # asc/desc (optional), meta_group_1 
                  ''', re.VERBOSE)
        if pattern.fullmatch(sort_criteria):
            query = f'''SELECT id, title, ifnull(year, 'N/A'), ifnull(runtime, 'N/A'), ifnull(genre, 'N/A'),
                            ifnull(director, 'N/A'), ifnull(actors, 'N/A'), ifnull(writer, 'N/A'), ifnull(language, 'N/A'),
                            ifnull(country, 'N/A'), ifnull(awards, 'N/A'), ifnull(imdb_rating, 'N/A'), ifnull(imdb_votes, 'N/A'),
                            ifnull(box_office, 'N/A') FROM movies  ORDER BY {sort_criteria};'''
            cur.execute(query)
            result = cur.fetchall()
        else:
            raise Exception(f'Given sort_by() argument ({sort_criteria}) is illegal!')

        connection.close()

        return result
