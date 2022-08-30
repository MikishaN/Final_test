import random

from selenium.webdriver.common.by import By
from selenium import webdriver

from page_objects.about_us_page import AboutUsPage
from page_objects.customer_feedback_page import CustomerFeedbackPage
from page_objects.login_page import LoginPage
from page_objects.photo_wall_page import PhotoWallPage
from unilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    __page_title = (By.XPATH, '//button[@aria-label= "Back to homepage"]/span[@class="mat-button-wrapper"]/span')
    __pagination_dropdown = (By.XPATH, "//mat-select[@role='combobox']")
    __product = (By.CSS_SELECTOR, "mat-card")
    __product_name = (By.CSS_SELECTOR, "[class='item-name']")
    __dismiss_button = (By.XPATH, "//*[text()='Dismiss']")
    __language_button = (By.XPATH, "//button[@aria-label='Language selection menu']")
    __language_radio_button = (By.XPATH, "//span[@class='mat-radio-label-content']/div")
    __items_header = (By.XPATH, "//app-search-result/div/div/div/div[@class='ng-star-inserted']")
    __search_icon = (By.XPATH, "//mat-icon[text() = ' search ']")
    __search_field = (By.XPATH, "//input[@type='text']")
    __search_result = (By.XPATH, "//div[@class='ng-star-inserted']")
    __not_found_search_result = (By.XPATH, "//span[@class = 'noResultText']")
    __account_button = (By.XPATH, "//button[@id = 'navbarAccount']")
    __login_button = (By.XPATH, "//button[@id = 'navbarLoginButton']")
    __menu_button = (By.XPATH, "//button[@class='mat-focus-indicator mat-tooltip-trigger mat-button mat-button-base']")
    __contact_page_open = (By.XPATH, "//a[@href='#/contact']")
    __about_us_page_open = (By.XPATH, "//a[@href='#/about']")
    __photo_wall_page_open = (By.XPATH, "//a[@href='#/photo-wall']")
    __git_hub_open = (By.XPATH, "//a[@class='mat-list-item mat-focus-indicator mat-list-item-with-avatar "
                                "ng-star-inserted']")
    __help_getting_button = (By.XPATH, "//mat-nav-list/a[@class='mat-list-item mat-focus-indicator ng-star-inserted']")
    __pop_up_help_getting = (By.XPATH, "//div[@id='hacking-instructor']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def get_page_title(self):
        return self.get_text(self.__page_title)

    def get_pagination_value(self):
        return self.get_text(self.__pagination_dropdown)

    def get_products_quantity(self):
        return len(self.wait_for_elements_located(self.__product))

    def click_dismiss_button(self):
        self.click(self.__dismiss_button)

    def select_language(self, language):
        self.click(self.__language_button)
        self.select_from_menu_content(language, self.__language_radio_button)

    def get_items_header(self):
        return self.get_text(self.__items_header)

    def choose_random_product(self):
        products = self.wait_for_elements_located(self.__product_name)
        random_product = random.choice(products)
        return random_product.text

    def click_search_icon(self):
        self.click(self.__search_icon)

    def search_existing_product(self, existing_product):
        return self.send_keys(self.__search_field, existing_product)

    def get_search_value(self):
        return self.get_text(self.__search_result)

    def get_not_found_search_value(self):
        return self.get_text(self.__not_found_search_result)

    def open_login_page(self):
        self.click(self.__account_button)
        self.click(self.__login_button)
        return LoginPage(self.driver)

    def open_feedback_page(self):
        self.click(self.__menu_button)
        self.click(self.__contact_page_open)
        return CustomerFeedbackPage(self.driver)

    def open_about_us_page(self):
        self.click(self.__menu_button)
        self.click(self.__about_us_page_open)
        return AboutUsPage(self.driver)

    def open_photo_wall_page(self):
        self.click(self.__menu_button)
        self.click(self.__photo_wall_page_open)
        return PhotoWallPage(self.driver)

    def open_git_hub(self):
        self.click(self.__menu_button)
        self.click(self.__git_hub_open)
        return 'https://github.com/juice-shop/juice-shop'

    def open_info_pop_up_help_getting_started(self):
        self.click(self.__menu_button)
        self.click(self.__help_getting_button)
        return self.get_text(self.__pop_up_help_getting)
