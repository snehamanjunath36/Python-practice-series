age = int(input("Enter the age of the person: "))
if age > 0:
    if age < 18:
        print("Not eligible to vote")
    else:
        print("Eligible to vote")
else:
    print("Invalid age")