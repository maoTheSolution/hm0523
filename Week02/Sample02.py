#   name, argument, return type
# def hm(given:int) -> bool:
    


def test01() -> None : 
    print("Welcome to our land!!")

# test01()

def test02() -> int:
    return 1004

# print(test02())

def test03(name:str) -> str:
    return name + ", 님 안녕하세요!"

print(test03("Adam"))


def gugudan(dan:int) -> None:
    for each in range(1,10):
        print(each * dan)

# gugudan(5)


def mul(first:int, second:int) -> int:
    return first * second
# print(mul(4, 12))


def welcoming(name:str) -> str:
    return str + ", welcome!"


def checker(given:int) -> bool:
    if given < 10:
        return True
    else:
        return False
    
print(checker(5))
print(checker(10))
print(checker(17))

target = 100
def guessingGameDemo(guess : int) -> bool:
    if guess == target:
        return True
    else:
        return False