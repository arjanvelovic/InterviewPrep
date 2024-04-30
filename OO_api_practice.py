import requests
import xml.etree.ElementTree as ET
import asyncio
import aiohttp

class APIClient:
    const = 'this is a const attribute'
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params = None, headers = None):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url, params = params, headers = headers)
        if response.ok:
            if response.headers['content-type'] == 'application/json':
                return response.json()['current']['temp_f']
            elif response.headers['content-type'] == 'text/xml':
                body = response.content
                tree = ET.fromstring(body)

                for elem in tree:
                    for elem2 in elem:
                        if elem2.tag == 'name':
                            print(elem2.tag, elem2.text)
                        elif elem2.tag == 'temp_f':
                            print(elem2.tag, elem2.text)
                        elif elem2.tag == 'humidity':
                            print(elem2.tag, elem2.text)
            else:
                body = response.text
                print(body)
        else:
            # TODO add logger
            print(response.status_code)

    async def get_async(self, endpoint, params = None, headers = None):
        url = f'{self.base_url}/{endpoint}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params = params, headers = headers) as response:
                if response.ok:
                    if response.headers['content-type'] == 'application/json':
                        json = await response.json()
                        print(json)
                    elif response.headers['content-type'] == 'text/xml':
                        body = await response.content
                        tree = ET.fromstring(body)

                        for elem in tree:
                            for elem2 in elem:
                                if elem2.tag == 'name':
                                    print(elem2.tag, elem2.text)
                                elif elem2.tag == 'temp_f':
                                    print(elem2.tag, elem2.text)
                                elif elem2.tag == 'humidity':
                                    print(elem2.tag, elem2.text)
                    else:
                        body = await response.text
                        print(body)
                else:
                    # TODO add logger
                    print(response.status)
    

def main():

    cities = ['New York', 'London', 'Seattle', 'Miami', 'Munich']
    api_client = APIClient('http://api.weatherapi.com')

    params_london = {'q':'london'}
    paramscheck = api_client.get(f'v1/current.json?key={api_key}', params = params_london)
    print(paramscheck)

    # cities_temp = {}
    # max_temp = 0
    # max_temp_city = None

    # for city in cities:
    #     temp = api_client.get(f'v1/current.json?key={api_key}&q={city}')
    #     if temp > max_temp:
    #         max_temp = temp
    #         max_temp_city = city
    #     cities_temp[city] = temp

    # print(max_temp_city, max_temp)
    # print(cities_temp)

    # print(api_client.__dict__.items())

# async def main_async():
#     api_client = APIClient('http://api.weatherapi.com')

#     await asyncio.gather(
#         api_client.get_async(f'v1/current.json?key={api_key}&q=london'),
#         api_client.get_async(f'v1/current.json?key={api_key}&q=new york'),
#         api_client.get_async(f'v1/current.json?key={api_key}&q=seattle'),
#     )

main()

# asyncio.run(main_async())