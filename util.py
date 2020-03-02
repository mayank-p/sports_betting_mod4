import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 


def get_first_half_stats():
    driver.get('https://stats.nba.com/teams/boxscores-traditional/?Season=2019-20&SeasonType=Regular%20Season')
    #clicks advanced filters
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[4]/a').click()
    time.sleep(1)
    #clicks first half
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[5]/div/label/select/option[2]').click()
    time.sleep(1)
    #clicks run it
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[2]/div[2]/stats-run-it/a').click()
    time.sleep(1)
    #clicks all
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]').click()
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source)
    tables = soup.findAll('table')
    table = tables[0].prettify()
    first_half = pd.read_html(table)[0]

    first_half.to_csv('first_half.csv')
    
    