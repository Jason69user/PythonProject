import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/checkbox' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1920, 1080) # окно разрешения

# находим input на чекбокс "home"
checkbox_input = driver_chrome.find_element(By.CSS_SELECTOR, 'input[id="tree-node-home"]')

# Кликаем по чекбоксу
checkbox_span = driver_chrome.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
checkbox_span.click()
checkbox_input.is_selected()
print("checkbox select")

time.sleep(2)

driver_chrome.close()