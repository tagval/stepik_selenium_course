from selenium import webdriver
from selenium.webdriver.common.by import By
import math



link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome('C:/chromedriver/chromedriver')
browser.get(link)

box = browser.find_element(By.TAG_NAME, "img")
x = box.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input1 = browser.find_element(By.TAG_NAME,"input")
input1.send_keys(y)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radiobutton = browser.find_element(By.ID, "robotsRule")
radiobutton.click()

button = browser.find_element(By.TAG_NAME,"button")
button.click()

browser.quit()