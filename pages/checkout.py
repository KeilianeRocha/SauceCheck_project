import time
from tabnanny import check

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Comandos 'assert' → sempre espera um retorno da condição True

# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste
browser.implicitly_wait(12) # fica fazendo verificação ate fazer o teste

# Acessa página
browser.maximize_window()
browser.get("https://www.saucedemo.com/")
wait = WebDriverWait(browser, 30)

username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login = browser.find_element(By.ID, "login-button").click()

homePage = browser.find_element(By.XPATH, "//*[@class='app_logo']")
print(homePage.text)
assert homePage.text == "Swag Labs"

# Selecionar produto

browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# visualizar no carro
browser.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
checkproduct = browser.find_element(By. XPATH, "//*[@class='inventory_item_name']")
print(checkproduct.text)
assert checkproduct.text == "Sauce Labs Backpack"

# Checkout
browser.find_element(By.ID, "checkout").click()
firstName = browser.find_element(By.ID, "first-name").send_keys("Teste")
lastName = browser.find_element(By.ID, "last-name").send_keys("Lorem")
zipCode = browser.find_element(By.ID, "postal-code").send_keys("12345-010")
continue_button = browser.find_element(By.ID, "continue").click()

# Checar carrinho
catPage = browser.find_element(By.XPATH, "//*[@class='title']")
print(catPage.text)
assert catPage.text == "Checkout: Overview"

# Finalizar carrinho
browser.find_element(By.ID, "finish").click()

# Mensagem final
checkComplete = browser.find_element(By.XPATH, "//*[@class='complete-header']")
print(checkComplete.text)
assert checkComplete.text == "Thank you for your order!"

# Voltar para home
browser.find_element(By.ID, "back-to-products").click()
time.sleep(3)