from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome('C:/chromedriver/chromedriver')
browser.get(link)

a_element = browser.find_element(By.ID,"num1")
a = a_element.text

b_element = browser.find_element(By.ID,"num2")
b = b_element.text

sum = int(a) + int(b)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum))

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(5)

browser.quit()