import requests

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('restcountries_key')

url = "https://restcountries.com/v3.1/all"

def get_data():
    response = requests.get(url = url)
    print(response.status_code)
    # print(response.json())
    print(type(response.json()))

    for item in response.json():
        for key, value in item.items():
            print(f'{key}: {value}')
            print('---------------------------------------')
        print('#############################################')

def post_data():
    pass

def put_data():
    pass

def delete_data():
    pass

def main():
    get_data()

main()