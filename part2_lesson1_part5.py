from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome('C:/chromedriver/chromedriver')
browser.get(link)

#Считывание значения. Атрибут text возвращает текст, который находится между открывающим
# и закрывающим тегами элемента. Например, text для данного элемента
# <div class="message">У вас новое сообщение.</div>
# вернёт строку: "У вас новое сообщение".
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

y_element = browser.find_element(By.ID, "answer")
y_element.send_keys(y)

checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
checkbox.click()

radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
radiobutton.click()

submit = browser.find_element(By.TAG_NAME,"button")
submit.click()

time.sleep(5)

browser.quit()