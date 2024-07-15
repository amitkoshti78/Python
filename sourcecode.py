def input(prompt=None):
    """
    Read a string from standard input. The trailing newline is stripped.
    If the user hits EOF (End Of File), raise EOFError.
    The prompt string, if given, is printed to standard output without a trailing newline before reading input.
    """
    if prompt is not None:
        print(prompt, end='', flush=True)
    
    line = ''
    while True:
        try:
            char = sys.stdin.read(1)  # Read one character at a time
            if char == '\n':
                break
            line += char
        except EOFError:
            if line == '':
                raise EOFError('EOF when reading a line')
            break
    
    return line

import sys

# This would be a test of the input function
# Usage example
try:
    user_input = input("Enter something: ")
    print(f'You entered: {user_input}')
except EOFError:
    print('EOFError caught: No input received')
