import requests
import textrazor


# TODO Hide

class NewsAgg():
    def __init__(self, text = None):
        self.text = text

    def get_news(self, category, q):
        url = f'https://newsapi.org/v2/top-headlines/sources?category={category}&q={q}&country=us'
        headers = {
            'X-Api-Key': news_api_key
        }

        response = requests.get(url, headers = headers)

        if response.ok:
            if 'json' in response.headers['Content-Type']:
                for items in response.json()['sources']:
                    # print(items['description'])
                    # print('---------------------')
                    self.text = response.json()['sources'][0]['description']
            elif 'xml' in response.headers['Content-Type']:
                print(response.text)
            else:
                print(response.content)
        else:
            print(response.status_code, response.reason)

    def get_anal(self):
        client = textrazor.TextRazor(extractors=["entities", "topics"])
        response = client.analyze(self.text)

        if response.ok:
            json = response.json
            for topics in json['response']['coarseTopics']:
                print('---------------------')
                print(topics['label'], topics['score'])
        else:
            print('Something went wrong')

    def user_input(self):
        news_dict = {
            '1': 'business',
            '2': 'entertainment',
            '3': 'general',
            '4': 'health',
            '5': 'science',
            }
        
        news_cat = input('Select a category\n1)business 2)entertainment 3)general 4)health 5)science\n')

        while news_cat not in ['1', '2', '3', '4', '5']:
            news_cat = input('Select a category\n1)business 2)entertainment 3)general 4)health 5)science\n')
        
        sel_cat = news_dict[news_cat]

        q= input('input a keyword or phrase:\n')
        self.get_news(sel_cat, q)


        
newsagg1 = NewsAgg()
newsagg1.user_input()
newsagg1.get_anal()

