class Parent:
    def displayParent(self):
        print("Display of Parent class is being called")


class Child(Parent):
    def displayChild(self):
        print("Display of Child class is being called")


o = Child()
o.displayChild()
o.displayParent()
