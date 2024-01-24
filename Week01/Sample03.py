
num = 77
while(True):
    temp = int(input("Guess any number between 0 and 100 : "))
    if temp > num :
        print("DOWN")
    elif temp < num :
        print("UP")
    else :
        print("BINGO!")
        break
