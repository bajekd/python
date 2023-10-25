class Movie:
    """Data model of single movie"""

    def __init__(self, movie_json):
        self.title = movie_json.get('Title', 'N/A')

        self.year = movie_json.get('Year', 'N/A')
        self.year = int(self.year) if self.year != 'N/A' else None

        self.runtime = movie_json.get('Runtime', 'N/A').replace('min', '')  # runtime in minutes (as integer in db)
        self.runtime = int(self.runtime) if self.runtime != 'N/A' else None

        self.genre = movie_json.get('Genre', 'N/A')
        self.director = movie_json.get('Director', 'N/A')
        self.actors = movie_json.get('Actors', 'N/A')
        self.writer = movie_json.get('Writer', 'N/A')
        self.language = movie_json.get('Language', 'N/A')
        self.country = movie_json.get('Country', 'N/A')
        self.awards = movie_json.get('Awards', 'N/A')

        self.imdb_rating = movie_json.get('imdbRating', 'N/A')
        self.imdb_rating = float(self.imdb_rating) if self.imdb_rating != 'N/A' else None

        self.imdb_votes = movie_json.get('imdbVotes', 'N/A').replace(',', '')
        self.imdb_votes = int(self.imdb_votes) if self.imdb_votes != 'N/A' else None

        self.box_office = movie_json.get('BoxOffice', 'N/A').replace(',', '').replace('$', '')
        self.box_office = int(self.box_office) if self.box_office != 'N/A' else None




