import random
v = random.randint(0,100)

n = int(input("Guess the number : "))
a = 0
b = 10
while n != v:
    if a > 9:
        print("Game over")
        break
    if n > v:
        print("Your number is greater than the original number.")
    if n < v:
        print("Your number is lesser than the original number.")
    n = int(input("Guess the number : "))
    a = a +1
    print ("Try left  " + str(b - a))
    if n == v:
        print("You won!")
        break
    continue
