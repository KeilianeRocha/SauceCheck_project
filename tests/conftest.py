"""import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():
    # setup
    global driver
    # Config. modo anônimo
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Ativa o modo anônimo
    driver = webdriver.Chrome(options=chrome_options)  # instancia o Chrome como driver desse teste
    driver.implicitly_wait(12)  # fica fazendo verificação ate fazer o teste
    # Acessa página
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test
    yield

    # teardown
    driver.quit()
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


@pytest.fixture()
def setup_teardown():
    # Configurações para o GitHub Actions
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Execução sem interface gráfica
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # Configuração específica para evitar conflitos de user-data-dir
    chrome_options.add_argument("--remote-debugging-port=9222")

    # Caminho para o chromedriver (necessário no GitHub Actions)
    service = Service(executable_path='/usr/bin/chromedriver')

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        yield driver
    finally:
        driver.quit()