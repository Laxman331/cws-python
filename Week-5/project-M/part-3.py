# a = {"1": {"2": 8, "3": 9}}
# for k, v in a.items():
#     print(v)
Movie_list = {}
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
