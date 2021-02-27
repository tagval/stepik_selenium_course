from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome('C:/chromedriver/chromedriver')
browser.get(link)

button1 = browser.find_element(By.TAG_NAME, "button")
button1 = button1.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.ID,"input_value")
x = x_element.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input1 = browser.find_element(By.TAG_NAME, "input")
input1 = input1.send_keys(y)

button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button2 = button2.click()

time.sleep (5)
browser.quit()