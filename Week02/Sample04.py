def guessingGameHelper(guess:int, target) -> None:
    if guess > target:
        print("DOWN")
    elif guess < target:
        print("UP")
    else:
        print("BINGO")

def guessingGameDemo(target:int) -> bool:
    guess = int(input("guess a number : "))
    guessingGameHelper(guess, target)
    if guess == target:
        return True
    return False
    
while(True):
    result = guessingGameDemo(100)
    if result :
        break

