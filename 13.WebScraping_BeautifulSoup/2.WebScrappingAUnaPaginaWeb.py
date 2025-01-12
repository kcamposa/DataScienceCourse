# -- Cómo obtener el código HTML de una página web

from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# -- Cómo hacer web scraping en una página
box = soup.find('article', class_='main-article')
title = box.find('h1').get_text()

transcript = soup.find('div', class_='full-script').get_text(strip=True, separator=' ') # para que salga todo corrido 

# -- Exportar data a un archivo TXT
with open(f"{title}.txt", "w", encoding='utf-8') as file: 
    file.write(transcript)

# -- Web Scraping en multiples links ubicados en la misma pagina
