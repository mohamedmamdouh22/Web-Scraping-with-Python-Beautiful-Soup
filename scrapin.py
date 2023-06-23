import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
date=input('Enter date(mm/dd/yyyy):')
try:
    page=requests.get(f'https://www.yallakora.com/match-center/?date={date}')
except:
    print('wrong format')
match_results=[]
def main(page):
    src=page.content
    soup=BeautifulSoup(src,'lxml')
    championships=soup.find_all('div',{"class":'matchCard'})
    for i in range(len(championships)):
        title= championships[i].find('h2').text.strip()
        try:
            channel=championships[i].find('div',{'class':'channel'}).text.strip()
        except:
            channel='غير مذاعه'
        state=championships[i].find('div',{'class':'matchStatus'}).find('span').text.strip()
        teamA=championships[i].find('div',{'class':'teamA'}).find('p').text.strip()
        teamB=championships[i].find('div',{'class':'teamB'}).find('p').text.strip()
        results=championships[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
        score=results[0].text.strip()+'-'+results[1].text.strip()
        time=championships[i].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()
        match_results.append(
            {
                'البطوله':title,
                'القناه':channel,
                'الحاله':state,
                'الفريق الاول':teamA,
                'النتيجه':score,
                'الفريق الثاني':teamB,
                'الوقت':time
            }
        )
    df=pd.DataFrame(match_results)
    df.to_csv('results.csv',index=None)
    print('done')

main(page)