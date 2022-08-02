def add():
    name = input("name: ")
    pwd = input('password: ')
    with open('pfile.txt','a') as f:
        f.write(name + "|" + pwd +"\n")

def view():
    with open("pfile.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            n , d = data.split('|')
            print(f"Name: {n}  |  Password: {d}")
        

master_pwd = 123456
for i in range(3):
    m_password = input('Enter the master password: ')
    if m_password != str(master_pwd):
        p=2
        p -=i
        if p>0:
            print(f"{p} chance left ")
            continue
        else:
            print("Bye!")
        
    else:
        while True:
            choice = input('What action you wanna perform(view/add/quit): ').lower()
            if choice == "quit":
                break
            if choice == "view":
                view()
            if choice == "add":
                add()
            else:
                print("invalid entry")
                continue
            