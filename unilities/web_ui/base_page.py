from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for_element_located(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_elements_located(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def move_to_element(self, locator):
        ActionChains(self.driver).move_to_element(locator).perform()

    def get_text(self, locator):
        element = self.wait_for_element_located(locator)
        return element.text

    def click(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    def select_from_menu_content(self, value, locator):
        elements = self.wait_for_elements_located(locator)
        for element in elements:
            if element.text.strip() == value:
                element.click()
                break

    def send_keys(self, locator, value, is_clear=False):
        element = self.wait_for_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def is_element_present(self, locator):
        try:
            self.wait_for_element_located(locator)
            return True
        except TimeoutException:
            return False

    def is_element_active(self, locator):
            element = self.wait_for_element_located(locator)
            state = element.get_attribute('disabled')
            if state == 'true':
                return False
            elif state == 'false':
                return True