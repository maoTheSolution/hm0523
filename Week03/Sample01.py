year = int(input("Enter any year : "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap")
#         else:
#             print("Nope")
#     else:
#         print("Leap")
# else:
#     print("Not a Leap")


# if year % 4 == 0:
#     if year % 400 == 0:
#         print("Leap")
#     elif year % 100 == 0:
#         print("Nope")
#     else:
#         print("Leap")
# else:
#     print("Nope")


if (year%4==0 and year%100 != 0) or year%400==0:
    print("Leap")
else:
    print("Nope")