import  urllib.request as q
from bs4 import BeautifulSoup as bsp

website = 'https://www.uottawa.ca/en'

def get_from_list(links):
    newLinks = []
    for i in links:
        c = str(i)
        if 'href="' in c:
            the_splitted = c.split('href="')[1].split('"')[0]

            if 'http://' in the_splitted and the_splitted  not in newLinks:
                #print(the_splitted)
                newLinks.append(the_splitted)
                #print(c.split('href="')[1].split('"')[0])
                #print("THIS IS ONE:  ", c)

    return newLinks

def read_each(newLinks):
    containers = []
    for i in newLinks:
        try:
            content = q.urlopen(i).read()
            if'co-op' in str(content):
                print(i)
                containers.append(i)
        except:
            print('an error occured')

    return containers


def getURLs(url):
    content = q.urlopen(website).read()
    #print(str(content))

    soup = bsp(content, "html.parser")

    links = soup.find_all('a')
    print(links)

    newLinks = get_from_list(links)

    containers = read_each(newLinks)

    print(containers)

getURLs(website)