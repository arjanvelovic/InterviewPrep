import asyncio
import aiohttp
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv

load_dotenv()
weatherapi_key = os.getenv('weatherapi_key')

async def async_get(location):
    url = f'http://api.weatherapi.com/v1/current.json?key={weatherapi_key}&q='

    async with aiohttp.ClientSession() as session:
        async with session.get(url+location) as response:
            if response.ok: 
                body = await response.text()
                print(body)
            else:
                print(response.status)

async def async_post(color):
    url = "https://vehicle-z65p.onrender.com/api/vehiclesapi"
    vehicleapi_key = os.getenv('vehicleapi_key')

    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'x-access-token': "Bearer " + vehicleapi_key
        }
    
    vehicle_info = {
        'year': '2024',
        'make': 'Tesla',
        'model': 'Model X',
        'trim': 'Basic',
        'color': color,
        'cost': 40000
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url = url, headers = headers, json = vehicle_info) as response:
            if response.ok: 
                body = await response.json()
                print(body)
            else:
                print(response.status)

async def async_xml_get(location):
    url = f'http://api.weatherapi.com/v1/current.xml?key={weatherapi_key}&q='

    async with aiohttp.ClientSession() as session:
        async with session.get(url+location) as response:
            if response.ok:
                print(response.headers['Content-Type'])
                print(await response.text())
                body = await response.text()
                # tree = ET.fromstring(body)

                # for elem in tree:
                #     print(elem.tag, elem.text)
                #     for elem2 in elem:
                #         print(elem2.tag, elem2.text)

                # for elem in tree:
                #     for elem2 in elem:
                #         if elem2.tag == 'name':
                #             print(elem2.tag, elem2.text)
                #         if elem2.tag == 'temp_f':
                #             print(elem2.tag, elem2.text)
                #         if elem2.tag == 'pressure_in':
                #             print(elem2.tag, elem2.text)
            else:
                print(response.status)
        
async def main():
    # await asyncio.gather(
    #     async_get('New York'),
    #     async_get('Miami'),
    #     async_get('Orlando')
    # )
    await asyncio.gather(
        async_xml_get('New York'),
        # async_xml_get('Miami'),
        # async_xml_get('Orlando')
    )
    # await asyncio.gather(
    #     async_post('Orange'),
    #     async_post('Yellow'),
    #     async_post('Black'),
    # )

asyncio.run(main())