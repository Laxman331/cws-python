"""•	name - the name of the product
•	category - the category of the product
•	price - the price of the product
•	quantity - the quantity of the product in stock"""


class Product:
    def __init__(self):
        self.name = input("Enter name of the product =")
        self.category = input("Enter category of the product =")
        self.price = int(input("Enter price of the product ="))
        self.quantity = int(input("Enter quantity of the product ="))

    def update_price(self):
        new_price = int(input("Enter new price = "))
        self.price = new_price

    def update_quantity(self):
        new_quantity = int(input("Enter new quantity of the product ="))
        self.quantity = new_quantity

    def display_product(self):
        print("\n------INFO------")
        print(f"Name = {self.name}")
        print(f"Category = {self.category}")
        print(f"Price = {self.price}")
        print(f"Quantity = {self.quantity}")


products = []


def search_products(product):
    for i in products:
        if (i.name == product) or (i.category == product):
            return i
        continue
    else:
        return None


while True:
    print("enter 1 to Add a product")
    print("enter 2 to view all products")
    print("enter 3 to search a product")
    print("enter 4 to update a product")
    print("Enter 5 to remove a product")
    print("enter 6 to exist")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        obj = Product()
        products.append(obj)
        print(products)
    elif choice == 2:
        for i in products:
            i.display_product()
    elif choice == 3:
        nam_cat = input("Enter which one should be searched name or category =")
        if nam_cat == "name":
            pro_name = input("Enter product name =")
            search = search_products(pro_name)
            if search != None:
                search.display_product()
            else:
                print("No product found ")
        elif nam_cat == "category":
            pro_cat = input("Enter category name =")
            search = search_products(pro_cat)
            if search != None:
                search.display_product()
            else:
                print("No product found ")
        else:
            print("Invalid")

    elif choice == 4:
        upd_pro = input("Enter product to update price or quantity =")
        search = search_products(upd_pro)
        if search != None:
            pro_qua = input("Enter which one should be updated price or quantity =")
            if pro_qua == "price":
                search.update_price()
                search.display_product()
            elif pro_qua == "quantity":
                search.update_quantity()
                search.display_product()
            else:
                print("This cannot be updated")

        else:
            print("No product found ")
    elif choice == 5:
        del_pro = input("Enter product to remove =")
        search = search_products(del_pro)
        if search != None:
            products.remove(search)
            print(products)

        else:
            print("No product found ")

    elif choice == 6:
        break
