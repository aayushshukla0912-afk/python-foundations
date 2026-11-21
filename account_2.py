account_2 = {
    "account_id": "6741",
    "username": "",
    "age": 0,
    "account_balance": 0.0,
}
username = input("Enter you username: ")
age = int(input("Enter your age: "))
account_balance = float(input("Enter the amount you would like for initial deposit:"))
account_2["username"] = username
account_2["age"] = age
account_2["account_balance"] = account_balance
print(f"Welcome {account_2['username']}! Your current balance is ${account_2['account_balance']}.")
while True: 
    print("Please choose the one of the following options:"
          "1.Deposit",\
          "2.Withdraw",
          "3.Check Balance",
          "4.Exit") 
    option = int(input("Enter your option: "))
    if option < 1 or option > 4:
        print("Invalid option. Please try again.")
    elif option == 1:
        deposit_amount = float(input("Enter the amount you would like to deposit: "))
        account_2["account_balance"] += deposit_amount
        print(f"{deposit_amount} has been deposited to your account. Your new balance is ${account_2['account_balance']}.")
        break
    elif option == 2:
        withdraw_amount = float(input("Enter the amount you would like to withdraw: "))
        if withdraw_amount > account_2["account_balance"]:
            print("Insufficient funds, if you know how to do arithmetic.")
        else:
            account_2["account_balance"] -= withdraw_amount
        print(f"{withdraw_amount} has been withdrawn from you account. Your new balance is ${account_2['account_balance']}.")
        break
    elif option == 3:
        print(f"Your current balance is ${account_2['account_balance']}.")
        break
    elif option == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
