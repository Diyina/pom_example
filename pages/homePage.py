from selenium.webdriver.common.by import By


class EbayHomePage:
    URL = 'https://www.ebay.com'
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#gh-ug > a:nth-child(1)')


    def __init__(self, browser):
        self.browser = browser

    def load_home_page(self):
        self.browser.get(self.URL)

    def click_login_button(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()
