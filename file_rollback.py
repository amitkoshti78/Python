import shutil   # to create backup files by copying orignal files into backup files
import os       # to delete backup files
import datetime
import logging
import uuid    # to generate unique id

# Paths to account files
account_a = 'account_a.txt'
account_b = 'account_b.txt'

# Create backup files
backup_a = 'account_a_backup.txt'
backup_b = 'account_b_backup.txt'

#2024-09-27 15:59:40,976 - Transaction e2fd423c-2ce9-45-20240927155940: Debit 100 from 1234567890, Credit 100 to 9876543210 - Success
#2024-09-27 15:59:40,991 - Transaction a3bf4221-59ba-4f-20240927155940: Failed - Error while crediting Account B!
# Configure logging
logging.basicConfig(filename='transaction_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


# Function to generate a unique transaction ID with timestamp
def generate_transaction_id():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4())[:16]  # Generate a short unique ID (first 16 characters)
    return f"{unique_id}-{timestamp}"


# Function to read the account details (balance, account number, account name)
def get_account_details(file_name):
    with open(file_name, 'r') as file:
        account_data = file.readlines()
        # Assuming the file has 3 lines: account number, account name, and balance
        account_number = account_data[0].strip()
        account_name = account_data[1].strip()
        balance = float(account_data[2].strip())
        return account_number, account_name, balance


# Function to update the balance in the file (without altering account number and name)
def update_balance(file_name, new_balance):
    with open(file_name, 'r') as file:
        account_data = file.readlines()
    account_data[2] = f"{new_balance:.2f}\n"  # Update balance line
    with open(file_name, 'w') as file:
        file.writelines(account_data)


# Function to log the transaction
def log_transaction(transaction_id, status, debit_account=None, credit_account=None, debit_amount=None,
                    credit_amount=None, error_message=None):
    if status == 'success':
        logging.info(
            f"Transaction {transaction_id}: Debit {debit_amount} from {debit_account}, Credit {credit_amount} to {credit_account} - Success")
    else:
        logging.error(f"Transaction {transaction_id}: Failed - {error_message}")


# Function to verify account details (account number and name)
def verify_account(account_number, account_name, file_name):
    file_account_number, file_account_name, _ = get_account_details(file_name)
    return account_number == file_account_number and account_name == file_account_name


# Function to perform the transaction (debit from account A, credit to account B)
def perform_transaction(debit_account_number, debit_account_name, debit_amount, credit_account_number,
                        credit_account_name, credit_amount):
    transaction_id = generate_transaction_id()  # Generate unique transaction ID
    try:
        # Step 1: Backup original files
        shutil.copy(account_a, backup_a)
        shutil.copy(account_b, backup_b)

        # Step 2: Verify account details
        if not verify_account(debit_account_number, debit_account_name, account_a):
            raise ValueError("Debit Account verification failed!")

        if not verify_account(credit_account_number, credit_account_name, account_b):
            raise ValueError("Credit Account verification failed!")

        # Step 3: Read current balances
        _, _, balance_a = get_account_details(account_a)
        _, _, balance_b = get_account_details(account_b)

        print(f"Initial Balance A: {balance_a}")
        print(f"Initial Balance B: {balance_b}")

        # Step 4: Perform debit and credit
        # Debit from Account A
        if balance_a < debit_amount:
            raise ValueError("Insufficient funds in Account A!")

        balance_a -= debit_amount
        update_balance(account_a, balance_a)

        # Simulate an error during the credit operation (optional)
        if credit_amount == -1:  # Forcing an error to simulate rollback
            raise Exception("Error while crediting Account B!")

        # Credit to Account B
        balance_b += credit_amount
        update_balance(account_b, balance_b)

        print(f"New Balance A: {balance_a}")
        print(f"New Balance B: {balance_b}")

        # Step 5: Log success
        log_transaction(transaction_id, 'success', debit_account_number, credit_account_number, debit_amount,
                        credit_amount)

    except Exception as e:
        # Step 6: Rollback in case of error
        print(f"Transaction failed: {e}. Rolling back changes...")
        shutil.copy(backup_a, account_a)  # Restore Account A
        shutil.copy(backup_b, account_b)  # Restore Account B

        # Log failure
        log_transaction(transaction_id, 'failure', debit_account_number, credit_account_number, error_message=str(e))

    finally:
        # Clean up backup files
        if os.path.exists(backup_a):
            os.remove(backup_a)
        if os.path.exists(backup_b):
            os.remove(backup_b)


if __name__ == '__main__':
    # Initial account data in the files (for demonstration purposes)
    # Format: [Account Number, Account Name, Balance]
    with open(account_a, 'w') as f:
        f.write('1234567890\nJohn Doe\n1000.00')

    with open(account_b, 'w') as f:
        f.write('9876543210\nJane Smith\n500.00')

    # Test the transaction with a successful operation
    print("Performing successful transaction:")
    perform_transaction(debit_account_number='1234567890', debit_account_name='John Doe', debit_amount=100,
                    credit_account_number='9876543210', credit_account_name='Jane Smith', credit_amount=100)

    # Test the transaction with a forced failure (rollback scenario)
    print("\nPerforming transaction with a failure (forced rollback):")
    perform_transaction(debit_account_number='1234567890', debit_account_name='John Do', debit_amount=100,
                    credit_account_number='9876543210', credit_account_name='Jane Smith',
                    credit_amount=-1)  # Simulate failure

