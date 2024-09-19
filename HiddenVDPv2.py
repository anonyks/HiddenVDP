import os
import requests
from multiprocessing import Pool
from colorama import Fore, Style


def screen_clear():
    """Clear the console screen."""
    _ = os.system('cls')


# Configuration for requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'
}
keywords = [
    "disclose", "disclosure", "responsible", "vulnerability", "bugbounty", "hackerone", "bugcrowd", "intigriti",
    'acknowledgments', 'acknowledgment', 'coordinated'
]

# Color settings
bl, wh, gr, red, res, yl = Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.RED, Style.RESET_ALL, Fore.YELLOW


def check_url(star, path):
    """Check a URL to see if it contains any of the specified security keywords."""
    formatted_url = f"http://{star}" if "://" not in star else star.strip()
    url = f"{formatted_url}/{path}"
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if any(keyword.lower() in response.text.lower() for keyword in keywords):
            print(f"{path} {gr}OK{res} => {formatted_url}\n")
            with open("Found.txt", "a") as file:
                file.write(f'{url}\n')
        else:
            print(f"{red}Not{res} {path} => {formatted_url}\n")
    except requests.RequestException:
        pass


def filter_urls(star):
    """Filter URLs to check for security information."""
    check_url(star, ".well-known/security.txt")
    check_url(star, "security.txt")


def main():
    """Main function to process list of URLs."""
    # Crediting the coder
    print(f"Script developed by: {yl}@AnonyKs_xD{res} - Telegram: {yl}@AnonyKs_xD{res}\n")
    
    list_path = input(f"{gr}Provide Your List.txt/{red}> {gr}${res} ")
    with open(list_path, 'r', encoding="utf-8") as file:
        stars = file.readlines()
    pool = Pool(15)
    pool.map(filter_urls, stars)
    pool.close()
    pool.join()


if __name__ == '__main__':
    screen_clear()
    main()
