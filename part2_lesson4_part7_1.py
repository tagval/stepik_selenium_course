# Перепишем тест из part2_lesson4_part7 так чтобы в нем использовались явные ожидания вместо неявных.
# Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome('C:/chromedriver/chromedriver')

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.
button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
# В этой строке происходит следующее:
# Из модуля expected_conditions вызывается функция element_to_be_clickable(). Далее в эту функцию мы
# передаем кортеж (By.ID, "verify"). Такой тип данных, что-то вроде массива. Только массив выглядит
# так: [1, 2, 3, 4], а кортеж в круглых скобках: (1, 2, 3, 4)
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

# Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно
# задать негативное правило с помощью метода until_not:
#
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
