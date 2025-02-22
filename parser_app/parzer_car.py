import requests
from bs4 import BeautifulSoup

URL = 'https://m.mashina.kg'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

# 1.
def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response  # Теперь возвращаем объект Response

# 2.
def get_data(html):
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div', class_='list-item list-label')
    car_list = []
    for item in items:
        title = item.find('div', class_='block title').get_text(strip=True)
        price = item.find('div', class_='block price').get_text(strip=True)
        counters = item.find('div', class_='block counters').get_text(strip=True)
        like = item.find('span', class_='listing-icons heart').get_text(strip=True) if item.find('span',class_='listing-icons heart') else "Нет лайков"
        city = item.find('div', class_='block city').get_text(strip=True)
        image = item.find('div', class_='image-wrap')
        car_list.append({
            'title': title,
            'price': price,
            'counters': counters,
            'like': like,
            'city': city,
            'image': image
        })

    return car_list

# 3.
def parser_mashina():
    response = get_html(URL)
    if response.status_code == 200:
        car_list2 = []
        for page in range(1, 2):
            response = get_html('https://m.mashina.kg/search/all/?region=all', params={'page': page})
            car_list2.extend(get_data(response.text))
        return car_list2
    else:
        return Exception('Error')

# print(parse_mashina())
