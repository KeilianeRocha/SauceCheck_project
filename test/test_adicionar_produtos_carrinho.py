import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste
browser.implicitly_wait(12) # fica fazendo verificação ate fazer o teste

# Acessa página
browser.maximize_window()
browser.get("https://www.saucedemo.com/")
wait = WebDriverWait(browser, 30)

# Add credenciais
browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()

# Selecionar produto(mochila)
browser.find_element(By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']").click() # clica no produto
browser.find_element(By. XPATH, "//*[text()='Add to cart']").click() # clica em add

# mapear(mochila) no carrinho
browser.find_element(By. XPATH, "//*[@class='shopping_cart_link']").click()
assert browser.find_element(By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']").is_displayed()



# voltar para home page
browser.find_element(By.ID,"continue-shopping").click()

# Selecionar produto (bike light)
browser.find_element(By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Bike Light']").click() # clica no produto
browser.find_element(By. XPATH, "//*[text()='Add to cart']").click() # clica em add

# mapear(produtos) no carrinho
browser.find_element(By. XPATH, "//*[@class='shopping_cart_link']").click()
assert browser.find_element(By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']").is_displayed()
assert browser.find_element(By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Bike Light']").is_displayed()


time.sleep(2)
browser.quit()
