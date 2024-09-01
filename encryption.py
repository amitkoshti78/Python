# program to encrypt and descrypt message

#https://ascii.co.uk/

import random

logo = '''
________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/

'''
print(logo)

letters = [' ', 'A', 'B', 'C', 'D','E', 'F', 'G', 'H','I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P','Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd','e', 'f', 'g', 'h','i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p','q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

#25 + 1 = 26
#26 - 25 = 1

def fun_encrypt_msg(message):
    
    new_message = ""
    random_index = random.randint(1,len(letters))
    for alphabet in message:
        
        if alphabet == ' ':
            new_message = new_message + " "
        else:    
            letter_index = letters.index(alphabet)
            final_index = random_index + letter_index
            if final_index > len(letters):
                final_index = final_index - len(letters)
                
            new_message =  new_message + letters[final_index]      
        
    return new_message.strip(), random_index

def fun_decrypt_msg(message, random_index):
    new_message = ""
    
    for alphabet in message:
        
        if alphabet == ' ':
            new_message = new_message + " "
        else:    
            letter_index = letters.index(alphabet)
            final_index = random_index - letter_index
            if final_index < 1 :
                final_index = final_index + len(letters)
                
            new_message =  new_message + letters[final_index]      
        
    return new_message.strip()

    
def main():
    
    message = input("Enter a message : ")
    
    print("Your message is : ", message)
    
    encrypt_msg, random_index = fun_encrypt_msg(message.strip())
    
    print("Encrypted message is :", encrypt_msg)
    
    decrypt_message = fun_decrypt_msg(encrypt_msg, random_index)
    
    print(decrypt_message)
        
if __name__ == "__main__":
    main()