from banking_functions import BankingFunctions

def main():

    bankingFuncObj = BankingFunctions()

    choice = 1

    while choice != 0:

        print("--- Main Menu --- ")
        print("1. Sign Up (New Customer) ")
        print("2. Sign In (Existing Customer) ")
        print("3. Admin Sign In ")
        print("0. Quit ")

        try:
            choice = int(input())

        except Exception as e:
            print("Invalid Choice")
            choice = 1
            continue

        if choice == 1:
            ''' Write Sign Up Logic of Customer'''
            bankingFuncObj.sign_up()
            # Pass

        elif choice == 2:
            '''Write Sign In Logic of Customer'''
            print("Adding the sign in logic")

        elif choice == 3:
            '''Write Admin Sign In Logic'''

        elif choice == 0:
            print("Application Closed")

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()