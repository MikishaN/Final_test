from selenium.webdriver.common.by import By

from unilities.web_ui.base_page import BasePage


class CustomerFeedbackPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __customer_feedback_form = (By.XPATH, "//div[@id='feedback-form']")
    __comment_input = (By.XPATH, "//div[@class='mat-form-field-infix ng-tns-c119-10']")
    __result_input = (By.XPATH, "//div[@class='mat-form-field-infix ng-tns-c119-9']")
    __empty_comment = (By.XPATH, "//mat-error[@class='mat-error ng-tns-c119-10 ng-star-inserted']")
    __empty_result = (By.XPATH, "//mat-error[@class='mat-error ng-tns-c119-9 ng-star-inserted']")

    def is_customer_feedback_form_present(self):
        return self.is_element_present(self.__customer_feedback_form)

    def click_comment_field(self):
        self.click(self.__comment_input)
        return self

    def click_result_field(self):
        self.click(self.__result_input)
        return self

    def get_error_message_empty_comment(self):
        return self.get_text(self.__empty_comment)

    def get_error_message_empty_result(self):
        return self.get_text(self.__empty_result)