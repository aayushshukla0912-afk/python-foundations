account_1 = { 
    "name": 0,
    "age": 0,
    "initial_deposit": 0.0
}
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
initial_deposit = float(input("Please enter your initial deposit amount: "))
account_1["name"] = name
account_1["age"] = age
account_1["initial_deposit"] = initial_deposit
while True:
    print("What would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter the number of your choice: ")
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        continue
    elif choice == "1":
        deposit_amount = float(input("Enter deposit amount: "))
        if deposit_amount < 0.0:
                    print("Error. Please enter a valid amount.")
        account_1["initial_deposit"] += deposit_amount
        print(f"Deposited ${deposit_amount}. New balance is ${account_1['initial_deposit']}")
    elif choice == "2":
        withdraw_amount = float(input("Enter withdrawal amount: "))
        if withdraw_amount > account_1["initial_deposit"]:
            print("Insufficient funds.")
        elif withdraw_amount < 0.0:
            print("Error. Please enter a valid amount.")
        else:
            account_1["initial_deposit"] -= withdraw_amount
            print(f"Withdrawed ${withdraw_amount}. New balance is ${account_1["initial_deposit"]}.")
    elif choice == "3":
        print(f"Current balance is ${account_1["initial_deposit"]}.")
    elif choice == "4":
        print("Thank you for banking with us. See you again!")
        break