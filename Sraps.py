import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

startUrl = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome("/Users/naseemahusain/Desktop/Whitehatjr/C127/chromedriver")

browser.get(startUrl)
time.sleep(10)


def scrap():
    planetData = []
    headers = ['NAME', 'LIGHT-YEARS FROM EARTH',
               'PLANET MASS', 'STELLAR MAGNITUDE', 'DISCOVERY DATE']
    for i in range(0, 441):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all('ul',attrs=['class','exoplanet']):
            li_tag=ul_tag.find_all('li')
            allData=[]
            for index,li_tag in enumerate(li_tag):
                if index==0:
                    allData.append(li_tag.find_all('a')[0].contents[0])

                    try:
                        allData.append(li_tag.contents[0])

                    except:
                        addData.append('')
            planetData.append(allData)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a')
    with open('save.csv','w') as f:
        csvWriter=csv.writer(f)
        csvWriter=writerows(planetData)
scrap()