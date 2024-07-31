# 3. Dictionary where each account number is the key, and the value is a tuple containing the balance and a set of recent transactions
accounts = {
    "ACC123": (5000.00, {"Deposit $1000", "Withdraw $500"}),
    "ACC124": (1500.00, {"Deposit $1500"}),
    "ACC125": (3000.00, {"Withdraw $1000", "Deposit $2000"}),
    "ACC126": (7000.00, {"Deposit $7000"}),
    "ACC127": (1000.00, {"Withdraw $500", "Deposit $1500"}),
    "ACC128": (2000.00, {"Deposit $2000"})
}
print("\nDictionary of accounts (account number -> (balance, transactions)):")
for acc_num, acc_details in accounts.items():
    print(f"{acc_num}: Balance {acc_details[0]}, Transactions: {acc_details[1]}")

# 4. Creating a set of all unique transactions across all accounts
all_transactions = set()
for acc_details in accounts.values():
    all_transactions.update(acc_details[1])

print("\nSet of all unique transactions:", all_transactions)

# 5. Creating a dictionary where each transaction type is the key, and the value is a list of account numbers where that transaction occurred
transaction_accounts = {transaction: [] for transaction in all_transactions}
print(transaction_accounts)

# for acc_num, acc_details in accounts.items():
#     for transaction in acc_details[1]:
#         transaction_accounts[transaction].append(acc_num)

# print("\nDictionary of transactions with list of account numbers where it occurred (transaction -> accounts):")
# for transaction, acc_list in transaction_accounts.items():
#     print(f"{transaction}: {acc_list}")

