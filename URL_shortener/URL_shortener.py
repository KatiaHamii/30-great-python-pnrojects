from typing import Final
import requests

API_KEY: Final[str] = 'xcyfsdkmvsdjngösadm'
BASE_URL: Final[str] = 'https://cit.ly/api/api.php'


def shorten_lim(full_link: str):

    payload: dict = {'key':API_KEY, 'short': BASE_URL}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        if url_data['status'] ==7:
            short_link: str = url_data['shortLink']
            print('Link: ', short_link)
        else:
            print('Error status: ', url_data['status'])


def main():
    input_link: str = input('Enter your link: ')
    shorten_lim(input_link)


if __name__ == '__main__':
    main()