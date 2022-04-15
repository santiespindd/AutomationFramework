import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import moment
import allure


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)

        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):

        try:
            driver = self.driver
            home_page = HomePage(driver)

            home_page.click_welcome()
            home_page.click_logout()
            x = driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            current_date = moment.now().strftime("%H-%M-%S_%m-%d-%Y")
            test_name = utils.whoami()
            screenshot_name = test_name + "_"+ current_date
            #screenshoot
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name , attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Santi/PycharmProjects/AutomationFramework/screenshots" + screenshot_name + ".png")
            raise
        except:
            print("Some exception occurred")
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("This block will (lw(ys execute | Close DB")
