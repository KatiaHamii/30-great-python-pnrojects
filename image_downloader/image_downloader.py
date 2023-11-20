import  os
import requests


def get_extention(image_url:str ) -> str | None:
    extentions: list[str] = ['.png', '.jpeg', 'jpg', '.gif', '.svg']
    for ext in extentions:
        if ext in image_url:
            return ext


def download_image(image_url:str, name:str, folder: str=None):
    if ext := get_extention(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extention could not be located...')

    if os.path.isfile(image_name):
        raise Exception('File name already exists...')

    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloading : "{image_name}" successfully!')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    with open('image_urls.txt', mode='r') as urls:
        for i, url in enumerate(urls):
            img_name = "image_"+str(i)
            download_image(url, name=img_name, folder='images')

    #input_url :str = input("Enter an url: ")
    #input_name: str = input("Enter a name for yout image: ")
    #download_image(input_url, name=input_name, folder='images')




