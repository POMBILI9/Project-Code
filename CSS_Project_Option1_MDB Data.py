#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:20:07 2024

@author: user
"""

import pandas as pd 

#Question 1 
# Load the Dataset
file_path = "movie_dataset.csv"
df = pd.read_csv(file_path)

#Find the movie with the highest rating 
highest_rating_movie = df.loc[df["Rating"].idxmax()]

print("\n Question 1")
print(f"Movie Name : {highest_rating_movie['Title']}")


#Question 2 
 
Clean_movie_data = df.dropna()

#Calculate average revenue for all movies 

average_revenue = Clean_movie_data["Revenue (Millions)"].mean()

print("\n Question 2")
print(f"average_revenue: {average_revenue:.2f} Million")

#Question 3

#Calculate the average revenue of movies from 2015 to 2017 
#Filter movies form 2015 to 2017

Filtered_movie_data = Clean_movie_data[(Clean_movie_data["Year"] >= 2015) & (Clean_movie_data["Year"] <=2017)]


# Calculate the average revenues for the movies 
average_revenue = Filtered_movie_data["Revenue (Millions)"].mean()

print("\n Question 3")
print(f"Average Revenue (2015 to 2017): {average_revenue}")


#Question 4


#Number of movies released in 2016

No_of_movies_in_2016 = df[df["Year"] == 2016]

Movies_in_2016 = len(No_of_movies_in_2016)

print("\n Question 4")
print(f"Movies_in_2016:{Movies_in_2016}")


#Question 5 

#Movies directed by Christopher Nolan

Movies_directed_by_Christopher_Nolan = df[df["Director"] == "Christopher Nolan"]

Christopher_Nolan = len(Movies_directed_by_Christopher_Nolan )

print("\n Question 5")
print(f"Christopher_Nolan :{Christopher_Nolan}")


#Question 6

#Rating of atleast 8.0


Ratings = df[df["Rating"] >= 8.0]

Ratings_atleast_8 = len(Ratings)

print("\n Question 6")
print(f"Ratings_atleast_8 :{Ratings_atleast_8}")


# Question 7

# Median rating of movies directed by Christopher Nolan

Movies_directed_by_Christopher_Nolan = df[df["Director"] == "Christopher Nolan"]
Ratings = Movies_directed_by_Christopher_Nolan["Rating"]

Ratings_median = Ratings.median()

print("\n Question 7")
print(Ratings_median)


# Question 8

# Find the year with the highest ratings 

Highest_rating_year = df.groupby("Year")["Rating"].mean()

Highest_rating = Highest_rating_year.idxmax()

print("\n Question 8")
print(Highest_rating)


# Question 9
# Percentage increase in number of movies made between 2006 and 2016 

No_of_movies_in_2006 = df[df["Year"] ==2006]
Movies_in_2006 = len(No_of_movies_in_2006)

No_of_movies_in_2016 = df[df["Year"] == 2016]
Movies_in_2016 = len(No_of_movies_in_2016)

Percentage_increase = (Movies_in_2016 - Movies_in_2006) / Movies_in_2006 * 100

print("\n Question 9")
print(Percentage_increase)


# Question 10
# Find the most common actor in all the movies


Names = []

for name in df ["Actors"]:
    Names += name.split(", ")

Most_common_actor = max(Names, key= Names.count)


print("\n Question 10")
print(Most_common_actor)

# Question 11

# How many unique genres are there in the dataset
import pandas as pd

Genres = []

for each_cell in df ["Genre"]:
    Genres += each_cell.split(",")

Unique_genres = list(dict.fromkeys(Genres))

No_of_unique_genres = len(Unique_genres)

print("\n Question 11")
print(No_of_unique_genres)






    




