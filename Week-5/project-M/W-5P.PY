"""
Project 4
Simple Movie Database

Objective
Create a simple movie database that allows users to add, update, delete, and
view movie information. Utilize Python basics such as dictionaries, loops, and
conditional statements to create the application.

Requirements
1. Use dictionaries to store movie information, such as titles, directors,
release years, and genres.
2. Use loops to create a menu-driven interface for users to interact with
the database.
3. Use conditional statements to perform various operations, such as
adding, updating, deleting, and viewing movies.

Instructions
1. Create a dictionary to store movie information, including titles, directors,
release years, and genres.
2. Design a menu-driven interface that allows users to choose between
the following operations:
a. Add a movie
b. Update a movie
c. Delete a movie
d. View all movies
e. Exit
3. Use a loop to iterate through the menu, allowing users to perform
multiple operations without having to restart the application.

4. Based on the user's selection, use conditional statements to perform
the chosen operation:
a. Add a movie: Request the necessary movie information from the
user and add it to the dictionary.
b. Update a movie: Ask the user for the movie title, find the movie in
the dictionary, and update the relevant information.
c. Delete a movie: Ask the user for the movie title and remove the
movie from the dictionary.
d. View all movies: Display the movie information stored in the
dictionary.

5. Continue looping through the menu until the user chooses to exit the
application."""

Movie_list = {}
while True:
    print("enter 1 to Add a movie")
    print("enter 2 to update a movie")
    print("enter 3 to delete a movie")
    print("enter 4 to view all  movie")
    print("enter 5 to exist")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        movie_name = input("Enter Movie Name =")
        movie_Details = {}
        director = input("Enter Director name =")
        release_year = int(input("Enter Release year = "))
        genre = input("Enter movie genre =")
        movie_Details["Director"] = director
        movie_Details["Release_year"] = release_year
        movie_Details["genres"] = genre
        Movie_list[movie_name] = movie_Details
        print(Movie_list)
    if choice == 2:
        movie = input("Enter movie name to be updated=")

        for k, v in Movie_list.items():
            if k == movie:
                x = str(input("Enter which details of the movie to be updated ="))
                y = input("Enter your final updated name =")
                v[(str(x))] = y
            else:
                print("invalid movie")
        print(Movie_list)
    if choice == 3:
        delete_movie = input("Enter movie name to be deleted =")
        for k, v in Movie_list.items():
            if k == delete_movie:
                Movie_list.pop(delete_movie)
            else:
                print("Invalid movie")
        print(Movie_list)
    if choice == 4:
        if len(Movie_list) == 0:
            print("No movies")
        else:
            for k, v in Movie_list.items():
                print(f"{k}->{v}")
    if choice == 5:
        break
