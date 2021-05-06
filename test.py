from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('div.html', 'r') as f:
        # text = f.read()
        soup = BeautifulSoup(f, "html.parser")
    # print(f'soup = {soup}')
    # tds = soup.findAll("div", {"class": "t1"})
    # tab = tds[0]
    tds = soup.findAll("td", {"class": "dom_zone"})
    trs = soup.findAll("tr")
    print(f'trs = {len(trs)}')
    print(f'tDs = {len(tds)}')
    # tds = soup.findAll("td"), {"class": "td1"})
    # for i, tr in enumerate(trs):
    #     print('*******************************************************\n')
    #     print(str(trs[i]) + '\n')
    #     print('*******************************************************\n')
    print(str(trs[50]))


