#Original Code By Https://github.com/crxel
#His Repo https://github.com/crxel/rats-webhook-spammer/blob/main/wspammer.py
import requests
import time
import os
from colorama import Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    banner = fr"""
{Fore.GREEN + Style.BRIGHT}
   _____ _                _           ____________                                 
  / ____| |              | |         |___  /___  /                                 
 | (___ | |__   ___   ___| | ____  __   / /   / /__  __                            
  \___ \| '_ \ / _ \ / __| |/ /\ \/ /  / /   / / \ \/ /                            
  ____) | | | | (_) | (__|   <  >  <  / /__ / /__ >  <                             
 |_____/|_| |_|\___/ \___|_|\_\/_/\_\/_____/_____/_/\_\                _           
 \ \        / / | |   | |               | |    |  ____|               (_)          
  \ \  /\  / /__| |__ | |__   ___   ___ | | __ | |__ _   _ _ __  _ __  _  ___ _ __ 
   \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ / |  __| | | | '_ \| '_ \| |/ _ \ '__|
    \  /\  /  __/ |_) | | | | (_) | (_) |   <  | |  | |_| | | | | | | | |  __/ |   
     \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |_|   \__,_|_| |_|_| |_|_|\___|_|   
     
"""
    print(banner)

def spam_webhook():
    webhook = input("Enter Webhook URL: ")
    message = input("Enter Message: ")
    data = {"content": message}

    def send_message():
        time.sleep(0.5)
        response = requests.post(webhook, json=data)
        if response.status_code == 200:
            print(f'{Fore.BLUE + Style.BRIGHT}Message sent successfully to {webhook}')
        else:
            print(f'{Fore.GREEN}Message sent successfully to')

    while True:
        send_message()

def delete_webhook():
    webhook = input("Enter Webhook URL to delete: ")
    response = requests.delete(webhook)

    if response.status_code == 204:
        print(f'{Fore.BLUE + Style.BRIGHT}Webhook {webhook} deleted successfully.')
    elif response.status_code == 404:
        print(f'{Fore.RED}Webhook not found.')
    else:
        print(f'{Fore.RED}Failed to delete webhook.')

def main():
    while True:
        print_banner()
        print("Options:")
        print("1. Spam a Webhook")
        print("2. Delete a Webhook")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            spam_webhook()
        elif choice == "2":
            delete_webhook()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print(f'{Fore.RED}Invalid choice. Please enter a valid option.')

if __name__ == "__main__":
    main()
#this code is so fucking sloppy that it gives me cancer, but it somewhat works somehow 😭
