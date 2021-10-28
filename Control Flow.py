# Developer: Colton Ludmer
# Date: 10/11/21
# Program: ATM Bank Transaction

"""
This program simulates an ATM utilizing If, Elif, and Else statements
Nesting If statements and refresh our Comparison and Logical Operators
"""

print("Welcome to Cash-R-Us Bank\n\nLet's take a moment to set up your account.\n")

# Set up account by asking users for their first and last names using Variables
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

print("\nWelcome to Cash-R-Us", first_name, last_name + ", we will now set up a security PIN on your account.\n")

# Set up a PIN - Personal Identification Number
pin = input("Please choose a 4-digit Personal Identification Number: ")

print("\nThank you", first_name + ", we see that you set your PIN to", pin)

# Transaction
print("\nWould you like to make a transaction through our Automated Teller Machine?")
atm = input("Yes or No?: ").lower()

if atm == "yes":
    print("\n*************************************************************\n")

    # This part of the program will be asking users to complete a transaction through the ATM
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM", first_name, last_name, "\n")
    userPIN = input("What is your 4 digit PIN?: ")

    # If the pin is correct it shows the users balance
    if userPIN == pin:
        balance = 674
        print("\nYour Balance: $" + str(balance))

        # Ask users what type of transaction they want to make: Withdrawal or Deposit
        type_of_transaction = input("\nWould you like to make a withdrawal or deposit?\nW = Withdrawal or D = Deposit: ").lower()
        
        if type_of_transaction == "w":
            wAmount = int(input("\nHow much money would you like to withdraw?: "))
            balance = balance - wAmount
            print("Your new balance is: $" + str(balance))
            
    else:
        print("\nSorry", first_name + ", that PIN is incorrect")

else:
    print("\nHave a wonderful day", first_name, last_name + ", please come back and visit soon!")
