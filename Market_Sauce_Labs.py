import time
from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')
options.add_argument('--headless')
fake = Faker("ru_RU")

driver_chrome = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com' # Даём ссылку на тестируемый сайт
driver_chrome.get(base_url) # открываем ссылку в браузере Chrome
driver_chrome.set_window_size(1261, 2399) # задаем параметры окна разрешения

user_name = driver_chrome.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input')
user_name.send_keys("standard_user") # вводим логин

password = driver_chrome.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce") # вводим пароль

button_login = driver_chrome.find_element(By.ID, 'login-button')
button_login.click() # кликаем на авторизацию

# сохраняем товары в переменные
backpack = driver_chrome.find_element(By.XPATH, "//button[@id= 'add-to-cart-sauce-labs-backpack']")
bike_Light = driver_chrome.find_element(By.XPATH, "//button[@id= 'add-to-cart-sauce-labs-bike-light']")
bolt_TShirt = driver_chrome.find_element(By.XPATH, "//button[@id= 'add-to-cart-sauce-labs-bolt-t-shirt']")
fleece_Jacket = driver_chrome.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
onesie = driver_chrome.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
test_TShirt = driver_chrome.find_element(By.XPATH, "//button[@id= 'add-to-cart-test.allthethings()-t-shirt-(red)']")

print("Приветствую тебя в нашем интернет - магазине")

# вызываем меню магазина
def market_menu():
    enter = input("Выбери один из следующих товаров и укажи его номер: "
        "\n1 - Sauce Labs Backpack, "
        "\n2 - Sauce Labs Bike Light, "
        "\n3 - Sauce Labs Bolt T-Shirt, "
        "\n4 - Sauce Labs Fleece Jacket, "
        "\n5 - Sauce Labs Onesie, "
        "\n6 - Test.allTheThings() T-Shirt (Red)"
        "\n7 - Выйти из магазина"
        "\nНажмите на цифру пункта меню: ")

    if enter == "1":
        backpack.click()
        print("Вы выбрали Backpack")
    elif enter == "2":
        bike_Light.click()
        print("Вы выбрали Bike Light")
    elif enter == "3":
        bolt_TShirt.click()
        print("Вы выбрали Bolt T-Shirt")
    elif enter == "4":
        fleece_Jacket.click()
        print("Вы выбрали Fleece Jacket")
    elif enter == "5":
        onesie.click()
        print("Вы выбрали Onesie")
    elif enter == "6":
        test_TShirt.click()
        print("Вы выбрали T-Shirt (Red)")
    elif enter == "7":
        print("Выходим из магазина")
        exit()

market_menu()

# сохраняем в переменные название и цену выбранного товара
cart_link = driver_chrome.find_element(By.XPATH, "//a[@class= 'shopping_cart_link']")
cart_link.click()
check_item = driver_chrome.find_element(By.XPATH, "//div[@class= 'inventory_item_name']")
value_item = check_item.text
check_price = driver_chrome.find_element(By.XPATH, "//div[@class= 'inventory_item_price']")
value_price = check_price.text
click_checkout = driver_chrome.find_element(By.XPATH, "//button[@id= 'checkout']")
click_checkout.click()

# с помощью фейкера вводим имя/фамилию/пароль
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.password()
click_first_name = driver_chrome.find_element(By.ID, 'first-name')
click_first_name.send_keys(first_name) # вводим имя
click_last_name = driver_chrome.find_element(By.ID, 'last-name')
click_last_name.send_keys(last_name) # вводим имя
click_code = driver_chrome.find_element(By.ID, 'postal-code')
click_code.send_keys(postal_code) # вводим имя
time.sleep(1)
click_continue = driver_chrome.find_element(By.ID, "continue")
click_continue.click()

# проверяем название и цену товара в корзине
inventory_item = driver_chrome.find_element(By.XPATH, "//div[@class= 'inventory_item_name']")
inventory_item_value = inventory_item.text
assert inventory_item_value == value_item
print(f"Название {inventory_item_value} соответствует")
inventory_price = driver_chrome.find_element(By.XPATH, "//div[@class= 'inventory_item_price']")
inventory_price_value = inventory_price.text
assert inventory_price_value == value_price
print(f"Цена {inventory_price_value} соответствует")
click_finish = driver_chrome.find_element(By.ID, "finish")
click_finish.click()

# совершаем покупку и проверяем финишную страницу
check_complete = driver_chrome.find_element(By.XPATH, "//span[@class= 'title']")
complete_value = check_complete.text
assert complete_value == "Checkout: Complete!"
print("Поздравляем! Вы совершили покупку")

driver_chrome.close()