import pyodbc
import pandas as pd
import json
from sqlalchemy import create_engine


conn = pyodbc.connect("Driver=SQL Server;"
                      "Server=DESKTOP-DKUUCTH\SQLEXPRESS;"
                      "Database=DAP301m_movies;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE MOVIE (
#         id INT PRIMARY KEY,
#         adult BIT,
#         budget INT,
#         homepage VARCHAR(255),
#         imdb_id VARCHAR(255),
#         original_language VARCHAR(255),
#         original_title VARCHAR(255),
#         overview VARCHAR(MAX),
#         popularity FLOAT,
#         poster_path VARCHAR(255),
#         release_date DATETIME,
#         revenue INT,
#         runtime INT,
#         [status] VARCHAR(255),
#         tagline VARCHAR(255),
#         title VARCHAR(255),
#         video BIT,
#         vote_average FLOAT,
#         vote_count INT
#     )
# 	CREATE TABLE RATING ( 
# 		userId INT, 
# 		movieId INT, 
# 		rating FLOAT,
# 		[timestamp] DATETIME PRIMARY KEY,
# 		CONSTRAINT FK_RATING_MOVIE FOREIGN KEY (movieId) REFERENCES MOVIE(id)
# 	)
#     CREATE TABLE [COLLECTION] (
#         id INT,
#         [name] VARCHAR(255),
#         poster_path VARCHAR(255),
#         backdrop_path VARCHAR(255),
#         movie_id INT,
#         CONSTRAINT PK_COLLECTION PRIMARY KEY (id, movie_id),
#         CONSTRAINT FK_COLLECTION_MOVIE FOREIGN KEY (movie_id) REFERENCES MOVIE(id)
#     )
#     CREATE TABLE GENRE (
#         id INT,
#         [name] VARCHAR(255),
#         movie_id INT ,
#         CONSTRAINT PK_GENRE PRIMARY KEY (id, movie_id),
#         CONSTRAINT FK_GENRE_MOVIE FOREIGN KEY (movie_id) REFERENCES MOVIE(id)
#     )
#     CREATE TABLE [LANGUAGE] (
#         iso_639_1 VARCHAR(255),
#         [name] VARCHAR(255),
#         movie_id INT,
#         CONSTRAINT PK_LANGUAGE PRIMARY KEY (iso_639_1, movie_id),
#         CONSTRAINT FK_LANGUAGE_MOVIE FOREIGN KEY (movie_id) REFERENCES MOVIE(id)
#     )
#     CREATE TABLE COMPANY (
#         [name] VARCHAR(255),
#         id INT,
#         movie_id INT,
#         CONSTRAINT PK_COMPANY PRIMARY KEY (id, movie_id),
#         CONSTRAINT FK_COMPANY_MOVIE FOREIGN KEY (movie_id) REFERENCES MOVIE(id)
#     )
#     CREATE TABLE COUNTRY (
#         iso_3166_1 VARCHAR(255),
#         [name] VARCHAR(255),
#         movie_id INT,
#         CONSTRAINT PK_COUNTRY PRIMARY KEY (iso_3166_1, movie_id),
#         CONSTRAINT FK_COUNTRY_MOVIE FOREIGN KEY (movie_id) REFERENCES MOVIE(id)
#     )
#     CREATE TABLE KEYWORD (
#         id INT,
#         [name] VARCHAR(255),
#         movie_id INT,
#         CONSTRAINT PK_KEYWORD PRIMARY KEY (id, movie_id),
#         CONSTRAINT FK_KEYWORD_MOVIE FOREIGN KEY (movie_id) REFERENCES MOVIE(id)
#     )
#     CREATE TABLE [CAST] (
#         cast_id INT,
#         [character] VARCHAR(255),
#         credit_id VARCHAR(255),
#         gender INT,
#         id INT,
#         [name] VARCHAR(255),
#         [order] INT,
#         profile_path VARCHAR(255),
#         movie_id INT,
#         CONSTRAINT PK_CAST PRIMARY KEY (cast_id, id, movie_id),
#         CONSTRAINT FK_CAST_MOVIE FOREIGN KEY (movie_id) REFERENCES MOVIE(id),
#     )
#     CREATE TABLE CREW (
#         credit_id VARCHAR(255),
#         department VARCHAR(255),
#         gender INT,
#         id INT,
#         job VARCHAR(255),
#         [name] VARCHAR(255),
#         profile_path VARCHAR(255),
#         movie_id INT,
#         CONSTRAINT PK_CREW PRIMARY KEY (credit_id, id, movie_id),
#         CONSTRAINT FK_CREW_MOVIE FOREIGN KEY (movie_id) REFERENCES MOVIE(id)
#     )    
# ''') 
# conn.commit()

