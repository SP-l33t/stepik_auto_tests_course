from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Vladimir")
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Sementin")
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("v.sementin@ya.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
