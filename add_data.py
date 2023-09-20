from main import Movie, session, Ratings, app
from sessions import retrieve_columns, print_table, update_rating

#
def add_rating():
    new_rating1 = Ratings(RATING=3, AUTHOR="Jack Spiel", MOVIE_NAME="The Reckoning", MOVIE_ID=3)
    new_rating2 = Ratings(RATING=1, AUTHOR="Captain Hosin", MOVIE_NAME="The Reckoning", MOVIE_ID=3)
    new_rating3 = Ratings(RATING=2, AUTHOR="Wei Lee", MOVIE_NAME="The Reckoning", MOVIE_ID=3)

    session.add_all([new_rating1, new_rating2, new_rating3])
    try:
        session.commit()
        print(f"Success!")
    except Exception as e:
        print(f"Failure due to \n {e}")


with app.app_context():
    # add_rating()
    # update_rating("The Reckoning")
    # print_table(Movie)
    pass
