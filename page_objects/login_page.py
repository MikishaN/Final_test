from selenium.webdriver.common.by import By

from page_objects.forgot_password_page import ForgotPasswordPage
from unilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_form = (By.XPATH, '//div[@id = "login-form"]')
    __email_input = (By.XPATH, '//input[@id = "email"]')
    __password_input = (By.XPATH, '//input[@id = "password"]')
    __login_button = (By.XPATH, '//button[@id = "loginButton"]')
    __invalid_creds_error = (By.CSS_SELECTOR, '.error')
    __empty_email = (By.XPATH, '//mat-error[@id="mat-error-0"]')
    __empty_password = (By.XPATH, '//mat-error[@id="mat-error-1"]')
    __forgot_pass_link = (By.XPATH, '//a[@href = "#/forgot-password"]')

    def is_login_form_present(self):
        return self.is_element_present(self.__login_form)

    def enter_email(self, email):
        self.send_keys(self.__email_input, email)
        return self

    def enter_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        return self

    def get_error_messages(self):
        return self.get_text(self.__invalid_creds_error)

    def is_login_button_active(self):
        return self.is_element_active(self.__login_button)

    def click_email_field(self):
        self.click(self.__email_input)
        return self

    def click_password_field(self):
        self.click(self.__password_input)
        return self

    def get_error_message_empty_email(self):
        return self.get_text(self.__empty_email)

    def get_error_message_empty_password(self):
        return self.get_text(self.__empty_password)

    def open_forgot_password_page(self):
        self.move_to_element(self.__forgot_pass_link)
        self.click(self.__forgot_pass_link)
        return ForgotPasswordPage(self.driver)

