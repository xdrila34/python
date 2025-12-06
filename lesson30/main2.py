from bs4 import BeautifulSoup

html_content = '''
<html>
    <head>
        <title>welcome top beautifulsoup</title>
    </head>
    <body>
        <h1>welcome top beautifulsoup</h1>
        <p class="intro">beautifulsoup makes web easier</p>
        <div id="content">
            <p>here are some links</p>
            <a href="http://example.com/page1">link1</a>
            <a href="http://example.com/page2">link2</a>
            <a href="http://example.com/page3">link3</a>
        </div>
    </body>
</html>
'''

soup = BeautifulSoup(html_content, 'html.parser')

print("title of the page:", soup.title.text)

intro_text = soup.find('p', class_="intro").text
print("intro text:", intro_text)

div_content = soup.find('div', id='content')
links = div_content.find_all('a')
for link in links:
    print("link:", link['href'])

first_link = soup.find('a')
print("first link:", first_link.text)
print("next sibling of the first link:", first_link.next_sibling)

paragraphs = soup.select('div#content p')
for paragraph in paragraphs:
    print('Paragraph inside content: ', paragraph.text)

new_tag = soup.new_tag('b')
new_tag.string = "Important"
soup.h1.append(new_tag)

print("modified h1 tag:", soup.h1)