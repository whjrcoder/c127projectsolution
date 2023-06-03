from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv
import requests

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("D:/Devangi Whitehatjunior/P127/chromedriver.exe")
browser.get(START_URL)

scraped_data=[]

def scrape():
    for i in range(1,100):
        soup= BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("tr",attrs={"class",""}):
            td_tags= tr_tag.find_all("td")
            temp_list=[]
            for index,td_tag in enumerate(td_tags):
                if index==0:
                    temp_list.append(td_tag.find_all("a")[1].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            scraped_data.append(temp_list)


                
        
        
           
           
scrape()

