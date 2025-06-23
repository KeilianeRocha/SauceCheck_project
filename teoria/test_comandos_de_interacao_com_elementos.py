import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Comandos de interação com elementos dentro de 'element.'

# Config. modo anônimo
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
browser = webdriver.Chrome(options=chrome_options) # instancia o Chrome como browser desse teste

# Acessa página
browser.maximize_window()
browser.get("https://www.saucedemo.com/")

# (find_element()) → encontra uma ocorrência somente / se não encontrar ele retorna ERRO
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

# (send_keys()) → envia informações para os campos dos elementos anteriores
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# click() → clica e entra na prox página
btn_login.click()

# (text) → confirma se o texto do 'xpath' esta na página que foi chamada
home_page = browser.find_element(By.XPATH, "//*[@class='title']")
print(home_page.text)
assert home_page.text == "Products" # o texto tem que ser igual!

# (get_attribute()) →
cart_element = browser.find_element(By.XPATH, "//*[@class='product_sort_container']")
cart_element.click()
time.sleep(5)

# captura o texto
filtro = browser.find_element(By. XPATH, "//*[@value='az']")
filtro.click()
print(filtro.text)
assert filtro.text == "Name (A to Z)"

# captura o texto do indice indicado
img = browser.find_element(By.XPATH, "//img[@class='inventory_item_img'][1]")
print(img.get_attribute("alt"))
assert img.get_attribute("alt") == "Sauce Labs Backpack"
time.sleep(5)


#text
#get_attribute()