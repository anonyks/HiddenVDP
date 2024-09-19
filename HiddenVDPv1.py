import os
import requests
from multiprocessing import Pool
from colorama import Fore, Style

def screen_clear():
    """Clear the terminal screen."""
    os.system('cls')

# Constants for stylizing the output
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

# HTTP request headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

def check_url(star, file_name, path):
    """Check the specified URL and log if a specific contact info is found."""
    url = f"http://{star.strip() if '://' not in star else star.strip()}/{path}"
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if "Contact: " in response.text:
            print(f"{path} {gr}OK{res} => {url}\n")
            with open(file_name, "a") as file:
                file.write(f'{url}\n')
        else:
            print(f"{red}Not{res} {path} => {url}\n")
    except requests.RequestException:
        print(f"Error accessing {url}")

def filter(star):
    """Process each URL for both well-known and regular security checks."""
    check_url(star, "well-known.txt", ".well-known/security.txt")
    check_url(star, "security.txt", "security.txt")

def main():
    """Main function that initializes the script execution."""
    print(f"Coded by {yl}@AnonyKs_xD{res} on Telegram: {yl}@AnonyKs_xD{res}\n")
    list_path = input(f"{gr}Provide Your List.txt/{red}> {gr}${res} ")
    try:
        with open(list_path, 'r', encoding="utf-8") as file:
            stars = file.readlines()
        pool = Pool(15)
        pool.map(filter, stars)
        pool.close()
        pool.join()
    except Exception as e:
        print(f"Failed to process list: {e}")

if __name__ == '__main__':
    screen_clear()
    main()
