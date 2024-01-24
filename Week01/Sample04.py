def gugudan():
    dan = int(input("Enter the dan : "))
    for each in range(1, 10):
        print(dan, "*", each, "=", dan*each)

def guessingGame():
    target = int(input("Enter any num : "))
    while(True):
        temp = int(input("Guess : "))
        if temp > target :
            print("DOWN")
        elif temp < target:
            print("UP")
        else : 
            print("BINGO")
            break

if __name__ == "__main__":
    gugudan()
    guessingGame()
    gugudan()