movie = []
new = {}
director = input("Enter Director name =")
release_year = int(input("Enter Release year = "))
genre = input("Enter movie genre =")
new["Director"] = director
new["Release_year"] = release_year
new["genres"] = genre
movie.append(new)
print(movie)
