import pytest

from selenium.webdriver import Chrome
from pages.loginPage import EbayLoginPage
from pages.homePage import EbayHomePage


@pytest.fixture()
def browser():
    driver = Chrome()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


def test_failed_login(browser):
    EMAIL = 'Hola@hola.com'
    PASSWORD = '12345678'

    home_page = EbayHomePage(browser)
    home_page.load_home_page()
    home_page.click_login_button()

    login_page = EbayLoginPage(browser)
    login_page.set_email_input(EMAIL)
    login_page.set_password_input(PASSWORD)
    login_page.click_login()
