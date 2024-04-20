import requests
import os
import platform
import logging

if platform.system() == 'Windows':
    platform_clear = 'cls'
else:
    platform_clear = 'clear'

def clear_terminal():
    os.system(platform_clear)

clear_terminal()

year = '2024'
make = 'Tesla'

def error_codes(status_code):
    status_code_errors = {
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        408: 'Timeout',
        500: 'Internal Server Error',
        500: 'Bad Gateway',
    }

    print(f'{status_code} Error: {status_code_errors[status_code]}')

# Logging Config
logging.basicConfig(filename='api_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    
def get_vehicles(url, headers, page, per_page):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # pagination
        all_vehicles = response.json()[page*per_page : (page*per_page) + per_page]
        
        for vehicle in all_vehicles:
            print(f"{vehicle['year']} {vehicle['make']}, {vehicle['model']} {vehicle['trim']}, {vehicle['color']}: ${vehicle['cost']}")
            print("---------------------------------------------")
    else:
        logging.error(f"API call to {url} failed: {response.status_code} Error")
        error_codes(response.status_code)
        return None
    
    
def post_vehicle(url, headers):
    model = input('Type the model you want:\n')
    print('---------------------------')
    trim = input('Type the trim you want:\n')
    print('---------------------------')
    color = input('Type the color you want:\n')
    print('---------------------------')
    cost = int(input('Type the cost you want:\n$'))
    print('---------------------------')

    vehicle_info = {
        'year': year,
        'make': make,
        'model': model,
        'trim': trim,
        'color': color,
        'cost': cost
    }

    response = requests.post(url=url, headers=headers, json=vehicle_info)

    if response.status_code == 200:
        new_vehicle = response.json()
        print(f"New vehicle created: {new_vehicle}")
    else:
        logging.error(f"API call to {url} failed: {response.status_code} Error")
        error_codes(response.status_code)
        return None


def get_single_vehicle(url, headers, id):
    response = requests.get(url = url + '/' + id, headers=headers)

    if response.status_code == 200:
        vehicle = response.json()
        return vehicle['model'], vehicle['trim'], vehicle['color'], vehicle['cost']
    else:
        logging.error(f"API call to {url} failed: {response.status_code} Error")
        error_codes(response.status_code)
        return None
    
def update_vehicle(url, headers, id):
    model0, trim0, color0, cost0 = get_single_vehicle(url, headers, id)

    model = input(f'Change model {model0}:\n')
    print('---------------------------')
    trim = input(f'Change trim {trim0}:\n')
    print('---------------------------')
    color = input(f'Change color {color0}:\n')
    print('---------------------------')
    cost = int(input(f'Change cost ${cost0}:\n$'))
    print('---------------------------')

    vehicle_info = {
        'year': year,
        'make': make,
        'model': 'Updated Vehicle',
        'trim': 'Updated Vehicle',
        'color': 'Updated Vehicle',
        'cost': 50000
    }

    response = requests.put(url = url + '/' + id, headers=headers, json=vehicle_info)

    if response.status_code == 200:
        update_vehicle = response.json()
        print(f"Updated vehicle: {update_vehicle}")
    else:
        logging.error(f"API call to {url} failed: {response.status_code} Error")
        error_codes(response.status_code)
        return None
    
    
def delete_vehicle(url, headers, id):
    response = requests.delete(url = url + '/' + id, headers=headers)

    if response.status_code == 200:
        deleted_vehicle = response.json()
        print(f"Deleted vehicle: {deleted_vehicle}")
    else:
        logging.error(f"API call to {url} failed: {response.status_code} Error")
        error_codes(response.status_code)
        return None
    

def user_interface(url, headers, page, per_page, id):
    main_menu = input('''Welcome to the Tesla dealership!
Please select a following option:
1)see vehicles 2)create vehicle 3)update vehicle 4)delete vehicle
-----------------------------------------------------------------
''')
    clear_terminal()

    if main_menu == '1':
        get_vehicles(url, headers, page, per_page)
    elif main_menu == '2':
        post_vehicle(url, headers)
    elif main_menu == '3':
        update_vehicle(url, headers, id)
    elif main_menu == '4':
        delete_vehicle(url, headers, id)

def main():
    url = "https://vehicle-z65p.onrender.com/api/vehiclesapi"
    api_token = '682b0fadb5b82904c2f815d804124fe781eb14fdf620d41f'

    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'x-access-token': "Bearer " + api_token
        }

    page = 1
    per_page = 5
    id = 'GHRjttk_VY2iRuLKRakLrrxUgj9BOy2Dqf5yNuX6cpg'

    user_interface(url, headers, page, per_page, id)

main()

 