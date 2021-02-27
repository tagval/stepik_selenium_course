from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link="http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome('C:/chromedriver/chromedriver')
browser.get(link)

input1=browser.find_element(By.NAME, "first_name")
input1.send_keys("Ivan")
input2=browser.find_element(By.NAME,"last_name")
input2.send_keys("Ivanov")
input3=browser.find_element(By.NAME, "firstname")
input3.send_keys("Moscow")
input4=browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button=browser.find_element(By.ID,"submit_button")
button.click()

time.sleep(25)

browser.quit()
