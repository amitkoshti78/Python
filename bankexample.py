# Python Program to model a Bank and its Customers using Lists, Sets, Tuples, and Dictionaries

# 1. List of customer names
customers = ["Amit K", "Omkar B", "Neha M", "Avinash B", "Anurag N", "Sakshi G", "Varad N", "Arnav S" ]
print("List of customers:", customers)

# 2. Dictionary where each customer's name is the key, and the value is a tuple with their age and a list of their bank accounts
customer_details = {
    "Amit K": (30, ["ACC123", "ACC124"]),
    "Omkar B": (25, ["ACC125"]),
    "Neha M": (19, ["ACC126", "ACC127"]),
    "Avinash B": (32, ["ACC128"]),
    "Anurag N": (21, ["ACC129", "ACC130"]),
    "Sakshi G": (20, ["ACC131"]),
    "Varad N": (18, ["ACC132", "ACC133"]),
    "Arnav S": (23, ["ACC134"]),
}
print("\nDictionary of customer details (name -> (age, accounts)):")
for customer, details in customer_details.items():
    print(f"{customer}: Age {details[0]}, Accounts: {details[1]}")

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
print("\nDictionary of all unique transactions:", transaction_accounts )

for acc_num, acc_details in accounts.items():
    for transaction in acc_details[1]:
        transaction_accounts[transaction].append(acc_num)

print("\nDictionary of transactions with list of account numbers where it occurred (transaction -> accounts):")
for transaction, acc_list in transaction_accounts.items():
    print(f"{transaction}: {acc_list}")

# 6. Demonstrating the use of tuples to represent the coordinates of branches
branch_locations = {
    "Main Branch": (40.7128, -74.0060),
    "West Branch": (34.0522, -118.2437),
    "East Branch": (51.5074, -0.1278),
}
print("\nDictionary of branch locations (branch -> (latitude, longitude)):")
for branch, coords in branch_locations.items():
    print(f"{branch}: Coordinates {coords}")

# 7. Find customers with accounts having both "Deposit $2000" and "Withdraw $1000" transactions
deposit_2000_accounts = set(transaction_accounts["Deposit $2000"])
withdraw_1000_accounts = set(transaction_accounts["Withdraw $1000"])
common_transaction_accounts = deposit_2000_accounts.intersection(withdraw_1000_accounts)

# Find customers associated with these accounts
customers_with_common_transactions = set()
for customer, details in customer_details.items():
    if any(acc in common_transaction_accounts for acc in details[1]):
        customers_with_common_transactions.add(customer)

print("\nCustomers with accounts that had both 'Deposit $2000' and 'Withdraw $1000':", customers_with_common_transactions)

# 8. Grouping accounts by balance range (e.g., under $2000, $2000-$5000, above $5000)
balance_groups = {"Under $2000": [], "$2000-$5000": [], "Above $5000": []}

for acc_num, acc_details in accounts.items():
    balance = acc_details[0]
    if balance < 2000:
        balance_groups["Under $2000"].append(acc_num)
    elif 2000 <= balance <= 5000:
        balance_groups["$2000-$5000"].append(acc_num)
    else:
        balance_groups["Above $5000"].append(acc_num)

print("\nAccounts grouped by balance range:")
for range_name, acc_list in balance_groups.items():
    print(f"{range_name}: {acc_list}")

# Summary of interconnected data structures
print("\nSummary:")
print("\nCustomers list:", customers)
print("\nCustomer details dictionary:", customer_details)
print("\nAccounts dictionary:", accounts)
print("\nUnique transactions set:", all_transactions)
print("\nTransactions with accounts dictionary:", transaction_accounts)
print("\nBranch locations dictionary:", branch_locations)
print("\nCustomers with both 'Deposit $2000' and 'Withdraw $1000':", customers_with_common_transactions)
print("\nAccounts grouped by balance:", balance_groups)
