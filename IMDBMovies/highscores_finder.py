import sqlite3


class HighscoresFinder:
    @staticmethod
    def highscores(db_path):
        """Returns list of higscroes movies (list of tuples) - one from each of 4 predefined categories """
        highscores_result = []

        connection = sqlite3.connect(db_path)
        cur = connection.cursor()

        # Searching for highest runtime
        cur.execute(
            """SELECT id, title, ifnull(year, 'N/A'), ifnull(runtime, 'N/A'), ifnull(genre, 'N/A'),
                    ifnull(director, 'N/A'), ifnull(actors, 'N/A'), ifnull(writer, 'N/A'), ifnull(language, 'N/A'),
                    ifnull(country, 'N/A'), ifnull(awards, 'N/A'), ifnull(imdb_rating, 'N/A'),
                    ifnull(imdb_votes, 'N/A'), ifnull(box_office, 'N/A') FROM movies WHERE runtime = 
                    (SELECT MAX(runtime) from movies);"""
        )
        highest_runtime = cur.fetchone()
        highscores_result.append(highest_runtime)
        '''
        # Searching for highest earnings
        cur.execute(
            """SELECT id, title, ifnull(year, 'N/A'), ifnull(runtime, 'N/A'), ifnull(genre, 'N/A'),
                    ifnull(director, 'N/A'), ifnull(actors, 'N/A'), ifnull(writer, 'N/A'), ifnull(language, 'N/A'),
                    ifnull(country, 'N/A'), ifnull(awards, 'N/A'), ifnull(imdb_rating, 'N/A'),
                    ifnull(imdb_votes, 'N/A'), ifnull(box_office, 'N/A') FROM movies WHERE box_office = 
                    (SELECT MAX(box_office) from movies);"""
        )
        highest_earnings = cur.fetchone()
        highscores_result.append(highest_earnings)
        '''
        # Searching for most Oscars won
        cur.execute(
            """SELECT ifnull(awards, 'N/A') FROM movies WHERE awards GLOB 'Won *Oscars.*';"""
        )
        awards_records_as_tuples_list = cur.fetchall()
        awards_records = []
        for awards_records_as_tuples in awards_records_as_tuples_list:
            awards_records.append(awards_records_as_tuples[0])
        most_oscars_won = max(
            [int(sentence.split(" ", 2)[1]) for sentence in awards_records]
        )
        query = f"""SELECT id, title, ifnull(year, 'N/A'), ifnull(runtime, 'N/A'), ifnull(genre, 'N/A'),
                ifnull(director, 'N/A'), ifnull(actors, 'N/A'), ifnull(writer, 'N/A'), ifnull(language, 'N/A'),
                ifnull(country, 'N/A'), ifnull(awards, 'N/A'), ifnull(imdb_rating, 'N/A'), ifnull(imdb_votes, 'N/A'),
                ifnull(box_office, 'N/A') FROM movies WHERE awards GLOB 'Won {most_oscars_won} Oscars*';"""
        cur.execute(query)
        movie_most_oscars = cur.fetchone()
        highscores_result.append(movie_most_oscars)

        # Searching for highest imdb_rating
        cur.execute(
            """SELECT id, title, ifnull(year, 'N/A'), ifnull(runtime, 'N/A'), ifnull(genre, 'N/A'),
                    ifnull(director, 'N/A'), ifnull(actors, 'N/A'), ifnull(writer, 'N/A'), ifnull(language, 'N/A'),
                    ifnull(country, 'N/A'), ifnull(awards, 'N/A'), ifnull(imdb_rating, 'N/A'),
                    ifnull(imdb_votes, 'N/A'), ifnull(box_office, 'N/A') FROM movies WHERE imdb_rating = 
                    (SELECT MAX(imdb_rating) from movies);"""
        )
        highest_imdb_rating = cur.fetchone()
        highscores_result.append(highest_imdb_rating)

        connection.close()
        return highscores_result
