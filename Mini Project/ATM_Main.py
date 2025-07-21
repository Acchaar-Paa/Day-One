balance=5000
history = []
c= 0
pin = 1234
def login_System():
    user = int(input("enter your 4 digit pin :"))
    i = 3
    while i > 0 :
        i -=1
        if user == pin:
            print("write")
            Main_Menu()
        elif user != pin :
            print("invalid pin")
        else :
            user = int(input(f"now u have only {i} attems enter your 4 digit pin :"))
            print( "Lock Account ")
def Main_Menu():
    global pin
    global c
    user_1 = int(input(f"1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Transaction History\n5. Exit\n6. Change Pin\nChoose :  "))
    while True :
        if user_1 == 1:
            c = 1
            print( f"You Have Current Blance : = {balance}")
            Main_Menu()
        elif user_1 == 2:
            c = 2
            Balance_system()
        elif user_1 == 3:
            c = 3
            Balance_system()
        elif user_1 == 4:
            c = 4
            transaction_history()
        elif user_1 == 5:
            c = 5
            exit_menu()
        elif user_1 == 6:
            c = 6
            user_2 = int(input("What Pin Do You Want Choose : "))
            pin = user_2
            Main_Menu()
def Balance_system():
    global c
    global history
    global balance
    user = c
    if user == 2:
        user = int(input("Add Value := "))
        balance = user+balance
        history.append(f"Deposit : {user}")
        print(balance)
        return Main_Menu()
    elif user == 3:
        user = int(input("Subtract Value := "))
        if user <= balance:
            balance = balance-user
            history.append(f"Withdraw : {user}")
            print( balance)
            Main_Menu()
        else:
            print( "You Put High Amount")
            Main_Menu()
    else:
        print( "You Write Wrong")
        Main_Menu()
def transaction_history():
    global history
    print(history)
    Main_Menu()
def exit_menu():
    user = input(f"No , Yes\nChoose := ")
    if user in ["n","no","NO","No","Y"]:
        Main_Menu()
    elif user in ["y","yes","Yes","YES","Y" ]:
        "Thanks You. Goodbye"
ans = login_System()
print(ans)