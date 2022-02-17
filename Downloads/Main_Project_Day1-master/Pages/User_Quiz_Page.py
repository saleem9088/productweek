import logging
from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base


class User_Quiz_Page(Base_Page):
    START_QUIZ_BUTTON = (By.XPATH, "//button[text()=' Start Quiz ']")
    FIRST_OPTION_CHECKBOX = (By.XPATH, "//input[@type='checkbox'][1]")
    NEXT_BUTTON = (By.XPATH, "//span[text()=' Next ']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")

    def __init__(self, driver):
        super().__init__(driver)
        dict_d = {}
        dict_d = Test_Data.getTestData(self, "BaseData", "test_URL")
        self.driver.get(dict_d["name"])

    #Function to attempt the quiz
    def take_quiz(self):
        log = test_Base.getLogger()
        log.info("From take quiz method in Quiz page")

        #CLicking the start button
        self.click_operation(User_Quiz_Page.START_QUIZ_BUTTON)
        log.info("Start button is clicked")

        flag = True
        questionNumber = 0

        #For answering the questions
        while flag:
            self.click_operation(User_Quiz_Page.FIRST_OPTION_CHECKBOX)
            try:
                self.click_operation(User_Quiz_Page.NEXT_BUTTON)
                questionNumber += 1
                log.info(f"Question number {questionNumber} is answered")
            except:
                self.click_operation(User_Quiz_Page.SUBMIT_BUTTON)
                log.info("Successfully completed the quiz")
                flag = False