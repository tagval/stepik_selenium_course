from selenium import webdriver
browser = webdriver.Chrome('C:/chromedriver/chromedriver')
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

# Сообщение об ощибке появляется потому что WebDriver быстро нашел кнопку и кликнул по ней,
# хотя кнопка была еще неактивной. На странице мы специально задали программно паузу в 1
# секунду после загрузки сайта перед активированием кнопки, но неактивная кнопка в момент
# загрузки — обычное дело для реального сайта.
# Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и дождаться,
# когда кнопка станет кликабельной. Для реализации подобных ожиданий в Selenium WebDriver
# существует понятие явных ожиданий (Explicit Waits), которые позволяют задать специальное
# ожидание для конкретного элемента.