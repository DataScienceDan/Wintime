import requests

from bs4 import BeautifulSoup, SoupStrainer
f = open("c:\wintime\gameIds.txt","a")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like

for y in range(2005, 2020):
    page = requests.get("https://www.footballdb.com/scores/index.html?lg=NFL&yr=" + str(y), headers=headers)


# Preseason 5 weeks
    for g in range(1,6):
        page = requests.get("https://www.footballdb.com/scores/index.html?lg=NFL&yr=" + str(y) + "&type=pre&wk=" + str(g), headers = headers)

        for link in BeautifulSoup(page.content, parse_only = SoupStrainer('a'),features="html.parser"):
            if link.has_attr('href'):
                if 'boxscore' in link['href']:
                    print(link['href'][-10:] + "," + str(y) + ",PRE," + str(g))
                    f.write(link['href'][-10:] + "," + str(y) + ",PRE," + str(g))
                    f.write("\n")


# Regular Season
    for g in range(1,18):
        page = requests.get("https://www.footballdb.com/scores/index.html?lg=NFL&yr=" + str(y) + "&type=reg&wk=" + str(g), headers = headers)

        for link in BeautifulSoup(page.content, parse_only = SoupStrainer('a'),features="html.parser"):
            if link.has_attr('href'):
                if 'boxscore' in link['href']:
                    print(link['href'][-10:] + "," + str(y) + ",REG," + str(g))
                    f.write(link['href'][-10:] + "," + str(y) + ",REG," + str(g))
                    f.write("\n")

# Post Season
    for g in range(1,5):
        page = requests.get("https://www.footballdb.com/scores/index.html?lg=NFL&yr=" + str(y) + "&type=post&wk=" + str(g), headers = headers)

        for link in BeautifulSoup(page.content, parse_only = SoupStrainer('a'),features="html.parser"):
            if link.has_attr('href'):
                if 'boxscore' in link['href']:
                    print(link['href'][-10:] + "," + str(y) + ",POST, " + str(g))
                    f.write(link['href'][-10:]  + "," + str(y) + ",POST, " + str(g))
                    f.write("\n")

 #    for link in BeautifulSoup(page.content, parse_only = SoupStrainer('a'),features="html.parser"):
  #       if link.has_attr('href'):
  #           if 'boxscore' in link['href']:
#                 print(link['href'][-10:])
#                 f.write(link['href'][-10:] + "," + y + "," + "")
#                 f.write("\n")


f.close()




