# Flask_Database_Practice

A personal practice project API which undergoes database interaction using SQLAlchemy and Flask via Python.

## Table of Contents

- [Introduction](#introduction)
- [Goals](#goals)
- [Technologies Used](#technologies-used)
- [Database Schema](#database_schema)
- [Challenges](#challenges)
- [Future Plans](#future-plans)

## Introduction

A personal project made to practice and showcase my abilities in SQLAlchemy and database interactions. I have not had much practice on either so it was quite a challenge to get the interaction working. 

The database focuses on a simple table involving movies and the ratings. I wanted to ensure that the structure of the Database and its tables were clean and made sense in a fundamental sense.

Through the database, I used SQLAlchemy and Flask to read the database and also practiced data manipulation, insertion and deletion. 

Finally, the API saves to a CSV file. The purpose of this is to gain practice and understanding of the real-wide practical use of exporting data like this into a common data file type(CSV).

## Goals

- To create a database using SQLite.
- To import the database using Flask and SQLAlchemy.
- To establish a connection between the database and the codebase/frameworks.
- To be able to thoroughly manipulate the data on the table as well as others such as adding and deleting.
- To be able to save the changed data into a common CSV file using Python.
- To learn as much as I can along the way through experimentation and failures.
 
## Technologies-Used

- Python
- Flask
- SQLAlchemy
- SQLite

## Database_Schema

|  Table Name | Fields |
| ------------------ | ------------------ |
| Movie | id(PK), name, director, rating |
| Ratings | id(PK), rating, author, movie_id(FK), movie_name


## Challenges

As this was a brand new project for me using technologies I have not been too familiar with practice wise. I have found a few things to be a struggle. From memory, some of these are:

-
-
-

## Future-Plans

There are a few ideas that I have in mind for improvement and 
