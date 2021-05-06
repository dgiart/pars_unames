import sys, os
import requests
from bs4 import BeautifulSoup


def get_tag(url, tagname, classname):
    response = requests.get(url)
    full_text = response.text
    soup = BeautifulSoup(full_text)
    div = (soup.find(tagname, class_=classname))
    return div


if __name__ == '__main__':
    print(sys.version)
    print(os.getcwd())
    url = 'https://www.ukrnames.com/domains/prices.jsp'
    tag = 'div'
    class_name = "right_column"
    div = get_tag(url, tag, class_name)# .text
    print(f'div len = {len(div)}')
    print(f'div type = {type(div)}')
    # print(div[5])
    with open('div.html', 'w') as file:
        file.write(str(div))
    tds = BeautifulSoup(div).findAll("td", {"class": "dom_zone"})
    print(f'len = {len(tds)}')
    print('DONE')
