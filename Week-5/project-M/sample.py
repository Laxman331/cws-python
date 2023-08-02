movies = {}
mnum = 0

while True:
    print("\n1) Add a Movie")
    print("2) Update a Movie")
    print("3) Delete a Movie")
    print("4) View all Movies")
    print("5) Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        movie_name = input("Enter Movie Name: ")
        director_name = input("Enter Director Name: ")
        release_year = input("Enter Release Year: ")
        genres = input("Enter Generes: ")
        dict = {}
        mnum = mnum + 1
        n = str(mnum)
        mov = "movie" + n
        dict = {
            "movie"
            + n: {
                "Name": movie_name,
                "Director": director_name,
                "Release Year": release_year,
                "Genres": genres,
            }
        }
        for k, v in dict.items():
            movies[k] = v
        print(movies)

    elif choice == 2:
        if len(movies) == 0:
            print("No Movies in the list")
        else:
            n = input("Enter the name of movie you want to update: ")
            for k, v in movies.items():
                if v["Name"] == n:
                    v["Name"] = input("Enter Movie Name: ")
                    v["Director"] = input("Enter Director Name: ")
                    v["Release Year"] = input("Enter release year: ")
                    v["Genres"] = input("Enter Genres: ")
            print(movies)

    elif choice == 3:
        if len(movies) == 0:
            print("No Movies in the list")
        else:
            m = {}
            n = input("Enter the name of movie you want to delete: ")
            for k, v in movies.items():
                if v["Name"] == n:
                    m[k] = v
        for key, value in m.items():
            del movies[key]
        print(movies)

    elif choice == 4:
        if len(movies) == 0:
            print("No Movies in the list")
        else:
            for k, v in movies.items():
                print()
                print(f"-----{v['Name'].upper()}-----")
                print(f"{v['Director']}")
                print(f"{v['Release Year']}")
                print(f"{v['Genres']}\n")
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
