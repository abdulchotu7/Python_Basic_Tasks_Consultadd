import random 

x=random.randint(1,100)
print("Guess a number between 1 and 100.")
attempts=0
while True:
    guess=int(input())
    if guess<x:
        print("Too low. Try again.")
        attempts+=1
    elif guess>x:
        print("Too high. Try again.")
        attempts+=1
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

