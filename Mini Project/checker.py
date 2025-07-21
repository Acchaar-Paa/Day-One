balance = 5000
c = 2
user = c
if user == 2:
    user = int(input("Add Value := "))
    balance = user+balance
    # history.append(f"Deposit : {balance}")
    print(balance)
    print(" Main_Menu")
elif user == 3:
    user = int(input("Subtract Value := "))
    if user <= balance:
        balance = balance-user
        # history.append(f"Withdraw : {balance}")
        print( balance)
        print(" Main_Menu")
    else:
        print( "You Put High Amount")
        print(" Main_Menu")
else:
    print( "You Write Wrong")
    print(" Main_Menu")