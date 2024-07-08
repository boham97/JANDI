from bs4 import BeautifulSoup
from datetime import date
import requests
import multiprocessing

def crawling(users):
    today = date.today()
    results = {}
    today_str = today.strftime("%Y-%m-%d")
    for username in users:
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

        response = requests.get(f'https://github.com/{username}', params=params, headers=headers)


        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 모든 날짜 요소 찾기
        element = soup.find('td', {'data-date': today_str})
        jandi_level = element.get('data-level') if element else 'No data'
        results[username] = jandi_level
    return results

def find(user):
    user_url = f"https://github.com/{user}?tab=followers"

    result = requests.get(user_url)
    html = BeautifulSoup(result.text, 'html.parser')
    elements = html.find_all('span', {'class' : 'Link--secondary'})

    users = [element.get_text() for element in elements]
    
    return users



def multi():
    mid_point = len(users) // 4
    users_part1 = users[:mid_point]
    users_part2 = users[mid_point:mid_point * 2]
    users_part3 = users[mid_point * 2:mid_point * 3]
    users_part4 = users[mid_point * 3:]
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(crawling, [users_part1, users_part2, users_part3, users_part4])

    all_results = {user: jandi for result in results for user, jandi in result.items()}
    
    for user, jandi in all_results.items():
        print(f"Username: {user}, Jandi Level: {jandi}")

if __name__ == "__main__":
    user = 'boham97'
    users = find(user)
    users.append(user)
    multi()