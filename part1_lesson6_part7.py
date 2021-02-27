from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link="http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome('C:/chromedriver/chromedriver')
browser.get(link)
elements = browser.find_elements(By.TAG_NAME,"input" )
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(5)
browser.quit()