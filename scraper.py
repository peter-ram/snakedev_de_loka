from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import wget
import sys

# month_string = "202202"
month_string = sys.argv[1]

def crawl_all():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
    
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",
    			chrome_options=options)
    
    try:
        driver.get("https://s3.amazonaws.com/tripdata/index.html")
        timeout_in_seconds = 5
        element_present = ec.presence_of_element_located((By.CLASS_NAME, "hide-while-loading table table-striped"))
        WebDriverWait(driver, timeout_in_seconds).until(element_present)
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        print(soup)
    except TimeoutException:
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
    
    finally:
        driver.quit()
        
        
    links = [link['href'] for link  in soup.find_all("a") if ".zip" in link['href'] ]
    
    
    
    for link in links:
        wget.download(link)
    


def crawl_file(month_string):
    link = "https://s3.amazonaws.com/tripdata/JC-" + month_string +  "-citibike-tripdata.csv.zip"
    wget.download(link, "datalake//")


crawl_file(month_string)