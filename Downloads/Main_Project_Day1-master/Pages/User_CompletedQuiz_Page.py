import logging
from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base


class User_CompletedQuiz_Page(Base_Page):
    LIST_OF_QUIZ_TITLES = "//tbody/tr/td[1]"
    LIST_OF_CATEGORIES = "//tbody//td[2]"
    CATEGORY_DROPDOWN = (By.ID, "categorySelect")

    def __init__(self, driver):
        super().__init__(driver)
        dict_d = {}
        dict_d = Test_Data.getTestData(self, "BaseData", "test_URL")
        self.driver.get(dict_d["name"])

    # Function for verifying the completed quiz
    def quiz_title_verification(self, str1):
        log = test_Base.getLogger()

        # Retreiving the quiz title web elements into a list
        l1 = self.driver.find_elements_by_xpath(User_CompletedQuiz_Page.LIST_OF_QUIZ_TITLES)
        count = 0
        log.info(f"str == {str1}")

        # Verifying the completed quiz with the quiz which are there in completed section
        for i in range(len(l1)):
            if l1[i].text == str1:
                count += 1

        assert count > 0
        log.info("The quiz completed is present in completed quiz section")

    # Function for filtering the records by category
    def filter_by_category(self):
        log = test_Base.getLogger()

        sel = self.dropdown_operation(User_CompletedQuiz_Page.CATEGORY_DROPDOWN)
        dict_d = {}

        dict_d = Test_Data.getTestData(self, "QuizCategory", "test_Python")
        log.info(dict_d)

        str1 = dict_d["name"]

        sel.select_by_visible_text(str1)

        #Retrieving the categories into a list
        categoryList = self.driver.find_elements_by_xpath(User_CompletedQuiz_Page.LIST_OF_CATEGORIES)

        if len(categoryList) == 0:
            log.info("No quiz completed with selected category")

        else:
            for i in range(len(categoryList)):
                assert categoryList[i].text == str1

        log.info(" Filter is applied correctly by category")
