try:
    a = int(input("Enter number 1= "))
    b = int(input("Enter number 2= "))
    print(a / b)
except:
    print("Error occured")
    """ Else or Finally is not compulasary
    else wil be run when there is no error
    finally will be run if there is error or not"""
else:
    print("This is else statement")
finally:
    print("This is final  statement")
