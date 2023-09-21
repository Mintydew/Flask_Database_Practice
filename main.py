from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Troubleshooting identification on whether database exists
# db_path = 'ForCSVImport.db'

# if os.path.exists(db_path):
#     print("Database exists")
# else:
#     print("Database does not exist at: ", db_path)


app = Flask('__NAME__')
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///ForCSVImport.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
session = db.session

# CREATE TABLE "Movie" (
# 	"ID"	INTEGER NOT NULL UNIQUE,
# 	"NAME"	TEXT NOT NULL,
# 	"DIRECTOR"	TEXT NOT NULL,
# 	"RATING"	INTEGER,
# 	PRIMARY KEY("ID" AUTOINCREMENT),
# 	FOREIGN KEY("RATING") REFERENCES "Ratings"("ID")
# )

with app.app_context():
    class Movie(db.Model):
        ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
        NAME = db.Column(db.String, nullable=False, unique=True)
        DIRECTOR = db.Column(db.String, nullable=False)
        RATING = db.Column(db.Integer, nullable=False)
        RATINGS = db.relationship('Ratings', backref='movie', lazy='dynamic', cascade="all, delete, delete-orphan")

        def __repr__(self):
            return "Movie ID: {}, Movie: {}, director: {} with a rating of {}".format(self.ID, self.NAME, self.DIRECTOR, self.RATING)


    # CREATE TABLE "Ratings" (
    # 	"ID"	INTEGER NOT NULL UNIQUE,
    # 	"RATING"	INTEGER NOT NULL,
    # 	"AUTHOR"	TEXT NOT NULL,
    # 	"MOVIE_ID"	INTEGER NOT NULL,
    # 	"MOVIE_NAME"	TEXT NOT NULL,
    # 	FOREIGN KEY("MOVIE_ID") REFERENCES "Movie"("ID"),
    # 	PRIMARY KEY("ID" AUTOINCREMENT)
    # )


    class Ratings(db.Model):
        ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
        RATING = db.Column(db.Integer, nullable=False)
        AUTHOR = db.Column(db.String, nullable=False)
        MOVIE_NAME = db.Column(db.String, nullable=False)
        MOVIE_ID = db.Column(db.Integer, db.ForeignKey('movie.ID'), nullable=False)

        def __repr__(self):
            return "Rating ID: {}, author: {}, for movie: {}".format(self.ID, self.AUTHOR, self.MOVIE_NAME)
