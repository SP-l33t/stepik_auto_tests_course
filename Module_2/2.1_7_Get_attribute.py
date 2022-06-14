from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = int(x.get_attribute("valuex"))
    y = calc(x)
    print(y)
    in_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    in_field.send_keys(y)
    chck_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    chck_box.click()
    radio_box = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_box.click()
    # mail = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    # mail.send_keys(data["email"])
    time.sleep(1)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
