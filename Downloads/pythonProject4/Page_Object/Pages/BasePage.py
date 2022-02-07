import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Page_Object.Test_Base.Test_Setup import Test_Setup


class Base_page(Test_Setup):

    def click_operation(self, locator):
        #print(locator)
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).click()

    def send_keys_operation(self, locator, keys):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).send_keys(keys)

    def get_text_from_locator(self, locator):
        text = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).text
        return text

    def get_attribute_value(self, locator, attribute):
        text = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute)
        return text

    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    def switch_between_frame(self,frame):
        self.driver.switch_to.frame(frame)

    def switch_default(self):
        self.driver.switch_to.default_content()

    def items_to_dictonary(self, locator):
        dict_obj = {}
        for i in range(1, 12, 2):
            j=0
            st= "(//*[@class='container']//child::div//p)[{0}]".format(i)
            strr = self.driver.find_element(By.XPATH, st).text
            j=1+i
            str1 = "(//*[@class='container']//child::div//p)[{0}]".format(j)
            strr1 = self.driver.find_element(By.XPATH, str1).text

            strr1 = [int(i) for i in strr1.split() if i.isdigit()]
            dict_obj[strr] = strr1
        return dict_obj

    def get_url_operation(self, url, locator):
        self.driver.get(url)
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
