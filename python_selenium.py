import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://the-internet.herokuapp.com/javascript_alerts' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1261, 2399) # задаем параметры окна разрешения

# закрываем окно Alert
click_alert = driver_chrome.find_element(By.XPATH, "//button[@onclick= 'jsAlert()']")
click_alert.click()
print("Кликаем на Click for JS Alert")
time.sleep(1)
driver_chrome.switch_to.alert.accept()
print("Кликаем Закрыть")
time.sleep(1)

# закрываем окно Alert кнопкой "нет"
click_confirm = driver_chrome.find_element(By.XPATH, "//button[@onclick= 'jsConfirm()']")
click_confirm.click()
print("Кликаем на Click for JS Confirm")
time.sleep(1)
driver_chrome.switch_to.alert.dismiss()
print("Кликаем Нет")
time.sleep(1)

# вводим слово в поле и закрываем окно Alert кнопкой "продолжить"
click_prompt = driver_chrome.find_element(By.XPATH, "//button[@onclick= 'jsPrompt()']")
click_prompt.click()
print("Кликаем на Click for JS Prompt")
time.sleep(1)
driver_chrome.switch_to.alert.send_keys("Ave Maria")
print("Вводим в поле: 'Ave Maria'")
time.sleep(1)
driver_chrome.switch_to.alert.accept()
print("Кликаем Продолжить")
time.sleep(1)

driver_chrome.close()