import io
import json
import os
import re
import sqlite3
import unittest
import unittest.mock

from highscores_finder import HighscoresFinder
from movie_adder import MovieAdder
from movie_filter import MovieFilter
from movie import Movie
from movie_sorter import MovieSorter


class TestMovie(unittest.TestCase):
    def test_construct_movie_instance(self):
        movie_json = {"Title": "Test", "Year": "2001", "Rated": "PG-13", "Released": "19 Dec 2001",
                      "Runtime": "178 min", "Genre": "Test", "Director": "Test", "Writer": "Test", "Actors": "Test",
                      "Plot": '''A meek Hobbit from the Shire and eight companions set out on a journey to destroy the
                      powerful One Ring and save Middle-earth from the Dark Lord Sauron.''', "Language": "Test",
                      "Country": "Test", "Awards": "Test", "Poster": '''https://m.media-amazon.com/images/M/MV5BN2EyZjM3
                      NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SX300.jpg''', "Ratings":
                          [{"Source": "Internet Movie Database", "Value": "8.8/10"},
                           {"Source": "Rotten Tomatoes", "Value":
                               "91%"}, {"Source": "Metacritic", "Value": "92/100"}], "Metascore": "92",
                      "imdbRating": "8.8",
                      "imdbVotes": "1,545,049", "imdbID": "tt0120737", "Type": "movie", "DVD": "06 Aug 2002",
                      "BoxOffice": "$314,000,000", "Production": "New Line Cinema", "Website": "N/A", "Response":
                          "True"}

        movie = Movie(movie_json)

        self.assertEqual(movie.title, "Test")
        self.assertEqual(movie.year, 2001)
        self.assertEqual(movie.runtime, 178)
        self.assertEqual(movie.genre, "Test")
        self.assertEqual(movie.director, "Test")
        self.assertEqual(movie.actors, "Test")
        self.assertEqual(movie.writer, "Test")
        self.assertEqual(movie.language, "Test")
        self.assertEqual(movie.country, "Test")
        self.assertEqual(movie.awards, "Test")
        self.assertEqual(movie.imdb_rating, 8.8)
        self.assertEqual(movie.imdb_votes, 1545049)
        self.assertEqual(movie.box_office, 314000000)

    def test_construct_movie_instance_without_info(self):
        movie_json = {"Title": "N/A", "Year": "N/A", "Rated": "PG-13",
                      "Released": "19 Dec 2001", "Runtime": "N/A", "Genre": "N/A", "Director": "N/A", "Writer": "N/A",
                      "Actors": "N/A", "Plot": '''A meek Hobbit from the Shire and eight companions set out on a journey 
                             to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.''',
                      "Language":
                          "N/A", "Country": "N/A", "Awards": "N/A", "Poster": '''https://m.media-amazon.com/images/M/MV5BN2E
                             yZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SX300.jpg''',
                      "Ratings": [{"Source": "Internet Movie Database", "Value": "8.8/10"}, {"Source": '''Rotten Tomatoe
                             s''', "Value": "91%"}, {"Source": "Metacritic", "Value": "92/100"}], "Metascore": "92", '''imdbRat
                             ing''': "N/A", "imdbVotes": "N/A", "imdbID": "tt0120737", "Type": "movie",
                      "DVD": "06 Aug 2002",
                      "BoxOffice": "N/A", "Production": "New Line Cinema", "Website": "N/A", "Response": "True"}

        movie = Movie(movie_json)

        self.assertEqual(movie.title, "N/A")
        self.assertIsNone(movie.year, None)
        self.assertIsNone(movie.runtime, None)
        self.assertEqual(movie.genre, "N/A")
        self.assertEqual(movie.director, "N/A")
        self.assertEqual(movie.actors, "N/A")
        self.assertEqual(movie.writer, "N/A")
        self.assertEqual(movie.language, "N/A")
        self.assertEqual(movie.country, "N/A")
        self.assertEqual(movie.awards, "N/A")
        self.assertIsNone(movie.imdb_rating, None)
        self.assertIsNone(movie.imdb_votes, None)
        self.assertIsNone(movie.box_office, None)


class TestRegex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # meta_group_1 (one occurrence, mandatory), meta_group_2 (up to 13 occurrences, optional) -> 14 tables in db
        cls.pattern_sort = re.compile(r'''
                                  ( ([a-z_]{1,13})            # column name, meta_group_2 (optional)
                                  (\s[acdes]{3,4})?           # asc/desc (optional), meta_group_2 (optional)
                                  (,\s) ){,13}                # separator, meta_group_2 (optional),
                                  ( ([a-z_]{1,13})            # column name, meta_group_1
                                  (\s[acdes]{3,4})? )         # asc/desc (optional), meta_group_1 
                                ''', re.VERBOSE)
        cls.pattern_filter = re.compile(r'''
                                        ( ([a-z_]{1,13})                     # column_name, meta-group_2 (optional)
                                        (\s[<>!=]{1,2}\s|\sLIKE\s)           # operator\-s, meta-group_2 (optional)
                                        ([a-zA-Z0-9%_']{1,15})               # value, meta-group_2 (optional)
                                        (\sAND\s|\sOR\s) ){0,13}             # AND | OR, meta-group_2 (optional)
                                        ([a-z_]{1,13})                       # column_name, meta-group_1
                                        (\s[<>=!]{1,2}\s|\sLIKE\s)           # operator\-s, meta-group_1
                                        ([a-zA-Z0-9%_']{1,15})               # value, meta-group_1
                                      ''', re.VERBOSE)

    def test_movie_sorter_validator_match(self):
        self.assertTrue(self.pattern_sort.fullmatch('id desc') is not None)
        self.assertTrue(
            self.pattern_sort.fullmatch('id desc, title asc, year desc, genre, runtime desc, director desc, actors,'
                                        ' writer, language, country desc, awards, imdb_rating desc, imdb_votes desc,'
                                        ' box_office') is not None)

    def test_movie_sorter_validator_not_match(self):
        self.assertTrue(self.pattern_sort.fullmatch('') is None)
        self.assertTrue(self.pattern_sort.fullmatch('id desc,') is None)
        self.assertTrue(self.pattern_sort.fullmatch('id desc, title asc, year desc, genre, runtime desc, director desc,'
                                                    ' actors, writer, language, country desc, awards, imdb_rating desc,'
                                                    ' imdb_votes desc, box_office,') is None)

    def test_movie_filter_validator_match(self):
        self.assertTrue(self.pattern_filter.fullmatch('year >= 2012') is not None)
        self.assertTrue(self.pattern_filter.fullmatch("awards LIKE '%Oscars%'") is not None)
        self.assertTrue(self.pattern_filter.fullmatch('year >= 2012 AND runtime <= 160') is not None)
        self.assertTrue(self.pattern_filter.fullmatch("language LIKE '%Spanish%' AND actors LIKE '%Bale%'") is not None)

    def test_movie_filter_validator_not_match(self):
        self.assertTrue(self.pattern_filter.fullmatch('') is None)
        self.assertTrue(self.pattern_filter.fullmatch('year >= 2012 AND') is None)


class TestMovieFunctions(unittest.TestCase):
    def setUp(self):
        self.db_connection = sqlite3.connect('testing_db.db')
        self.cur = self.db_connection.cursor()

        self.cur.execute('''CREATE table movies(
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
                            )''')

        self.db_connection.commit()

        # populate testing db
        with open('movies_to_populate_testing_db.txt') as file:
            file_content = file.read()
            for movie_json in file_content.split('----------'):
                movie = Movie(json.loads(movie_json))
                MovieAdder.add_to_db('testing_db.db', movie)

    def tearDown(self):
        # closing connection and remove entire database file
        self.db_connection.close()
        os.remove('testing_db.db')

    def test_sort_by(self):
        movies = MovieSorter.sort_by('testing_db.db', "title, year desc, runtime desc")
        expected_result = [
            (3, 'Harry Potter and the Deathly Hallows: Part 2', 2011, 130, 'Adventure, Drama, Fantasy, Mystery', 'David Yates', 'Ralph Fiennes, Michael Gambon, Alan Rickman, Daniel Radcliffe', 'Steve Kloves (screenplay), J.K. Rowling (novel)', 'English', 'USA, UK', 'Nominated for 3 Oscars. Another 45 wins & 91 nominations.', 8.1, 708269, 381000185),
            (2, 'Star Wars: Episode IV - A New Hope', 1977, 121, 'Action, Adventure, Fantasy, Sci-Fi', 'George Lucas', 'Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing', 'George Lucas', 'English', 'USA', 'Won 6 Oscars. Another 50 wins & 28 nominations.', 8.6, 1143909, 'N/A'),
            (1, 'The Lord of the Rings: The Fellowship of the Ring', 2001, 178, 'Adventure, Drama, Fantasy', 'Peter Jackson', 'Alan Howard, Noel Appleby, Sean Astin, Sala Baker', 'J.R.R. Tolkien (novel), Fran Walsh (screenplay), Philippa Boyens (screenplay), Peter Jackson (screenplay)', 'English, Sindarin', 'New Zealand, USA', 'Won 4 Oscars. Another 113 wins & 123 nominations.', 8.8, 1545049, 314000000)
        ]

        self.assertListEqual(movies, expected_result)

    def test_sort_by_exception_message(self):
        with self.assertRaises(Exception) as context:
            movies = MovieSorter.sort_by('testing_db.db', "id,")

        exception_msg = context.exception.args[0]
        expected_msg = "Given sort_by() argument (id,) is illegal!"

        self.assertEqual(exception_msg, expected_msg)

    def test_filter_by(self):
        movies = MovieFilter.filter_by('testing_db.db', "awards LIKE '%Oscars%' AND year == 2001")
        expected_result = [(1, 'The Lord of the Rings: The Fellowship of the Ring', 2001, 178, 'Adventure, Drama, Fantasy', 'Peter Jackson', 'Alan Howard, Noel Appleby, Sean Astin, Sala Baker', 'J.R.R. Tolkien (novel), Fran Walsh (screenplay), Philippa Boyens (screenplay), Peter Jackson (screenplay)', 'English, Sindarin', 'New Zealand, USA', 'Won 4 Oscars. Another 113 wins & 123 nominations.', 8.8, 1545049, 314000000)]

        self.assertListEqual(movies, expected_result)

    def test_filter_by_exception_message(self):
        with self.assertRaises(Exception) as context:
            movies = MovieFilter.filter_by('testing_db.db', 'year = 2001 AND')

        exception_msg = context.exception.args[0]
        expected_msg = "Given filter_by() argument ( year = 2001 AND ) is illegal!"

        self.assertEqual(exception_msg, expected_msg)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_add_to_db_(self, mock_stdout):
        movie = Movie({"Title": "The Social Network", "Year": "2010", "Rated": "PG-13", "Released": "01 Oct 2010",
                       "Runtime": "120 min", "Genre": "Biography, Drama", "Director": "David Fincher",
                       "Writer": "Aaron Sorkin (screenplay), Ben Mezrich (book)", "Actors": "Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons",
                       "Plot": "As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, he is sued by the twins who claimed he stole their idea, and by the co-founder who was later squeezed out of the business.",
                       "Language": "English, French", "Country": "USA", "Awards": "Won 3 Oscars. Another 165 wins & 168 nominations.",
                       "Poster": "https://m.media-amazon.com/images/M/MV5BOGUyZDUxZjEtMmIzMC00MzlmLTg4MGItZWJmMzBhZjE0Mjc1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
                       "Ratings": [{"Source": "Internet Movie Database", "Value": "7.7/10"}, {"Source": "Rotten Tomatoes", "Value": "96%"}, {"Source": "Metacritic", "Value": "95/100"}],
                       "Metascore": "95", "imdbRating": "7.7", "imdbVotes": "579,002", "imdbID": "tt1285016", "Type": "movie",
                       "DVD":"11 Jan 2011", "BoxOffice": "$96,400,000", "Production": "Columbia Pictures",
                       "Website": "N/A", "Response": "True"})
        expected_output = f"Data from movie - {movie.title} has been inserted to database\n" # obviously sys.stdout automaticly add \n at the end
        expected_result = [(4, 'The Social Network', 2010, 120, 'Biography, Drama', 'David Fincher', 'Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons', 'Aaron Sorkin (screenplay), Ben Mezrich (book)', 'English, French', 'USA', 'Won 3 Oscars. Another 165 wins & 168 nominations.', 7.7, 579002, 96400000)]

        MovieAdder.add_to_db('testing_db.db', movie)
        self.cur.execute("SELECT * from movies where title LIKE 'The Social Network'")
        result = self.cur.fetchall()

        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertListEqual(result, expected_result)

    def test_add_to_db_exception_message(self):
        movie = Movie({
            "Title": "The Lord of the Rings: The Fellowship of the Ring", "Year": "2001", "Rated": "PG-13",
            "Released": "19 Dec 2001", "Runtime": "178 min", "Genre": "Adventure, Drama, Fantasy",
            "Director": "Peter Jackson", "Writer": "J.R.R. Tolkien (novel), Fran Walsh (screenplay), Philippa Boyens (screenplay), Peter Jackson (screenplay)",
            "Actors": "Alan Howard, Noel Appleby, Sean Astin, Sala Baker",
            "Plot":"A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
            "Language": "English, Sindarin", "Country": "New Zealand, USA", "Awards": "Won 4 Oscars. Another 113 wins & 123 nominations.",
            "Poster":"https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SX300.jpg",
            "Ratings": [{"Source": "Internet Movie Database", "Value": "8.8/10"}, {"Source": "Rotten Tomatoes", "Value": "91%"}, {"Source": "Metacritic", "Value": "92/100"}],
            "Metascore": "92", "imdbRating": "8.8", "imdbVotes": "1,545,049", "imdbID": "tt0120737", "Type": "movie", "DVD": "06 Aug 2002",
            "BoxOffice": "$314,000,000", "Production": "New Line Cinema", "Website": "N/A", "Response": "True"})
        with self.assertRaises(Exception) as context:
            MovieAdder.add_to_db('testing_db.db', movie)

        exception_msg = context.exception.args[0]
        expected_msg = f"Given movie ({movie.title}) already in database!"

        self.assertEqual(exception_msg, expected_msg)

    def test_highscores(self):
        expected_result = [
            (1, 'The Lord of the Rings: The Fellowship of the Ring', 2001, 178, 'Adventure, Drama, Fantasy', 'Peter Jackson', 'Alan Howard, Noel Appleby, Sean Astin, Sala Baker', 'J.R.R. Tolkien (novel), Fran Walsh (screenplay), Philippa Boyens (screenplay), Peter Jackson (screenplay)', 'English, Sindarin', 'New Zealand, USA', 'Won 4 Oscars. Another 113 wins & 123 nominations.', 8.8, 1545049, 314000000),
            (3, 'Harry Potter and the Deathly Hallows: Part 2', 2011, 130, 'Adventure, Drama, Fantasy, Mystery', 'David Yates', 'Ralph Fiennes, Michael Gambon, Alan Rickman, Daniel Radcliffe', 'Steve Kloves (screenplay), J.K. Rowling (novel)', 'English', 'USA, UK', 'Nominated for 3 Oscars. Another 45 wins & 91 nominations.', 8.1, 708269, 381000185),
            (2, 'Star Wars: Episode IV - A New Hope', 1977, 121, 'Action, Adventure, Fantasy, Sci-Fi', 'George Lucas', 'Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing', 'George Lucas', 'English', 'USA', 'Won 6 Oscars. Another 50 wins & 28 nominations.', 8.6, 1143909, 'N/A'),
            (1, 'The Lord of the Rings: The Fellowship of the Ring', 2001, 178, 'Adventure, Drama, Fantasy', 'Peter Jackson', 'Alan Howard, Noel Appleby, Sean Astin, Sala Baker', 'J.R.R. Tolkien (novel), Fran Walsh (screenplay), Philippa Boyens (screenplay), Peter Jackson (screenplay)', 'English, Sindarin', 'New Zealand, USA', 'Won 4 Oscars. Another 113 wins & 123 nominations.', 8.8, 1545049, 314000000)
        ]

        movies = HighscoresFinder.highscores('testing_db.db')

        self.assertListEqual(movies, expected_result)


if __name__ == '__main__':
    unittest.main()
