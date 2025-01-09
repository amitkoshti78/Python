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
         #  0 .  1    2    3    4   5    6   7     8    9   10   11   12  
           'M', 'N', 'O', 'P','Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z',
        #  13    14   15   16  17   18   19   20  21   22   23   24   25  26   
           'a', 'b', 'c', 'd','e', 'f', 'g', 'h','i', 'j', 'k', 'l','m', 
        #  27    28   29   30  31   32   33   34  35   36   37   38  39   
           'n', 'o', 'p','q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
        #  40   41   42  43   44   45   46  47   48   49    50   51  52

# J 10 + 28 = 38 l
# a 27 + 28 = 55 - 52 = 3 B


def fun_encrypt_msg(message):
    
    new_message = ""
    random_index = random.randint(1,len(letters))
    print("Random Index is : ", random_index)

    for alphabet in message:
        
        if alphabet == ' ':
            new_message = new_message + " "
        else:    
            letter_index = letters.index(alphabet)
            final_index = random_index + letter_index
            if final_index >= len(letters):
                final_index = final_index - len(letters)

                
            new_message =  new_message + letters[final_index]   
            print("Alphabet is : ", alphabet, "Letter Index is : ", letter_index, "Final Index is : ", final_index, "New letter is :", letters[final_index]  )
        
    return new_message.strip(), random_index

def fun_decrypt_msg(message, random_index):
    new_message = ""
    print("Random Index is : ", random_index)
    
    for alphabet in message:
        
        if alphabet == ' ':
            new_message = new_message + " "
        else:    
            letter_index = letters.index(alphabet)
            print("Alphabet is : ", alphabet, "Letter Index is : ", letter_index)
            final_index =  letter_index - random_index
            print("Final Index is : ", final_index)
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
    
    print("Original Message is :", decrypt_message)
        
if __name__ == "__main__":
    main()