import time

from selenium import webdriver
from datetime import datetime, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/date-picker' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1920, 1080) # окно разрешения

# удаляем поле с датой
data_input = driver_chrome.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')
data_input.send_keys(Keys.CONTROL + 'a')
data_input.send_keys(Keys.DELETE)

time.sleep(1)

# вставляем дату на 10 дней вперед от сегодня
days_later = datetime.now() + timedelta(days=10)
current_data = days_later.strftime('%m.%d.%Y')
print(current_data)
data_input.send_keys(current_data)

time.sleep(2)

driver_chrome.close()