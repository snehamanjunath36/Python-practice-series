def triangle():
     h = int(input("Enter the height: "))
     b = int(input("Enter the breath: "))
     area = (1/2) * b * h
     print(f'Area of the given triangle is: {area}sq units')

def square():
    s = int(input("Enter the length of a side of the square: "))
    area = s ** 2
    print(f'Area of the given Square is: {area}sq units')

def rectangle():
    h = int(input("Enter the height: "))
    l = int(input("Enter the length: "))
    area = l * h
    print(f'Area of the given rectangle is: {area}sq units')

def circle():
    s = int(input("Enter the radius of the Circle: "))
    pi = 3.141
    area =pi * (s ** 2)
    print(f'Area of the given Circle is: {area}sq units')

def err():
    return("Invalid input")


choice = int(input('''
1.Triangle
2.Square
3.Rectangle
4.Circle
Which among the above is your geometric object whose area has to be found: ''').lower())

op = {
    1:triangle,
    2:square,
    3:rectangle,
    4:circle
}
op.get(choice,err)()
