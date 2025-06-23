import time
from selenium import webdriver


# Comando de aplicação denttro do 'browser.' não precisa de (), ja retorna como str
browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://google.com")

# (title) → printa o titulo da página
print("Esse é o título da página →", browser.title)

# (current_url) → printa a URL da página
print("A URL da página é →",browser.current_url)

# (page_source) → printa o código fonte da página
print("O código fonte  da página é →", browser.page_source)
time.sleep(2)
