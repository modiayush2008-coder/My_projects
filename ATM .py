def atm(account_balance,pin):
    # Chack The Corrct Pin
    attemts = 0

    while attemts < 3:
        pin_input = int(input("Enter The Pin : "))

        if (pin_input == pin):
            print("Pin Is Correct")
            break
        else:
            print("Pin Is Incorrct")
            attemts += 1
        if(attemts == 3):
            print("Account Is Locked")
            return account_balance

          

    # Loop Manu
    while True:
        print("----MANU----")
        print("1. Withdraw")
        print("2. Deposite")
        print("3. Chack Balance")
        print("4. Exit")

        Choice = int(input("Enter Your Choice : "))

    # 1. withdraw
        if (Choice == 1):
            withdraw_input=int(input("Enter The Withdraw Amount: "))
            if (withdraw_input > account_balance):
                print("Balance Is Insufficient!!")
                print(f"Your Acoount Balance is {account_balance}")
            elif (withdraw_input <= 0):
                print("Enter Valid Amount!!!")
            else:
                print(f"You Withdraw {withdraw_input} Ruppes")
                account_balance -= withdraw_input
                print(f"Your Acoount Balance is {account_balance}")   


    # 2.Deposite
        if(Choice == 2):
            Deposite_input=int(input("Enter The Deposite Amount: "))
            if (Deposite_input <= 0):
                print("Enter Valid Amount!!!")
            else:
                print(f"You Withdraw {Deposite_input} Ruppes")
                account_balance += Deposite_input
                print(f"Your Acoount Balance is {account_balance}")


    #3.Check Balance
        if(Choice == 3):
            print(f"Your Balance Is {account_balance}")


    #4.Exit
        if(Choice == 4):
            print("Thank You For Using")
            break
                
account_balance = 7000
pin = 1234
atm(account_balance , pin)
