import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9'
}

def get_page_content(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None

def extract_article(content):
    soup = BeautifulSoup(content, 'html.parser')
    articles = []

    for article_block in soup.find_all('div', class_="search-item"):
        title_div = article_block.find('div', class_="search-txt")

        title = "no title found"
        link = "no link found"
        date = "no date found"
        description = "no description found"

        if title_div:
            # Title & Link
            title_tag = title_div.find('a')
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = title_tag.get('href', "no link found")

            # Meta info (e.g., date)
            meta_ul = title_div.find('ul', class_='story-meta')
            if meta_ul:
                date_li = meta_ul.find('li')
                if date_li:
                    date = date_li.get_text(strip=True)

            # Description (if exists)
            desc_p = title_div.find('p')
            if desc_p:
                description = desc_p.get_text(strip=True)

        articles.append({
            'title': title,
            'link': link,
            'date': date,
            'description': description
        })

    return articles

def scrape_multiple_pages(base_url, num_pages):
    all_articles = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}//{page}"
        print(f"scraping{url}...")
        page_content = get_page_content(url)
        if page_content:
            articles = extract_article(page_content)
            all_articles.extend(articles)
        else:
            print(f"failed to load {url}")

    return all_articles
base_url = ""
num_pages = 5
all_articles = scrape_multiple_pages(base_url, num_pages)

df = pd.DataFrame(all_articles)

df.to_csv('tech_news_articles.csv', index=False)

print("articles have been saved to tech_news_articles.csv")