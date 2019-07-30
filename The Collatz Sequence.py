

def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return collatz(number//2)
    elif number % 2 != 0 and number != 1:
        print((number*3)+1)
        return collatz((number*3)+1)
    elif number == 1:
        return number


while True:
    number = input("Enter Number: ")
    try:
        int(number)
        number = int(number)
        break
    except ValueError:
        print("Enter a Valid number")

collatz(number)
