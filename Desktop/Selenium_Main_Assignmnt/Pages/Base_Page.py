import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page:

    def __init__(self, driver):
        self.driver = driver

    def enter_url_operation(self, url, locator):
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException as exp:
            print("Loading took too much time!", exp)

    def click_operation(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).click()
        time.sleep(5)

    def send_keys_operation(self, locator, text):
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def send_keys_js(self, locator, loc, keys):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        javaScript = "document.getElementsByClassName('" + loc + "')[0].value = '" + keys + "' "
        self.driver.execute_script(javaScript)

    def get_text_from_locator(self, locator):
        text = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).text
        return text

    def get_attribute_value(self, locator, attribute):
        text = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute)
        return text

    def Switch_to_child_window(self, windownumber):

        self.driver.switch_to.window(self.driver.window_handles[windownumber])

    def is_text_present(self, text):
        return str(text) in self.driver.page_source

    def scroll_operation(self):
        self.driver.execute_script("window.scrollTo(0,250)")

    def element_exist_check(self, locator):
        if WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)):
            return True
        else:
            return False

    def get_title(self):
        get_title = self.driver.title
        return get_title

    def clear_text_operation(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).clear()

    def implicit_waiting(self):
        self.driver.implicitly_wait(30)

    def Hover_operation(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        a = ActionChains(self.driver)
        a.move_to_element(
            WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))).perform()
