from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome('C:/chromedriver/chromedriver')

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100"))

button1 = browser.find_element(By.ID, "book")
button1.click()

browser.execute_script("window.scrollBy(0, 100);")

x_element = browser.find_element(By.ID,"input_value")
x = x_element.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input1 = browser.find_element(By.TAG_NAME, "input")
input1 = input1.send_keys(y)

button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button2 = button2.click()

browser.quit()