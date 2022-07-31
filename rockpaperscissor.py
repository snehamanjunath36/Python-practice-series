
import random

c_win = 0
p_win =0 
total_play = 0

while True:
    sel = ['rock','paper','scissor']
    p_choice = input("Enter your move(rock,paper,scissor) or q to quit:  ").lower()
    if(p_choice == 'q'  ):
        print("See You Next Time,Bye!!")
        break
    elif(p_choice not in sel):
        continue
    else:
        c_choice = sel[random.randint(0,2)]
        print(f"Computer choose {c_choice}.")
        if(c_choice == p_choice):
            total_play += 1
            continue
        elif(c_choice == 'rock' and p_choice == "scissor"):
            c_win += 1
            total_play += 1
            continue
        elif(c_choice == 'paper' and p_choice == 'rock'):
            c_win += 1
            total_play += 1
            continue
        elif(c_choice == 'scissor' and p_choice == 'paper'):
            c_win += 1
            total_play += 1
            continue
        else:
            p_win += 1
            total_play += 1
            continue
print(f"""Total games played: {total_play}
 You won: {p_win} scores
 Computer won: {c_win} scores""")

# import random
# def play():
#     sel = ['rock','paper','scissor']
#     c_choice = sel[random.randint(0,2)]
#     print(type(c_choice))
#     p_choice = input("Enter your move(rock,paper,scissor)").lower()
#     if(c_choice == p_choice):
#         total_play += 1
#         quit
#     elif(c_choice == 'rock' & p_choice == "scissor"):
#         c_win += 1
#         total_play += 1
#         return c_win

#     elif(c_choice == 'paper' & p_choice == 'rock'):
#         c_win += 1
#         total_play += 1
#         return c_win
#     elif(c_choice == 'scissor' & p_choice == 'paper'):
#         c_win += 1
#         total_play += 1
#         return c_win
#     else:
#         p_win += 1
#         total_play += 1
#         return p_win
    
# c_win = 0
# p_win = 0
# total_play = 0

# choice = input('You wanna play rock paper scissor(yes/no):  ').lower()
# if choice == 'yes':
#     while True:
#         play()
# elif choice == 'no':
#     quit()
# else:
#     print("invalid choice")
