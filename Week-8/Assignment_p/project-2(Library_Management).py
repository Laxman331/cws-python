"""Library Management"""


class Library:
    def __init__(self):
        self.title = input("Enter Title of the book =")
        self.author = input("Enter author of the book =")
        self.num_copies = int(input("Enter number of copies of the book ="))

    def display_book(self):
        print("\n------INFO------")
        print(f"Title = {self.title}")
        print(f"Author = {self.author}")
        print(f"No.of Copies = {self.num_copies}")


Books = []
borrowers = []


def searchbook(Name, Author):
    for i in Books:
        if (i.title == Name) and (i.author == Author):
            return i
        continue
    else:
        return None


def search_book(Name, Author):
    for i in borrowers:
        if (i.title == Name) and (i.author == Author):
            return i
        continue
    else:
        return None


while True:
    print("\nEnter 1 to Add a Books")
    print("Enter 2 to view all Books")
    print("Enter 3 to display Available Books to borrow")
    print("Enter 4 to Borrow a Book")
    print("Enter 5 to display Borrow Books")
    print("Enter 6 to return a Book")
    print("Enter 7 to exist")

    choice = int(input("Enter your choice = "))
    if choice == 1:
        obj = Library()
        Books.append(obj)
        print(Books)
    elif choice == 2:
        if len(Books) != 0:
            for i in Books:
                i.display_book()
        else:
            print("No Books there")
    elif choice == 3:
        if len(Books) != 0:
            for i in Books:
                i.display_book()
        else:
            print("No Books there")
    elif choice == 4:
        name = input("Enter name  of the book to borrow =")
        Author = input("Enter name  of the Author to borrow =")
        search = searchbook(name, Author)
        if search != None:
            borrowers.append(search)
            search.num_copies = search.num_copies - 1
            if search.num_copies == 0:
                Books.remove(search)
            print(borrowers)

        else:
            print("Book Not found")

    elif choice == 5:
        if len(borrowers) != 0:
            for i in borrowers:
                i.display_book()
        else:
            print("No Book Borrowed")
    elif choice == 6:
        name = input("Enter name  of the book to return =")
        Author = input("Enter name  of the Author to return =")
        name = search_book(name, Author)
        if search != None:
            borrowers.remove(search)
            search.num_copies = search.num_copies + 1
            Books.append(search)
            print(Books)
            print(borrowers)

        else:
            print("Book Not found")
    elif choice == 7:
        break
