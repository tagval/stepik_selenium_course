from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"

    browser = webdriver.Chrome('C:/chromedriver/chromedriver')
    browser.get(link)

    # Заполнение обязательных полей для регистрации
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block>div>input.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block>div>input.second")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block>div>input.third")
    input3.send_keys("ivanov@mail.com")

    # Нажатие на кнопку Submit
    button = browser.find_element_by_css_selector("button.btn").click()
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
