import csv
import requests
from fake_useragent import HTTPStatus, UserAgent


def get_websites(csv_path:str) -> list[str]:
    websites:list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1] or 'https://':
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
    return websites


def get_useragent() -> str:
    ua = UserAgent()
    return ua.chrome


def get_status_description(status_code:int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'

            return description
    return '(???) Unknown status code'


def check_website(website:str, useragent):
    try:
        code:int = requests.get(website, headers={'User-Agent: ' : useragent}).status_code
        print(website, get_status_description(code))
    except:
        print(f'***Could not get information about the website {website}')

def main():
    sites:str = get_websites('websites.csv')
    useragent:str = get_useragent()

    for site in sites:
        check_website(site, useragent)


if __name__ == '__main__':
    main()
