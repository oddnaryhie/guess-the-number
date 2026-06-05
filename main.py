import random
n = random.randint(1, 100)
a = -1
guesses = 1
while (a!=n):
    a = int(input("Guess a Number"))
    if a>n:
        print("Lower Number Please")
        guesses += 1
    elif(a<n):
        print("Higher Number Please")
        guesses += 1

print(f"CONGRATSS!! You Guessed The Correct Number {n} in {guesses} Attempt")