import time
import pytest

from pages.login_page import LoginPage
from tests import conftest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginInvalido
class TestCT02:
    def test_ct02_login_invalido(self):
        driver = conftest.driver
        login_page = LoginPage()
        login_page.fazer_login("standard_user", "test_errorzz")

        alert_erro_messagen = driver.find_element(By.XPATH, "//*[@class='error-message-container error']")
        print(alert_erro_messagen.text)
        assert alert_erro_messagen.text == "Epic sadface: Username and password do not match any user in this service"
        time.sleep(3)