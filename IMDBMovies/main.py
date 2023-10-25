import pathlib
import sys

from db_creator import DbCreator
from fetch_data import FetchData
from highscores_finder import HighscoresFinder
from movie import Movie
from movie_adder import MovieAdder
from movie_filter import MovieFilter
from movie_presenter import MoviePresenter
from movie_sorter import MovieSorter


db_path = pathlib.Path("database/movies.db")

if db_path.is_file():

    if len(sys.argv) < 2:
        raise TypeError("Program take at least one positional argument but 0 was given")

    elif sys.argv[1] == "--add" and len(sys.argv) >= 3:

        if sys.argv[2] == "from_file" and len(sys.argv) == 3:
            with open("movie_titles_to_populate_db.txt") as file:
                for line in file:
                    movie_json = FetchData.get_data(line)
                    movie = Movie(movie_json)
                    MovieAdder.add_to_db(db_path, movie)

        else:
            for movie_title in sys.argv[2:]:
                movie_json = FetchData.get_data(movie_title)
                movie = Movie(movie_json)
                MovieAdder.add_to_db(db_path, movie)

    elif sys.argv[1] == "--sort" and len(sys.argv) == 3:
        movies = MovieSorter.sort_by(db_path, sys.argv[2])
        MoviePresenter.console_logger(movies)

    elif sys.argv[1] == "--filter" and len(sys.argv) == 3:
        movies = MovieFilter.filter_by(db_path, sys.argv[2])
        MoviePresenter.console_logger(movies)

    elif sys.argv[1] == "--highscores" and len(sys.argv) == 2:
        movies = HighscoresFinder.highscores(db_path)

        MoviePresenter.console_logger(
            movies,
            customise_headers=[
                "Movie with highest runtime",
                "Movie with highest earnings",
                "Movie with most Oscars won",
                "Movie highest imdb_rating",
            ],
        )

    else:
        raise Exception(
            "Something wrong with specified argument/-s. Please check readme.md and try again!"
        )

else:
    # in case folder 'database/' doesn't exist --> create it with mask 755, and don't raise error if dir already exists
    pathlib.Path("database/").mkdir(mode=0o755, exist_ok=True)

    db = DbCreator(db_path)
    db.create_db()
