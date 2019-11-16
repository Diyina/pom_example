from selenium.webdriver.common.by import By


class EbayLoginPage:
    EMAIL_INPUT = (By.ID, 'userid')
    PASSWORD_INPUT = (By.ID, 'pass')
    LOGIN_BUTTON = (By.ID, 'sgnBt')

    def __init__(self, browser):
        self.browser = browser

    def set_email_input(self, email):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)

    def set_password_input(self, password):
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()
