import os
import time
import pyperclip
import pyautogui

def copy_text_to_clipboard(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            text = line.strip()  # Read and strip each line individually
            pyperclip.copy(text)
            print(f"Line '{text}' copied to clipboard successfully.")

            paste_to_application_area()
            time.sleep(5)  # Delay to ensure paste operation completes
            
            push_button_in_application()
            time.sleep(5)  # Delay of 2 seconds between each line
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except IOError as e:
        print(f"Error: An error occurred while reading the file at '{file_path}': {e}")
    except pyperclip.PyperclipException as e:
        print(f"Error: Failed to copy text to clipboard: {e}")

def paste_to_application_area():
    try:
        # Simulate clearing previous content in the application area (adjust as per your application)
        # Example: Using pyautogui to simulate Ctrl+A (select all) and Backspace (delete)
        pyautogui.hotkey('ctrl', 'a')  # Select all
        pyautogui.press('backspace')   # Delete
        
        # Simulate pasting from clipboard (adjust as per your application)
        pyautogui.hotkey('ctrl', 'v')  # Paste from clipboard
        print("Text pasted into application area successfully.")
    except Exception as e:
        print(f"Error: Failed to paste into application area: {e}")

def push_button_in_application():
    try:
        # Simulate clicking the button within the application (adjust coordinates as per your application)
        button_x, button_y = 600, 400  # Example coordinates, adjust based on your application
        pyautogui.click(button_x, button_y)
        print("Button clicked successfully.")
    except Exception as e:
        print(f"Error: Failed to click button in application: {e}")

def main():
    file_path = r'C:\Amit\Python\PL99999999output.txt'  # Replace with your actual file path

    copy_text_to_clipboard(file_path)

    print("Process completed.")

if __name__ == "__main__":
    main()
