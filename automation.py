from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

path = "/Users/boone/Documents/Random/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://www.nvidia.com/en-us/geforce/")

search = driver.find_element_by_class_name("nav-search-icon").click()
input = driver.find_element_by_id("search-terms")
#input.clear()
input.send_keys(3080)
input.send_keys(Keys.RETURN)

try:
    content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 
              "search-results-container")))
    titles = content.find_elements_by_class_name("item-title")

    for title in titles:
        if title.text == "GeForce RTX 3080 Graphics Card | NVIDIA":
            found = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 
                    "item-footer")))
            found.click()
except:
    driver.quit()