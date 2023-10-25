class MoviePresenter:
    @staticmethod
    def console_logger(data_to_print, customise_headers=""):
        """Prints given input to console - data passed as list of tuples (each tuple is a movie description)"""

        dash = f"\n{104 * '-'}\n"
        formatted_result = [
            f"""{id_column} | {title} | {year} | {(str(runtime // 60) + 'h') if runtime != 'N/A' else 'N/A'} {(str(runtime % 60) + 'min') if runtime != 'N/A' else ''} | {genre} | {director} | {actors} | {writer} | {language} | {country} | {awards} | {imdb_rating} | {('{:,}'.format(imdb_votes)) if imdb_votes != 'N/A' else 'N/A'} | {('${:,}'.format(box_office)) if box_office != 'N/A' else 'N/A'}{dash}"""
            for id_column, title, year, runtime, genre, director, actors, writer, language, country, awards, imdb_rating, imdb_votes, box_office in data_to_print
        ]

        if customise_headers != "":
            customise_headers = [
                f"""{header:^100}{dash}""" for header in customise_headers
            ]
            new_formatted_result = []
            for i in range(len(customise_headers)):
                new_formatted_result.append(customise_headers[i])
                new_formatted_result.append(formatted_result[i])

            (
                id_column,
                title,
                year,
                runtime,
                genre,
                director,
                actors,
                writer,
                language,
                country,
                awards,
                imdb_rating,
                imdb_votes,
                box_office,
            ) = (
                "id",
                "title",
                "year",
                "runtime",
                "genre",
                "director",
                "actors",
                "writer",
                "language",
                "country",
                "awards",
                "imdb_rating",
                "imdb_votes",
                "box_office",
            )

            print(
                "\n".join(
                    [
                        f"""{dash}| {id_column} | {title} | {year} | {runtime} | {genre} | {director} | {actors} | {writer} | {language} | {country} | {awards} | {imdb_rating} | {imdb_votes} | {box_office}{dash}"""
                    ]
                    + new_formatted_result
                )
            )

        else:
            (
                id_column,
                title,
                year,
                runtime,
                genre,
                director,
                actors,
                writer,
                language,
                country,
                awards,
                imdb_rating,
                imdb_votes,
                box_office,
            ) = (
                "id",
                "title",
                "year",
                "runtime",
                "genre",
                "director",
                "actors",
                "writer",
                "language",
                "country",
                "awards",
                "imdb_rating",
                "imdb_votes",
                "box_office",
            )

            print(
                "\n".join(
                    [
                        f"""{dash}| {id_column} | {title} | {year} | {runtime} | {genre} | {director} | {actors} | {writer} | {language} | {country} | {awards} | {imdb_rating} | {imdb_votes} | {box_office}{dash}"""
                    ]
                    + formatted_result
                )
            )
