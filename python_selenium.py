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
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1920, 1080) # задаем параметры окна разрешения

# переключаемся на iframe
iframe = driver_chrome.find_element(By.XPATH, "//iframe[@id= 'iFrame1']")
driver_chrome.switch_to.frame(iframe)

# редактируем поле с текстом
input_frame = driver_chrome.find_element(By.XPATH, "//*[@id='__next']/div/div[2]")
input_frame.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
input_frame.send_keys("Bobr")
value_frame = input_frame.text
print(value_frame)
time.sleep(1)

# выделяем текст и включаем жирный курсив
input_frame.send_keys(Keys.CONTROL + 'a')
click_panel_bold = driver_chrome.find_element(By.XPATH, "//button[@title = 'Bold']")
click_panel_bold.click()
print("Клик по кнопке Bold")
time.sleep(1)

# сравниваем текст до и после жирного курсива
new_input_frame = driver_chrome.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/b")
new_value_frame = new_input_frame.text
print(new_value_frame)
assert new_value_frame == value_frame
print("Редактирование успешно")

driver_chrome.close()