
import random
RNum = random.randint(1,50)
PNam = input("Please enter your name:")
YES = "Good job " + PNam + "! You guessed my number!"
NOH = "Too bad " + PNam + ", your guess was too high."
NOL = "Too bad " + PNam + ", your guess was too low."
END = "Thank you for playing! GAME OVER"
print("Hello " + PNam + ", welcome to my game!")
while True:
    PNum = int(input("Please guess a number between 1 and 50:"))
    if RNum == PNum:
        print(YES)
        break
    elif RNum > PNum:
        print(NOL)
    else:
        print(NOH)
print(END)
