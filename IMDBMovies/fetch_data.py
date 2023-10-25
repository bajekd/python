import os
import urllib.parse

import requests
from requests import HTTPError


class FetchData:
    @staticmethod
    def get_data(movie_title):
        """Return response from api service in json format(python dict) describing given movie."""
        # to be explicit, requests do it automatically anyway
        movie_title = requests.utils.quote(movie_title)
        api_key = os.environ.get("OMDB_API_KEY")
        url = f"https://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
        print(url)
        response = requests.get(url)
        try:
            response.raise_for_status()
        except HTTPError as http_err:
            raise HTTPError(f"HTTP HTTP error has occurred: {http_err}")
        except Exception as err:
            raise Exception(f"Other exception has occurred: {err}")

        response_json = response.json()
        if response_json["Response"] != "True":
            movie_title = urllib.parse.unquote_plus(
                movie_title
            )  # decoding url string -> clarity of err message
            raise Exception(
                f"Movie {movie_title} has not been found in https://www.omdbapi.com database!"
            )

        print(f"Data from movie - {response_json['Title']} has been downloaded")
        return response_json
