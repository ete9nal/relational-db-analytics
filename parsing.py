import requests
from bs4 import BeautifulSoup
import json

url = 'http://quotes.toscrape.com/'

# списки для зберігання цитат і авторів
quotes_data = []
authors_data = []

# множина, щоб не потрапляли пропрацьовані автори
added_authors = set()
current_page = '/'


while current_page:
    # виконуємо запит до поточної сторінки
    response = requests.get(url + current_page)
    soup = BeautifulSoup(response.text, 'lxml')

    # знаходимо усі контейнери з цитатами
    quotes = soup.find_all('div', class_='quote')

    # розбираємо окремо кожну цитату та додаємо до списку цитат
    for q in quotes:
        quote = q.find('span', class_='text').text
        author = q.find('small', class_='author').text
        tags = [tag.text for tag in q.find_all('a', class_='tag')]
        quotes_data.append({
            'tags': tags,
            'author': author,
            'quote': quote
        })

        # розбираємо окремо кожного автора та додаємо до списку авторів
        if author not in added_authors:
            author_link = q.find('a', string="(about)")
            if author_link:
                author_url = author_link['href']
                author_response = requests.get(url + author_url)
                author_soup = BeautifulSoup(author_response.text, 'lxml')
                authors_data.append({
                    'fullname': author,
                    'born-date': author_soup.find('span', class_='author-born-date').text,
                    'born_location': author_soup.find('span', class_='author-born-location').text,
                    'description': author_soup.find('div', class_='author-description').text,
                })
                added_authors.add(author)

    # шукаємо кнопку 'next'
    next_button = soup.find('li', class_='next')

    # перевірка чи є кнопка 'next', щоб зупинитися на останній сторінці
    if next_button:
        current_page = next_button.find('a')['href']
    else:
        current_page = None

# записуємо наші списки словників у json
with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(quotes_data, f, ensure_ascii=False, indent=2)

with open('authors.json', 'w', encoding='utf-8') as f:
    json.dump(authors_data, f, ensure_ascii=False, indent=2)
