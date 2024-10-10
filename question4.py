
def saccoTransactions():

    accountBalance = 0
    run = 1

    while run ==1:

        print("\nWelcome to, WITU Academy sacco.")

        #menu
        print('1. Deposit money')
        print('2. withdraw money')
        print('3. check balance')


    studentChoice = int(input("Enter your selection(1,2,3): "))

    #performing the transaction basing on the student selection
    if studentChoice == 1:
        print('\n...processing a deposit transaction...')
    depositAmount = int(input("Enter amount to be deposited: "))

        #check if deposit amount is less than 1000
    if depositAmount < 1000:
        print('\nMinimum deposit is 1000')

    else:
     accountBalance += depositAmount
     print(f"Dear student, you have deposited {depositAmount:,} and your new account balance is {accountBalance:,}")

    if studentChoice == 2:
     print('\n...processing a withdrawing transaction...')
    withdrawAmount = int(input("Enter amount to be withdraw: "))

    if accountBalance ==0:
        print("your balance is 0")

    elif withdrawAmount < 500:
        print("Minimum withdraw amount is 500")

    elif  withdrawAmount > accountBalance:
        print(f"withdraw failed, insufficient funds")

    else:
        accountBalance -= withdrawAmount
        print(f'Dear student, you have withdrawn {withdrawAmount:,} and your new balance is {accountBalance}')

    if studentChoice == 3:
        print(f'Your account balance is {accountBalance:,}')

    else:
     print("you entered a wrong choice !! please select 1,2 or 3\n")
     run = int(print("Enter 1 to continue or ant number to exit: "))

     if run!=1:
        print("Thanks for using our sacco")
        
    saccoTransactions()