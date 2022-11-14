import random
randNumber = random.randint(1,100)
# print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You Guessed it Right!! ")
    else:
        if(userGuess > randNumber):
            print("please Guess smaller number")
        else:
            print("please Guess larger number")



print(f"you guessed the number in {guesses} guesses")
print("you win the guess")




with open("hiscore.txt" , 'r')as f:
    hiscore = int(f.read())


if(guesses>hiscore):
    print("you have just broken the hiscore")
    with open("hiscore.txt" , 'w') as f:
        f.write(str(guesses))










