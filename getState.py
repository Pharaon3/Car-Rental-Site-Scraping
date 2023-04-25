from config import *
from setting import *
import csv
import threading

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pandas as pd
import time
import re
import csv
from datetime import datetime
from datetime import date

def execute_code():
    threading.Timer(120.0, execute_code).start()

    profile_id = fnGetUUID()
    port = get_debug_port(profile_id)
    driver = get_webdriver(port)
    driver.get(TARGET_URL)
    
    time.sleep(2)

    stateName = '//*[@id="avisHome"]/div[2]/div[2]/div/section/div[2]/ul'
    stateElement = driver.find_element(By.XPATH, stateName)
    children = stateElement.find_elements(By.XPATH, './li')
    with open('state.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(["stateName", "stateHref"])
        for c in range(0, len(children)):
            stateName = children[c].find_element(By.XPATH, './a').get_attribute("innerHTML")
            stateHref = children[c].find_element(By.XPATH, './a').get_attribute("href")
            print(stateName)
            print(stateHref)
            writer.writerow([stateName, stateHref])

    driver.close()
    
execute_code()