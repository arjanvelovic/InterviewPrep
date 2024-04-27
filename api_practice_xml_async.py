import requests
import xml.etree.ElementTree as ET
import asyncio
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('weatherapi_key')


def get_data(location):
    # call api_key from secured/hidden file location
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'

    response = requests.get(url)
    # check if response is json or xml, and check status code
    # print(response.headers)

    if response.ok:
        if response.headers['Content-Type'] == 'application/json':
            body = response.json()
            # print(body)
            if 'location' in body and 'name' in body['location']:
                location_name = body['location']['name']
                print('Location: ',location_name)
            if 'current' in body and 'temp_f' in body['current']:
                current_temp = body['current']['temp_f']
                print('Current Temp:', current_temp)
            if 'current' in body and 'precip_in' in body['current']:
                percip = body['current']['precip_in']
                print('Percip:', percip)
        else:
            # TODO - handle different content-type
            print('Not a json')
    else:
        # in production add logger and log error to file
        print('Error:', response.status_code)

def get_data_xml(location):
    # call api_key from secured/hidden file location
    url = f'http://api.weatherapi.com/v1/current.xml?key={api_key}&q={location}'

    response = requests.get(url)
    # print(response.headers)

    if response.ok:
        if response.headers['Content-Type'] == 'text/xml':
            tree = ET.fromstring(response.content)

            # prints elements from tree by using tag
            # for elem in tree:
            #     print(elem.tag, elem.text)
            #     for elem2 in elem:
            #         print(elem2.tag, ':', elem2.text)
        
            for elem in tree:
                for elem2 in elem:
                    if elem2.tag == 'name':
                        print('Location:',elem2.text)
                    if elem2.tag == 'temp_f':
                        print('Temp:',elem2.text)
                    if elem2.tag == 'precip_in':
                        print('Percip:',elem2.text)
        else:
            # TODO - handle different content-type
            print('Not a xml')
    else:
        # in production add logger and log error to file
        print('Error:', response.status_code)


async def get_data_async(location):
    # call api_key from secured/hidden file location
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q='

    async with aiohttp.ClientSession() as session:
        print('Starting api search for ', location)
        async with session.get(url+location) as response:
            if response.ok:
                return True
                body = response.json()
                print(body)
            else:
                # in production add logger and log error to file
                print(response.status)


def user_input():
    location_input = input('Location?\n')

    while location_input.replace(" ","").isalpha() == False:
        location_input = input('Try again\n')

    get_data_xml(location_input.strip())
    # get_data(location_input.strip())

async def main():
    user_input()
    await asyncio.gather(
        get_data_async('New York'),
        get_data_async('London'),
    )

asyncio.run(main())
