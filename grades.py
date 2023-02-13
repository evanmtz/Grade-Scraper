import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from info import *

url = "https://hac.aldineisd.org/HomeAccess/Home/WeekView"

ser = Service("C:\Program Files (x86)\chromedriver.exe")

driver = webdriver.Chrome(service=ser)

driver.get(url)

time.sleep(20)

try:
    un = driver.find_element(By.ID, "LogOnDetails_UserName")
    un.send_keys(user)
    time.sleep(5)
except:
    print("Couldn't locate Username element.")
    driver.quit()

try:
    pwd = driver.find_element(By.ID, "LogOnDetails_Password")
    pwd.send_keys(passwd)
    time.sleep(5)

except:
    print("Couldn't locate Password element.")
    driver.quit()

sign_in = driver.find_element(By.NAME, "login")
sign_in.click()

time.sleep(10)

gradeList = []

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
r = requests.get(url, headers)
soup = BeautifulSoup(r.content, 'html.parser')

anchors = soup.find_all('a', id_ = 'courseName')

for course in anchors:
    className = course.find('a').text.strip()
    grade = course.find('a', id_ = 'average')

    classGrades = {
        "className": className,
        "grade": grade
    }

    gradeList.append(classGrades)

data = pd.DataFrame(gradeList)

print(data.head())
