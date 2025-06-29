import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1920, 1080) # окно разрешения
action = ActionChains(driver_chrome)

# двигаем ползунок Round
slider = driver_chrome.find_element(By.XPATH, '//input[@class = "slider-color"]')
action.click_and_hold(slider).move_by_offset(-500, 0).release().perform()
check_value = driver_chrome.find_element(By.XPATH, "//span[@id = 'f']")
check_text = check_value.text
print(f"Значение value: {check_text}")
assert check_text == "11"
print('Проверка пройдена')

time.sleep(5)

driver_chrome.close()