import requests
from bs4 import BeautifulSoup

file = open('books.csv', 'w', encoding='UTF-8')
file.write('სათაური,ავტორი,ფასი')
count = 1
while count >= 5:
    url = 'http://lit.ge/index.php?page=books&send[shop.catalog][page]=' + str(count)
    r = requests.get(url)
    # print(r.headers)
    # print(type(r.text))
    content = r.text
    soup = BeautifulSoup(content, "html.parser")
    section = soup.find("section", {'class': 'list-holder'})
    # print(section)
    all_books = section.find_all('article', {'class': 'item-holder'})

    for each in all_books:
        t_bar = each.find("div", {'class': 'title-bar'})

        for i in all_books:
            t_bar = i.find('div', {'class': 'title-bar'})
            title = t_bar.a.text
            author = t_bar.b.a.text
            print(author)
    count += 1

file.close()
