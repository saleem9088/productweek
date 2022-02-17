import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import Test_Data


class Base_Page:

    def __init__(self, driver):
        self.driver = driver
        '''
        dict_d = {}
        dict_d = Test_Data.getTestData(self, "BaseData", "test_URL")
        self.driver.get(dict_d["name"])
        '''

    def enter_url_operation(self, url, locator):
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
            print("Page is ready!")
        except TimeoutException as e:
            print("Loading took too much time!", e)

    def click_operation(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).click()
        time.sleep(5)

    def clear_text_operation(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).clear()
        time.sleep(5)
        # WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator)).send_keys(

    def send_keys_operation(self, locator, text):
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def send_keys_js(self, locator, loc, keys):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        # self.driver.executeScript("document.getElementByClassName('" + loc + "').setAttribute('value', '" + keys + "')")
        javaScript = "document.getElementsByClassName('" + loc + "')[0].value = '" + keys + "' "
        self.driver.execute_script(javaScript)

    def get_text_from_locator(self, locator):
        text = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).text
        return text

    def get_attribute_value(self, locator, attribute):
        text = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute)
        return text

    def get_title(self):
        get_title = self.driver.title
        return get_title

    def implicit_waiting(self):
        self.driver.implicitly_wait(30)

    def Hover_operation(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        a = ActionChains(self.driver)
        a.move_to_element(
            WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))).perform()
        time.sleep(5)

    def Switch_to_child_window(self, win):

        self.driver.switch_to.window(self.driver.window_handles[win])

    def is_text_present(self, text):
        time.sleep(5)
        return str(text) in self.driver.page_source

    def scroll_operation(self):
        self.driver.execute_script("window.scrollTo(0,250)")

    def element_exist_check(self, locator):
        if WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)):
            return True
        else:
            return False

    def get_all_dropdown_option(self, locator):
        select_box = self.driver.find_element_by_xpath(locator)
        options = [x for x in select_box.find_elements_by_tag_name("option")]
        op = ""
        for element in options:
            print(element.text)
                  #get_attribute("value"))
            op = op +" "+ element.text
        return op

    def select_option_dropdown(self, locator, index):
        ddelement = Select(self.driver.find_element_by_xpath(locator))
        ddelement.select_by_index(index)

    def select_option_byvisibletext(self, locator, text):
        ddelement = Select(self.driver.find_element_by_xpath(locator))
        ddelement.select_by_visible_text(text)

    def dropdown_operation(self, locator):
        ele = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return Select(ele)
