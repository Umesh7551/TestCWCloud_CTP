
from CommonImportsPkg.common_imports import *


class Login:
    def __init__(self, driver, data, test_case):
        self.driver = driver
        self.data = data
        self.test_case = test_case
        # print(self.test_case)
    def login(self):
        self.driver.maximize_window()
        self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
        time.sleep(5)
        username = self.data['login']['username']
        password = self.data['login']['password']
        username_input = self.driver.find_element(By.ID, "username")
        self.test_case.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
        username_input.send_keys(username)
        time.sleep(5)

        password_input = self.driver.find_element(By.ID, "password")
        self.test_case.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
        password_input.send_keys(password)
        time.sleep(5)

        login_button = self.driver.find_element(By.ID, "login")
        self.test_case.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
        login_button.click()
        time.sleep(10)
