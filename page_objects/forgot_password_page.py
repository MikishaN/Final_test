from selenium.webdriver.common.by import By

from unilities.web_ui.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __forgot_form = (By.XPATH, '//div[@id="forgot-form"]')

    def is_forgot_form_present(self):
        return self.is_element_present(self.__forgot_form)
