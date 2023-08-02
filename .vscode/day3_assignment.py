# Side = int(input("Enter Side = "))
# Area = Side * Side
# print(f"Area  of Square is  = {Area}")
# x = int(input("Enter number1 = "))
# y = int(input("Enter number2 = "))
# z = int(input("Enter number3 = "))
# Average = (x + y + z) / 3
# print(f"Average of three numbers is = {Average}")
Games_played = int(input("Enter No of games played = "))
Games_won = int(input("Enter No of games won =  "))
Games_lost = int(input("Enter No of games lost = "))
Games_tie = Games_played - Games_won - Games_lost
Total_points = (Games_won * 4) + (Games_tie * 2)
print(f"Total points is {Total_points}, No of games tie is {Games_tie}")
