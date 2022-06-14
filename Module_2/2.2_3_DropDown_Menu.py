from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    sum = int(browser.find_element(By.CSS_SELECTOR, "#num1").text) + \
          int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))  # ищем элемент с текстом "Python"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
