import requests
import html5lib 
from lxml import html

from bs4 import BeautifulSoup, SoupStrainer
f = open("c:\wintime\gameIds.txt","r")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like

fo = open("c:\wintime\gamedata.txt","a")

for g in range(1,4006):
    gameid = f.readline()

for g in range(4006,4589):
    gameid = f.readline()

    print(gameid)
    gameid = gameid[0:10]
    print(gameid)


    page = requests.get("https://www.footballdb.com/games/boxscore.html?gid=" + str(gameid), headers = headers)
    tree = html.fromstring(page.content)

    soup = BeautifulSoup(page.content,'html.parser')
    teams = soup.find_all('span',{'class':'visible-xs-inline'})
    print (teams[0].text)
    print (teams[1].text )
    print (teams[2].text)
    print (teams[3].text)
#    soup = BeautifulSoup(page.content,'html.parser')
#    hometeam = soup.find('span',{'class':'visible-xs-inline'}).text
#    print(hometeam)


    gamedate = tree.xpath('//*[@id="leftcol"]/center/div/text()[1]')
    print (gamedate[0])

    location = tree.xpath('//*[@id="leftcol"]/center/div/text()[2]')
    print (location[0])

    attendance = tree.xpath('//*[@id="leftcol"]/center/div/text()[3]')
    print (attendance[0][13:])

    vscore = tree.xpath('//*[@id="leftcol"]/table/tbody/tr[2]/td[6]/b')
    print (*vscore)

    fo.write(gameid + '\t' + gamedate[0] + '\t' + location[0] + '\t' + attendance[0][13:] + '\t' + teams[0].text + '\t' + teams[1].text + '\t' + teams[2].text + '\t' + teams[3].text + '\n')


fo.close()
f.close()
