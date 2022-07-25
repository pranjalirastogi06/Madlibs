import random
def guess(x):
        rn = random.randint(1, x)
        guess = 0
        while guess != rn:
                guess = int(input(f"Guess a number between 1 and {x}"))
                if guess > rn:
                        print("Too high")
                elif guess < rn:
                        print("Too low")
        print(f"Correct answer is {guess}")
guess(20)
                
	
