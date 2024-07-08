from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import date
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def crawling():
    for username in users:
        url = f'https://github.com/{username}'  
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'ContributionCalendar-day')))
        # 페이지가 로드될 때까지 대기 (필요시 명시적인 대기 조건을 추가할 수 있음)

        # 페이지 소스 가져오기
        page_source = driver.page_source

        # HTML 파싱
        soup = BeautifulSoup(page_source, 'html.parser')

        # 모든 날짜 요소 찾기
        date_elements = soup.find_all('td', {'data-date': today_str})
        element = soup.find('td', {'data-date': today_str})
        jandi_level = element.get('data-level') if element else 'No data'
        print(f"Username: {username}, Jandi Level: {jandi_level}")
    # 브라우저 닫기
    driver.quit()


now = time.time()

# 오늘 날짜 가져오기
today = date.today()
today_str = today.strftime("%Y-%m-%d")

# 브라우저 옵션 설정 (브라우저 창을 숨기려면 아래 두 줄 추가)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

users = []
user = 'boham97'
users.append(user)

driver.implicitly_wait(3)

print("jandi-level")
print("today: ", today_str)
print("-----------------------------")


driver.get(f'https://github.com/{user}?tab=followers')
soup = BeautifulSoup(driver.page_source, 'html.parser')
date_elements = soup.find_all('span', class_='Link--secondary')
jandi = [0] * (len(date_elements) + 1)
for element in date_elements:
    users.append(element.text)


crawling()





