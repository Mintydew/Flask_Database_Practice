from main import Movie, Ratings, app, session, db

with app.app_context():
    # result = session.connection().execute("SELECT DIRECTOR FROM Movies")
    # for row in result:
    #     print(row)

    all_movies = Movie.query.all()
    print(all_movies)

    movie_one = Movie.query.get(1) #Retrieve everything about Movie ID_1
    # print(movie_one)

    # movie_filtered = Movie.query.filter(Movie.NAME == 'The Reckoning').all()
    # print(movie_filtered)

    # movie_like_queried = Movie.query.filter(Movie.DIRECTOR.like('%Mays%')).all()
    # print(movie_like_queried)

    # movie_like_queried_advanced = session.query(Movie.DIRECTOR).filter(Movie.DIRECTOR.like('%M%Bay%')).all() #This query identifies directors with the letter M before Bay.
    # print(movie_like_queried_advanced)")

    movie_like_queried_advanced_only_director = Movie.query.filter(Movie.DIRECTOR.like('%M%Bay%')).with_entities(Movie.DIRECTOR).all() #This query identifies directors with the letter M before Bay.
    print(movie_like_queried_advanced_only_director)

    result = session.execute("SELECT * FROM RATINGS")
    for row in result:
        print(row)
