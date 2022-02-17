import time

from Pages.Admin_Login_Page import Login_Page
from Pages.All_Quiz import All_Quiz
from Pages.Create_Quiz import Create_Quiz
from Pages.User_CompletedQuiz_Page import User_CompletedQuiz_Page
from Pages.User_DashBoard_Page import User_DashBoard_Page
from Pages.User_Login_Page1 import User_Test_LoginPage1
from Pages.User_PendingQuiz_Page import User_PendingQuiz_Page
from Pages.User_Quiz_Page import User_Quiz_Page
from Testscripts.test_CompleteQuiz_User import Test_CompleteQuiz_User
from Utilities.test_Base import test_Base


class Test_Add_New_Quiz(test_Base):

    def test_e2e_new_quiz_functionality(self):
        try:

            self.login = Login_Page(self.driver)
            self.login.log.info("Navigating to login page of application HQM...")
            self.login.base_login_to_application()
            self.login.log.info("Login functionality for admin user is successfully validated")
            self.create_quiz = Create_Quiz(self.driver)
            self.create_quiz.navigate_to_Quiz_creation_section()
            quizname = self.create_quiz.creating_new_quiz()
            self.Allquiz = All_Quiz(self.driver)
            self.Allquiz.navigate_to_quiz_section()
            a = self.login.is_text_present(quizname)
            #assert True == a
            batch = self.Allquiz.Adding_question_to_quiz(quizname)
            self.login.log.info("Batch is successfully returned"+" "+batch)
            self.login.logout()

            self.userlogin = User_Test_LoginPage1(self.driver)
            self.login.log.info("Logging in as a user")
            self.userlogin.login1()
            # self.login.navigate_to_dashboard()
            a = self.login.is_text_present(quizname)
            self.login.log.info("Quiz is successfully assigned to User")
            self.login.log.info(a)
            self.login.log.info(type(a))
            assert True == a

            self.pendingQuiz = User_PendingQuiz_Page(self.driver)
            self.dashboard = User_DashBoard_Page(self.driver)
            self.quiz = User_Quiz_Page(self.driver)
            self.completedQuiz = User_CompletedQuiz_Page(self.driver)
            self.dashboard.click_pending_quiz_button()
            self.driver.refresh()
            quiz_title = self.pendingQuiz.quiz_title()

            # To enter the quiz
            self.pendingQuiz.click_attempt_quiz_button()

            # To take up the quiz
            self.quiz.take_quiz()
            self.dashboard.click_completed_quiz_button()

            # To verify the completed quiz is present in compled section
            self.completedQuiz.quiz_title_verification(quiz_title)

        except Exception as e:
            self.login.log.error("Could not add questions to quiz...")
            self.login.log.info(e)
            assert False
