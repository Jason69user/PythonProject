import time
from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')
fake = Faker("ru_RU")

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com' # Даём ссылку на тестируемый сайт
driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1261, 2399) # задаем параметры окна разрешения

# проходим авторизацию
user_name = driver_chrome.find_element(By.ID, 'user-name')
user_name.send_keys("standard_user") # вводим логин
password = driver_chrome.find_element(By.ID, 'password')
password.send_keys("secret_sauce") # вводим пароль
button_login = driver_chrome.find_element(By.ID, 'login-button')
button_login.click() # кликаем на авторизацию

# создаем словарь с товаром
data_market = {
    "1": {"name": "Sauce Labs Backpack",
          "action": lambda: driver_chrome.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()},
    "2": {"name": "Sauce Labs Bike Light",
          "action": lambda: driver_chrome.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()},
    "3": {"name": "Sauce Labs Bolt T-Shirt",
          "action": lambda: driver_chrome.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()},
    "4": {"name": "Sauce Labs Fleece Jacket",
          "action": lambda: driver_chrome.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket').click()},
    "5": {"name": "Sauce Labs Onesie",
          "action": lambda: driver_chrome.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()},
    "6": {"name": "Test.allTheThings() T-Shirt (Red)",
          "action": lambda: driver_chrome.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)').click()},
    "7": {"name": "Выйти из магазина", "action": lambda: exit()}
}

# вызываем меню магазина
def market_menu():
    print("Приветствую тебя в нашем интернет - магазине")
    cart_link = driver_chrome.find_element(By.XPATH, "//a[@class= 'shopping_cart_link']")

    while True:
        print("\nВыбери один из следующих товаров и укажи его номер: ")
        for key, product in data_market.items():
            print(f"{key} - {product['name']}")

        enter = input("Нажмите на цифру пункта меню: ")

        if enter in data_market:
            if enter == "7":
                print("Выходим из магазина")
                data_market[enter]["action"]()
            else:
                data_market[enter]["action"]()
                print(f"Вы выбрали {data_market[enter]['name']}")
                cart_link.click()
                return
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 7")

market_menu()

# сохраняем в переменные название и цену выбранного товара
check_item = driver_chrome.find_element(By.XPATH, "//div[@class= 'inventory_item_name']").text
check_price = driver_chrome.find_element(By.XPATH, "//div[@class= 'inventory_item_price']").text
click_checkout = driver_chrome.find_element(By.XPATH, "//button[@id= 'checkout']").click()

# с помощью фейкера вводим имя/фамилию/пароль
first_name = fake.name()
last_name = fake.last_name()
postal_code = fake.password()
click_first_name = driver_chrome.find_element(By.ID, 'first-name').send_keys(first_name) # вводим имя
click_last_name = driver_chrome.find_element(By.ID, 'last-name').send_keys(last_name) # вводим фамилию
click_code = driver_chrome.find_element(By.ID, 'postal-code').send_keys(postal_code) # вводим пароль
time.sleep(1)
click_continue = driver_chrome.find_element(By.ID, "continue").click()

# проверяем название и цену товара в корзине
inventory_item = driver_chrome.find_element(By.XPATH, "//div[@class= 'inventory_item_name']").text
assert inventory_item == check_item
print(f"Название {inventory_item} соответствует")
inventory_price = driver_chrome.find_element(By.XPATH, "//div[@class= 'inventory_item_price']").text
assert inventory_price == check_price
print(f"Цена {inventory_price} соответствует")
click_finish = driver_chrome.find_element(By.ID, "finish").click()

# совершаем покупку и проверяем финишную страницу
check_complete = driver_chrome.find_element(By.XPATH, "//span[@class= 'title']").text
assert check_complete == "Checkout: Complete!"
print("Поздравляем! Вы совершили покупку")