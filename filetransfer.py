from main import Movie, Ratings, app
from sessions import retrieve_columns
from flask import jsonify
import csv

print(retrieve_columns(Movie))
print(retrieve_columns(Ratings))

with app.app_context():
    def read_data():
        movie_data = Movie.query.all()
        ratings_data = Ratings.query.all()

        movie_list = [{'name': movie.NAME, 'director': movie.DIRECTOR, 'rating': movie.RATING} for movie in movie_data]
        ratings_list = [{'rating': ratings.RATING, 'author': ratings.AUTHOR, 'movie_name': ratings.MOVIE_NAME} for
                        ratings in ratings_data]

        data = {
            'movies': movie_list,
            'ratings': ratings_list
        }

        # print(jsonify(data))
        return jsonify(data)


    def save_to_csv():
        movie_data = Movie.query.all()
        ratings_data = Ratings.query.all()

        movie_list = [{'name': movie.NAME, 'director': movie.DIRECTOR, 'rating': movie.RATING} for movie in movie_data]
        ratings_list = [{'rating': ratings.RATING, 'author': ratings.AUTHOR, 'movie_name': ratings.MOVIE_NAME} for
                        ratings
                        in ratings_data]

        data = {
            'movies':movie_list,
            'ratings':ratings_list
        }

        filename = 'output.csv'

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = data['movies'][0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data['movies']:
                writer.writerow(row)

        print(f'Completed writing to {filename}')


    save_to_csv()
