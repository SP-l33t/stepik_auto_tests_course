from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
