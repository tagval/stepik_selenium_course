from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/wait1.html"

browser = webdriver.Chrome('C:/chromedriver/chromedriver')
# Задаем неявное ожидание при инициализации браузера, чтобы применять его ко всем тестам
# Ожидание называется неявным (implicit wait), так как его не надо явно указывать каждый раз,
# когда мы выполняем плиск элементов, оно автоматически будет применяться при вызове каждой последующей команды
# при этом проверка наличия элемента проверяется каждые 500мс
# Тут мы говорим webdriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get(link)

#time.sleep(1)
button = browser.find_element_by_id("verify")
button.click()
#time.sleep(1)
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text