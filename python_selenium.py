import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/radio-button' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1920, 1080) # окно разрешения

# Кликаем по Impressive
radio_button = driver_chrome.find_element(By.XPATH, '(//label[@class="custom-control-label"])[2]')
radio_button.click()

# делаем проверку через сравнение
radio_selected = driver_chrome.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p/span')
radio_text = radio_selected.text
assert radio_text == 'Impressive'
print("radio button выбран")

time.sleep(2)

driver_chrome.close()