from selenium.webdriver.common.by import By

from unilities.web_ui.base_page import BasePage


class AboutUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __about_us_form = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator mat-elevation-z6']")

    def is_about_us_form_present(self):
        return self.is_element_present(self.__about_us_form)