def boy():
    age = int(input("Enter the boy's age:"))
    if age > 21:
        print("Eligible to get married") 
    else:
        print("Not yet eligible to get married")
        
    

def girl():
    age = int(input("Enter the girl's age: "))
    if age > 18:
        print("Eligible to get married") 
    else:
        print("Not yet eligible to get married")

        
op = [boy , girl, quit]
gender = int(input(""" What is the gender of the person whose marriage eligibility to be checked:
1.Boy
2.Girl
3.Quit
"""))
if gender > 3 or gender < 1:
    print("Invalid input")
    quit
else:
    if op[gender-1] not in op:
        print("Invalid input")
        quit
    else:
        op[gender-1]()
      