import requests
from bs4 import BeautifulSoup

URL ="https://indianexpress.com/"

response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2')

    with open('headline.txt', 'w', encoding='utf-8') as file:
        for i, headline in enumerate(headlines, 1):
            title = headline.get_text(strip =True)
            if title:
                file.write(f"{i}. {title}\n")
    print("Headline scraped and saved successfully!")
else:
    print("Failed to fetch webpage. Status code: ", response.status_code)