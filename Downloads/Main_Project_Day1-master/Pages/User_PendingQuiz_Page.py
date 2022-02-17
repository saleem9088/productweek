import logging
from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base

class User_PendingQuiz_Page(Base_Page):
    FIRST_QUIZ_BUTTON = (By.XPATH, "//th[text()='1' and @scope]/ancestor::tr/td/div/button")
    QUIZ_TITLE = (By.XPATH, '(//tbody/tr/td[1])[1]')
    LIST_OF_QUIZ_TITLES = "//tbody/tr/td[1]"
    LIST_OF_CATEGORIES = "//tbody//td[4]"
    CATEGORY_DROPDOWN = (By.ID, "categorySelect")

    def __init__(self, driver):
        super().__init__(driver)
        dict_d = {}
        dict_d = Test_Data.getTestData(self, "BaseData", "test_URL")
        self.driver.get(dict_d["name"])

    def click_attempt_quiz_button(self):
        log = test_Base.getLogger()
        log.info("From pending quiz page")

        self.click_operation(User_PendingQuiz_Page.FIRST_QUIZ_BUTTON)
        log.info("user has entered the quiz")

    def quiz_title(self):
        return self.get_text_from_locator(User_PendingQuiz_Page.QUIZ_TITLE)

    def filter_by_category(self):
        log = test_Base.getLogger()

        sel = self.dropdown_operation(User_PendingQuiz_Page.CATEGORY_DROPDOWN)
        dict_d = {}

        dict_d = Test_Data.getTestData(self, "QuizCategory", "test_Java")
        log.info(dict_d)

        str1 = dict_d["name"]

        sel.select_by_visible_text(str1)

        # Retrieving the categories into a list
        categoryList = self.driver.find_elements_by_xpath(User_PendingQuiz_Page.LIST_OF_CATEGORIES)

        if len(categoryList) == 0:
            log.info("No quiz completed with selected category")

        else:
            for i in range(len(categoryList)):
                assert categoryList[i].text == str1

        log.info(" Filter is applied correctly by category")