import requests
import os

os.system('cls')

url = 'https://testing'
api_key = 'asdghalkjdfhblakfdas'

headers = {
    'application': 'json',
    'Authorization': f'Bearer {api_key}'
}

# def handles_api_error():

def get_data():
    response = requests.get(url = url, headers = headers)
    if response.status_code == 200:
        # TODO pagination
        print(response.json())
    else:
        # TODO log error
        print(response.status_code)
        print(response.json())

def post_data():
    data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    response = requests.post(url = url, headers = headers, json = data)
    if response.status_code == 200:
        print(response.json())
    else:
        # TODO log error
        print(response.status_code)
        print(response.json())

def put_data(id):
    data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    response = requests.put(url = url + '/' + id, headers = headers, json = data)
    if response.status_code == 200:
        print(response.json())
    else:
        # TODO log error
        print(response.status_code)
        print(response.json())
    

def delete_data(id):
    response = requests.delete(url = url + '/' + id, headers = headers)
    if response.status_code == 200:
        print(response.json())
    else:
        # TODO log error
        print(response.status_code)
        print(response.json())

def user_input():
    main_menu = True

    while main_menu:
        main_menu = input('''What would you like to do?
1)get data 2)post data 3)put data 4)delete data 5)quit\n''')
        os.system('cls')
        if main_menu == '1':
            get_data()
        elif main_menu == '2':
            post_data()
        elif main_menu == '3':
            put_data()
        elif main_menu == '4':
            delete_data()
        elif main_menu == '5':
            main_menu = False
            print('Bye bye')
        else:
            print('Error - please select another option')
            print('-------------------------------------')
        

def main():
    user_input()

main()