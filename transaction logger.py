print("The Transaction Logger")
history = []
while True:
 transaction = input("Enter your transaction:")
 if transaction == "exit":
  print("Thank you for the visit.")
  break
 elif transaction == "history":
  print("Previous transactions stored:")
  for idx, tx in enumerate(history, start=1):
   print(f"{idx}.{tx}")
 else:
  history.append(transaction)
  print(f"'{transaction}' has been stored in the history.")
 