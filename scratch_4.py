
print("Enter your number: ")
number = int(input())


def collatz(number):
    if  number % 2 == 0:
         number = number // 2
         print(number)
         return int(number)

    else:
        number = (number * 3) + 1
        print(number)
        return  int(number)

while number != 1:
    number = collatz(number)








