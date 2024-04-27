import requests
import os
import platform
import logging
from dotenv import load_dotenv
load_dotenv()

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


def get_single_vehicle(url, headers, id):
    response = requests.get(url = url + '/' + id, headers=headers)

    if response.status_code == 200:
        vehicle = response.json()
        print(f"{vehicle['year']} {vehicle['make']}, {vehicle['model']} {vehicle['trim']}, {vehicle['color']}: ${vehicle['cost']}")

        vehicle_options = True

        while vehicle_options:
            vehicle_options = input('''Please select an option:
1)updated vehicle 2)delete vehicle 3)quit\n''')
            clear_terminal()
            
            if vehicle_options in ['1', 'one', 'update', 'u', 'update vehicle']:
                update_vehicle(url, headers, id)
                vehicle_options = False
            elif vehicle_options in ['2', 'two', 'delete', 'd', 'delete vehicle']:
                delete_vehicle(url, headers, id)
                vehicle_options = False
            elif vehicle_options in ['3', 'three', 'quit', 'q']:
                vehicle_options = False
            else:
                print('Error - try another option')
                print('---------------------------')
        
    else:
        logging.error(f"API call to {url} failed: {response.status_code} Error")
        error_codes(response.status_code)
        return None


def get_vehicle_for_update(url, headers, id):
    response = requests.get(url = url + '/' + id, headers=headers)

    if response.status_code == 200:
        vehicle = response.json()
        return vehicle['model'], vehicle['trim'], vehicle['color'], vehicle['cost']
    else:
        logging.error(f"API call to {url} failed: {response.status_code} Error")
        error_codes(response.status_code)
        return None   


def get_vehicles(url, headers, page, per_page):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # pagination
        all_vehicles = response.json()[page*per_page : (page*per_page) + per_page]
        vehicle_ids = []
        
        for vehicle in all_vehicles:
            vehicle_ids.append(vehicle['id'])
            print(f"{all_vehicles.index(vehicle)}) {vehicle['year']} {vehicle['make']}, {vehicle['model']} {vehicle['trim']}, {vehicle['color']}: ${vehicle['cost']}")
            print("--------------------------------------------------------")

        vehicle_select = True
        while vehicle_select:
            vehicle_select = input('''Please select a vehicle by number or quit\n''')
            clear_terminal()
            for num in range(per_page):
                if vehicle_select == str(num):
                    get_single_vehicle(url, headers, vehicle_ids[num])
                    vehicle_select = False
            if num in ['q', 'quit']:
                vehicle_select = False

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
    cost = input('Type the price:\n$')
    print('----------------------------')
    while cost.isnumeric() == False:
        cost = input(f'''Error - only number values allowed
Type the price:\n$''')
        print('---------------------------')

    cost = int(cost)
    clear_terminal()

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


def update_vehicle(url, headers, id):
    model0, trim0, color0, cost0 = get_vehicle_for_update(url, headers, id)

    model = input(f'Current model - {model0}, enter the new model:\n')
    print('---------------------------')
    trim = input(f'Current trim - {trim0}, enter the new trim:\n')
    print('---------------------------')
    color = input(f'Current color - {color0}, enter the new color:\n')
    print('---------------------------')
    cost = input(f'Current cost - ${cost0}, enter the new cost:\n$')
    print('---------------------------')
    while cost.isnumeric() == False:
        cost = input(f'''Error - only number values allowed
Current cost - ${cost0}, enter the new cost:\n$''')
        print('---------------------------')

    cost = int(cost)
    clear_terminal()

    vehicle_info = {
        'year': year,
        'make': make,
        'model': model,
        'trim': trim,
        'color': color,
        'cost': cost
    }

    response = requests.put(url = url + '/' + id, headers=headers, json=vehicle_info)

    if response.status_code == 200:
        update_vehicle = response.json()
        print(f"Updated vehicle: {update_vehicle}")
        print('------------------------------------')
    else:
        logging.error(f"API call to {url} failed: {response.status_code} Error")
        error_codes(response.status_code)
        return None
    
    
def delete_vehicle(url, headers, id):
    response = requests.delete(url = url + '/' + id, headers=headers)

    if response.status_code == 200:
        deleted_vehicle = response.json()
        print(f"Deleted vehicle: {deleted_vehicle}")
        print('------------------------------------')
    else:
        logging.error(f"API call to {url} failed: {response.status_code} Error")
        error_codes(response.status_code)
        return None
    

def user_interface(url, headers, page, per_page):
    main_menu = True

    while main_menu:
        main_menu = input('''Welcome to the Tesla dealership!
Please select a following option:
1)see vehicles 2)create vehicle 3)quit
---------------------------------------
''')
        clear_terminal()
        if main_menu in ['1', 'one', 'see', 's', 'see vehicles']:
            get_vehicles(url, headers, page, per_page)
        elif main_menu in ['2', 'two', 'create', 'c', 'create vehicle']:
            post_vehicle(url, headers)
            print('--------------------------')
        elif main_menu in ['3', 'three', 'quit', 'q']:
            main_menu = False
            print('Bye Bye!')
        else:
            print('Error - try another option')
            print('---------------------------')
        

def main():
    url = "https://vehicle-z65p.onrender.com/api/vehiclesapi"
    api_token = os.getenv('vehicleapi_key')

    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'x-access-token': "Bearer " + api_token
        }

    page = 0
    per_page = 10

    user_interface(url, headers, page, per_page)

main()