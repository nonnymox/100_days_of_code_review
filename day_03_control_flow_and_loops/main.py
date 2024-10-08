# # Pizza Deliveries Algorithm
#
# print("Welcome to Python Pizza Deliveries!")
# try:
#     size = input("What size pizza do you want? S, M or L: ").lower()
#     bill = 0
#     if size == "s":
#         bill += 15
#     elif size == "m":
#         bill += 20
#     elif size == "l":
#         bill += 25
#     else:
#         print("Please input S, M or L only")
# except ValueError:
#     print("Please enter a S, M or L!")
#
# else:
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
#     match pepperoni:
#         case "y":
#             if size == "s":
#                 bill += 2
#                 print(bill)
#             else:
#                 bill += 3
#                 print(bill)
#         case "n":
#             pass
#     extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
#     match extra_cheese:
#         case "y":
#             bill += 1
#         case "n":
#             pass
# finally:
#     print(f"Your final bill is ${bill}")

print("""
     0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \\   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777

Welcome to the 007 Treasure Island
Your job is to find the treasure.""")

l_or_r = input("Left or Right?\n").lower()
match l_or_r:
    case "left":
        swim = input("swim or wait\n").lower()
        match swim:
            case "swim":
                print("Game Over!!!")
            case "wait":
                door = input("Which door?\n").lower()
                match door:
                    case "red":
                        print("Game Over!")
                    case "blue":
                        print("Game Over!!!")
                    case "yellow":
                        print("You win!!!")
                    case _:
                        print("Invalid Input!")
            case _:
                print("Invalid Input!")

    case "right":
        print("Game Over!!!")
    case _:
        print("Invalid Input!")
