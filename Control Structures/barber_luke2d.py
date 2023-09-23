import random

guessesamt = 0

number = random.randint(1, 11)
print(number)

print("I'm thinking of a number between 1 and 11.")
print()

guess = int(input('Guess my number: '))

guessesamt = guessesamt + 1
if guess == number:
    print("You got it!")
    print()
    print("It took you", guessesamt, "try to guess the number.")
    print("The secret number was", str(number)+'.')

else:
    if guess < number:
        print('Too low, try again.')
        print()
            
    elif guess > number:
        print('Too high, try again.')
        print()

    guess = int(input('Guess my number: '))
    
    if guess == number:
        guessesamt = guessesamt + 1
        print("You got it!")
        print()
        print("It took you", guessesamt, "tries to guess the number.")
        print("The secret number was", str(number)+'.')
        
    else:
        if guess < number:
            print('Too low, try again.')
            print()
            
        elif guess > number:
            print('Too high, try again.')
            print()  
            
        guess = int(input('Guess my number: '))
        
        if guess == number:
            guessesamt = guessesamt + 2
            print("You got it!")
            print()
            print("It took you", guessesamt, "tries to guess the secret number.")
            print("The secret number was", str(number)+'.')
        
        if guess != number:
            print("Sorry, game over")
            print()
            print("The secret number was", str(number)+'.')
