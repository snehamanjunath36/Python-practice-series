choice = input("""Hi!, Welcome to quiz session would you like to take up a quize round 
(y for yes, n for no):  """).lower()

if choice == 'y':
    score = 0
    ans = input('1) Wher is the term "Computer" is derived from? ').lower()
    if ans == "latin":
        score += 1
        print('\tYou got it right !')
    else:
        print('\tYou got it wrong !')

    ans = input('2) Who is the father of computer? ').lower()
    if ans == "charles babbage":
        score += 1
        print('\tYou got it right !')
    else:
        print('\tYou got it wrong !')

    ans = input('3) How many bits does a byte contain? ').lower()
    if ans == '8':
        score += 1
        print('\tYou got it right !')
    else:
        print('\tYou got it wrong !')

    ans = input('4) What does ALU stands for? ').lower()
    if ans == "arithmetic logic unit":
        score += 1
        print('\tYou got it right !')
    else:
        print('\tYou got it wrong !')

    ans = input('5) What does RAM stand for? ').lower()
    if ans == "random access memory":
        score += 1
        print('\tYou got it right !')
    else:
        print('\tYou got it wrong !')
    

    print(f"""\n You scored {score} points!!
     You got {(score/5)*100}%""")

else:
    print("Bye!!")
    quit
