# accounts = []
# balances = []
# name = ""
# print("Enter the names and balances of bank accounts (type: quit when done)")
# while name.lower() != "quit":
#     name = input("What is the name of this account?: ")
#     if name.lower() != "quit": 
#         balance = float(input("What is the balance? "))
#         accounts.append(name)
#         balances.append(balance)      
# else:
#     print("\nAccount Information:")
#     for account in accounts:
#         print(f"{account} - ${balances[accounts.index(account)]}")
#     print(f"\nTotal: $" + str(sum(i for i in balances)))
#     print(f"Average: $" + str(sum(i for i in balances) / len(balances)))

# --------------------------------------------------------------------------------------------

# # stretch

# # function added
# def Account_information():
#     print("\nAccount Information:")
#     for account in accounts:
#         print(f"{accounts.index(account)}. {account} - ${balances[accounts.index(account)]}")

# accounts = []
# balances = []
# name = ""
# print("Enter the names and balances of bank accounts (type: quit when done)")
# while name.lower() != "quit":
#     name = input("What is the name of this account?: ")
#     if name.lower() != "quit": 
#         balance = float(input("What is the balance? "))
#         accounts.append(name)
#         balances.append(balance)      
# else:
#     # function called
#     Account_information()
#     print(f"\nTotal: $" + str(sum(i for i in balances)))
#     print(f"Average: $" + str(sum(i for i in balances) / len(balances)))
#     # highest balance added 
#     print("Highest balance: " + str(accounts[balances.index(max(balances))]) + " - $" + str(max(balances)))
#     print()

# # keep looping until user decides to stop updating
# upd = "yes"
# while upd.lower() != "no":
#     upd = input("\nDo you want to update an account? ")
#     if upd.lower() == "yes":
#         ind = int(input("What account index do you want to update?"))
#         new_amount = float(input("What is the new amount? "))
#         balances[ind] = new_amount
#         Account_information()
# else:
#     Account_information()