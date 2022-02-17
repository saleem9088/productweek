import logging

from Pages.User_CompletedQuiz_Page import User_CompletedQuiz_Page
from Pages.User_DashBoard_Page import User_DashBoard_Page
from Pages.User_Login_Page1 import User_Test_LoginPage1
from Pages.User_PendingQuiz_Page import User_PendingQuiz_Page
from Pages.User_Quiz_Page import User_Quiz_Page
from Utilities.test_Base import test_Base


class Test_CompleteQuiz_User(test_Base):
    def test_CompletedQuizCategory(self):

        # Object creation of necessary pages
        log = test_Base.getLogger()
        log.info("Complete quiz method started")

        self.login = User_Test_LoginPage1(self.driver)
        self.dashboard = User_DashBoard_Page(self.driver)
        self.pendingQuiz = User_PendingQuiz_Page(self.driver)
        self.quiz = User_Quiz_Page(self.driver)
        self.completedQuiz = User_CompletedQuiz_Page(self.driver)

        # To login the account
        self.login.login1()
        log.info("Login is done")

        # To enter the pending quiz button
        self.dashboard.click_pending_quiz_button()

        try:
            # Taking the text of the quiz title
            quiz_title = self.pendingQuiz.quiz_title()

            # To enter the quiz
            self.pendingQuiz.click_attempt_quiz_button()

            # To take up the quiz
            self.quiz.take_quiz()
            self.dashboard.click_completed_quiz_button()

            # To verify the completed quiz is present in compled section
            self.completedQuiz.quiz_title_verification(quiz_title)
        except:
            log.info("There are no quiz in pending quiz section")
