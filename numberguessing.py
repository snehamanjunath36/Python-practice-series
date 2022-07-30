import random
def guess():
        guess_range = int(input("Enter your range of guessing number (ending number):  "))
        computer_choice = random.randrange(0, guess_range + 1)
                # random.randrange(a, b) ->  b is the number of elements given as output starting from the start point a
        print(""" You will be given 3 chances to guess the number along with hints
                                    ALL THE BEST!!! """)
        #print(computer_choice)
        for i in range(3):
            guessed = int(input(f'enter your {i+1} guess'))
            if guessed == computer_choice:
                print("You got it right !!")
                break
            elif guessed > guess_range:
                print("your guess is higher than the guessing number")
            elif guessed > computer_choice:
                print("your guess is higher than the computer choice")
            else:
                print('your guess is lower than the  computer choice')
score = 0
while True:
    score += 1
    ans = input("Do you like to play the number guess game(yes / no):  ").lower()
    if ans == "yes":
        guess()
    else:
        print("Bye!!")
        quit()

    