import requests

url = "https://restcountries.com/v3.1/all"

api_key = 'fd565215d3msh4ffdfc403716382p11574fjsn77d353a475e1'

# headers = {
#     'X-RapidAPI-Key': f'{api_key}',
#     'X-RapidAPI-Host': 'api-basketball.p.rapidapi.com'
# }

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