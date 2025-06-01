import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/' # Даём ссылку на тестируемый сайт

driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1700, 1800) # окно максимального разрешения

user_name = driver_chrome.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input')
user_name.send_keys("error_user") # вводим логин
print('input login')

password = driver_chrome.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce") # вводим не корректный пароль
print('input password')

user_name.send_keys(Keys.CONTROL + 'a' + Keys.DELETE) # очищаем поле логин
password.send_keys(Keys.CONTROL + 'a' + Keys.DELETE) # очищаем поле пароль

user_name.send_keys("standard_user") # повторно вводим логин
password.send_keys("secret_sauce") # повторно воодим пароль

button_login = driver_chrome.find_element(By.ID, 'login-button')
button_login.click() # кликаем на авторизацию
print("Click Login")

# # кладем товары в корзину
# button_add_backpack = driver_chrome.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
# button_add_Bike = driver_chrome.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
# button_add_TShirt = driver_chrome.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
# button_add_Jacket = driver_chrome.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
# button_add_Onesie = driver_chrome.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
# button_add_TShirt_Red = driver_chrome.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
# # переходим в корзину
# button_cart_link = driver_chrome.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
#
# actions = ActionChains(driver_chrome)
# element = driver_chrome.find_element(By.ID, "item_3_title_link")
# actions.move_to_element(element).perform() # скролим страницу к последнему товару в списке

# now_date = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
# name_screenshot = 'screenshot' + now_date + '.png'
# driver_chrome.save_screenshot('D:\\GitHub\\Project\\PythonProject\\screen\\' + name_screenshot) # делаем скриншот страницы
# # driver_chrome.refresh() # обновляем страницу