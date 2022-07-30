def num():
	num1 = int(input('Enter the first number: '))
	num2 = int(input('Enter the second number: '))
	return num1, num2

def add():
	a,b = num()
	return a + b

def sub():
	a,b = num()
	return a - b

def mul():
	a,b = num()
	return a * b

def div():
	a,b = num()
	if(b == 0):
		error()
	else:
		return a / b

def error():
	return "invalid input"

print("""
	1.Add
	2.Subtract
	3.Multiply
	4.Divide
	""")
choice = int(input('Enter your choice: '))

#Using Dictionary it can be done

operation = {
	1:add,
	2:sub,
	3:mul,
	4:div}
ans = str(operation.get(choice , error)())
print("Answer:" + ans)


#Using list it can be done

# op = [add,sub,mul,div]
# output =  op[choice - 1]()
# print("Answer:" + str(output))