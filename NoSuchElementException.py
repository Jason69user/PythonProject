import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/dynamic-properties' # Даём ссылку на тестируемый сайт
driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1261, 2399) # задаем параметры окна разрешения

# добавляем исключение при задержке появления кнопки(NoSuchElementException)
try:
    button_visible = driver_chrome.find_element(By.XPATH, "//button[@id = 'visibleAfter']")
    button_visible.click()
    print('NoSuchElementException не отработал')
except NoSuchElementException:
    print('Отработал NoSuchElementException')
    time.sleep(2)
    driver_chrome.refresh()
    time.sleep(5)
    button_visible = driver_chrome.find_element(By.XPATH, "//button[@id = 'visibleAfter']")
    button_visible.click()
    print('Кликаем на button visible')

driver_chrome.close()