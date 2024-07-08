import requests
import time
from bs4 import BeautifulSoup as bs
from datetime import datetime

start = time.time()

def get_followers(user):
    user_url = f"https://github.com/{user}?tab=followers"

    result = requests.get(user_url)
    html = bs(result.text, 'html.parser')
    elements = html.find_all('span', {'class' : 'Link--secondary'})

    users = [element.get_text() for element in elements]
    
    return users

def get_jandi(user, date):

    headers = {
        'accept': 'text/html',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'dnt': '1',
        'if-none-match': 'W/"f2323b3d3dd0a034d0eefb224d4d2124"',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "AVG Secure Browser";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'action': 'show',
        'controller': 'profiles',
        'tab': 'contributions',
        'user_id': 'boham97',
    }

    response = requests.get(f"https://github.com/{user}", params=params, headers=headers)

    html = bs(response.text, 'html.parser')

    elements = html.find('td', class_='ContributionCalendar-day', attrs={'data-date': str(date)})

    return elements['data-level']

user = 'boham97'

today = datetime.today().strftime('%Y-%m-%d')

print('jandi-level')
print(today)

users = get_followers(user)
users.append(user)

for x in users :
    jandi = get_jandi(x, today)
    print(f"username : {x}, jandi-level : {jandi}")

end = time.time()

print(f"{end - start} seconds")
    