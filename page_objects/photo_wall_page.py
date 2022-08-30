from selenium.webdriver.common.by import By

from unilities.web_ui.base_page import BasePage


class PhotoWallPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __photo_wall_form = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator heading mat-elevation-z6 "
                                   "mat-own-card']")

    def is_photo_wall_form_present(self):
        return self.is_element_present(self.__photo_wall_form)