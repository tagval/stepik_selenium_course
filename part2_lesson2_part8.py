from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome('C:/chromedriver/chromedriver')
browser.get(link)

name = browser.find_element(By.NAME, "firstname")
name.send_keys("John")

last_name = browser.find_element(By.NAME, "lastname")
last_name.send_keys("Snow")

email = browser.find_element(By.NAME,"email")
email.send_keys("snow@mail.com")

file = browser.find_element(By.ID, "file")
file.send_keys("C:/Users/Admin/Desktop/profile.txt")

submit = browser.find_element(By.TAG_NAME,"button")
submit.click()

time.sleep(5)

browser.quit()