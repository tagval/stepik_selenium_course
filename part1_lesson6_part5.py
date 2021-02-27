from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome('C:/chromedriver/chromedriver')
    browser.get("http://suninjuly.github.io/find_link_text")

    a = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    link = browser.find_element_by_link_text(a)
    link.click()

    input1=browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2=browser.find_element(By.NAME,"last_name")
    input2.send_keys("Ivanov")
    input3=browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Moscow")
    input4=browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button=browser.find_element(By.TAG_NAME,"button")
    button.click()

    time.sleep(7)
finally:
    browser.quit()
