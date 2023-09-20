from main import db, session, Movie, app


with app.app_context():
    # for row in session.execute('SELECT * FROM Movie'):
    #     print(f'Prior to testing: ', row)
    #
    # #Get schema of table
    # table = Movie.__table__
    #
    # columns_schema = [column.name for column in table.c]
    # print('\n', columns_schema, '\n')

    def add_movie(name, director, rating):
        existing_movie = Movie.query.filter(Movie.NAME == name).first()

        if existing_movie:
            print("Movie already exists!")
            return

        new_movie = Movie(NAME=name, DIRECTOR=director, RATING=rating)

        db.session.add(new_movie)
        try:
            db.session.commit()
            print(f"Successfully added: {new_movie.NAME} to the movie table", '\n')
            db.session.expire_all()
        except Exception as e:
            db.session.rollback()
            print(f"An unexpected error has occurred: {e}", '\n')

    def delete_movie(id_or_movie):
        movie_name = ""
        if isinstance(id_or_movie, int):
            query_result = Movie.query.filter(Movie.ID == id_or_movie).with_entities(Movie.NAME).first()
            movie_name = query_result[0]
            db.session.delete(Movie.query.get(id_or_movie))
        elif isinstance(id_or_movie, str):
            query_result = Movie.query.filter(Movie.NAME == id_or_movie).with_entities(Movie.NAME).first()
            movie_name = query_result[0]
            db.session.delete(Movie.query.filter(Movie.NAME == id_or_movie).first())

        try:
            db.session.commit()
            print(f"Successfully removed: {movie_name} from the movie table", '\n')
            db.session.expire_all()
        except Exception as e:
            db.session.rollback()
            print(f"An unexpected error has occurred: {e}", '\n')

    def update_movie(id_or_movie, to_update, update_data):
        if isinstance(to_update, str):
            to_update = to_update.upper()

        movie_name = ""
        table = Movie.__table__
        column_names = [column.name for column in table.columns]

        if to_update not in column_names:
            print("Please select a valid column!")
            return

        if isinstance(id_or_movie, int):
            query_result = Movie.query.filter(Movie.ID == id_or_movie).with_entities(Movie.NAME).first()
            movie_name = query_result[0]
            movie = Movie.query.get(id_or_movie)
            setattr(movie, to_update, update_data)
        elif isinstance(id_or_movie, str):
            query_result = Movie.query.filter(Movie.NAME == id_or_movie).with_entities(Movie.NAME).first()
            movie_name = query_result[0]
            movie = Movie.query.filter(Movie.NAME == id_or_movie).first()
            setattr(movie, to_update, update_data)

        try:
            db.session.commit()
            print(f"Successfully updated {movie_name} by adjusting the {to_update.lower()} to {update_data}", '\n')
            db.session.expire_all()
        except Exception as e:
            db.session.rollback()
            print(f"An unexpected error has occurred: {e}", '\n')


    def update_rating(movie):

        total = 0
        instance = 0

        query = [rating for rating in session.execute(f"SELECT RATING FROM Ratings WHERE MOVIE_NAME = '{movie}'")]

        for score in query:
            total += score[0]
            instance += 1

        updated_rating = total / instance
        update_movie(movie, "rating", updated_rating)


    def print_table(model, comment=""):
        if not isinstance(model, str):
            temp = model()
            model = temp.__class__.__name__

        if comment != "":
            for line in session.execute(f'SELECT * FROM {model}'):
                print(f"{comment}: {line}")
            print()
        else:
            for line in session.execute(f'SELECT * FROM {model}'):
                print(line)
            print()

    def retrieve_columns(model):
        table = model.__table__
        table_columns = [column.name for column in table.c]
        return table_columns



    # add_movie(input("Movie Name?"), input("Director?"), input("Ratings?"))
    # add_movie("Test Film!", "Me!", 100)
    # print_table("Added test row")
    # delete_movie('Test Film!')
    # print_table("Post deletion")

    # add_movie("Deliverance", "Ponti Markus", 5)
    # update_movie(54, "NAME", "Belong")
    # print_table("Post Update")

