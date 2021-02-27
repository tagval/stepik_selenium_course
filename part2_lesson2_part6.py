from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome('C:/chromedriver/chromedriver')
browser.get(link)

x_element = browser.find_element(By.ID,"input_value")
x = x_element.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
checkbox.click()

radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
radiobutton.click()

submit = browser.find_element(By.TAG_NAME,"button")
submit.click()

time.sleep(5)

browser.quit()