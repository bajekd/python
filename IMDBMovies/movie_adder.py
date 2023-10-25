import sqlite3


class MovieAdder:
    @staticmethod
    def add_to_db(db_path, movie):
        """Insert given movie (instance of movie class) to database (by given db_path).
        Raises exception with appropriate message if movie already is in database"""

        connection = sqlite3.connect(db_path)
        cur = connection.cursor()

        # test_query to check if specified movie already exists in db
        cur.execute("SELECT title from movies WHERE title = :title;", {'title': movie.title})
        test_query = cur.fetchone()

        if test_query:
            raise Exception(f"Given movie ({movie.title}) already in database!")
        else:
            cur.execute(''' INSERT INTO movies (title, year, runtime, genre, director, actors, writer, language,
            country, awards, imdb_rating, imdb_votes, box_office) VALUES(:title, :year, :runtime, :genre,
            :director, :cast, :writer, :language, :country, :awards, :imdb_rating, :imdb_votes,:box_office);''',
                            {'title': movie.title, 'year': movie.year, 'runtime': movie.runtime, 'genre': movie.genre,
                             'director': movie.director, 'cast': movie.actors, 'writer': movie.writer,
                             'language': movie.language, 'country': movie.country, 'awards': movie.awards,
                             'imdb_rating': movie.imdb_rating, 'imdb_votes': movie.imdb_votes,
                             'box_office': movie.box_office})
            print(f"Data from movie - {movie.title} has been inserted to database")

        connection.commit()
        connection.close()

