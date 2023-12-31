from CommonImportsPkg.common_imports import *
from login import Login


class QuickStockIssueTest(unittest.TestCase):
    def __init__(self, methodName='test_quick_stock_issue', data=None):
        super(QuickStockIssueTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_quick_stock_issue(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_quick_stock_issue']['username']
            # password = self.data['test_quick_stock_issue']['password']
            # username_input = self.driver.find_element(By.ID, "username")
            # self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
            # username_input.send_keys(username)
            # time.sleep(5)
            #
            # # Step 5: Enter password in the password input box
            # password_input = self.driver.find_element(By.ID, "password")
            # self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
            # password_input.send_keys(password)
            # time.sleep(5)
            #
            # # Step 6: Click on the login button
            # login_button = self.driver.find_element(By.ID, "login")
            # self.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
            # login_button.click()
            # time.sleep(10)
            # Step 6: Select Store Admin
            store_admin = self.driver.find_element(By.XPATH, "//h4[text()='Store Admin']")
            # Check if the element is displayed
            self.assertTrue(store_admin.is_displayed(), msg="Store Admin is not displayed")
            store_admin.click()
            time.sleep(10)

            menu_inventory = self.driver.find_element(By.XPATH, "//span[text()='Inventory']")
            self.assertTrue(menu_inventory.is_displayed(), msg="Inventory Menu is not Displayed")
            menu_inventory.click()
            time.sleep(5)

            sidebar_menu_quick_stock_issue = self.driver.find_element(By.XPATH,
                                                                      "//span[text()='Quick Stock Issue']")
            self.assertTrue(sidebar_menu_quick_stock_issue.is_displayed(),
                            msg="Quick Stock Issue menu is not displayed.")
            sidebar_menu_quick_stock_issue.click()
            time.sleep(5)

            source = self.data["test_quick_stock_issue"]["Source"]
            input_source = self.driver.find_element(By.ID, "source")
            self.assertTrue(input_source.is_displayed(), msg="Source input is not displayed.")
            input_source.send_keys(source)
            time.sleep(5)

            destination = self.data["test_quick_stock_issue"]["Destination"]
            input_destination = self.driver.find_element(By.ID, "destination")
            self.assertTrue(input_destination.is_displayed(), msg="Destination input is not displayed.")
            input_destination.send_keys(destination)
            time.sleep(5)

            stock_request = self.data["test_quick_stock_issue"]["Stock_Request"]
            input_stock_request = self.driver.find_element(By.ID, "po")
            self.assertTrue(input_stock_request.is_displayed(), msg="Stock Request input is not displayed.")
            input_stock_request.send_keys(stock_request)
            time.sleep(5)

            remarks = self.data["test_quick_stock_issue"]["Remarks"]
            input_remarks = self.driver.find_element(By.ID, "remarks")
            self.assertTrue(input_remarks.is_displayed(), msg="Remarks input is not displayed.")
            input_remarks.send_keys(remarks)
            time.sleep(5)

            date = self.data["test_quick_stock_issue"]["Date"]
            input_date = self.driver.find_element(By.ID, "date")
            self.assertTrue(input_date.is_displayed(), msg="Date input is not displayed.")
            input_date.send_keys(date)
            time.sleep(5)

            fetch_button = self.driver.find_element(By.ID, "step6")
            self.assertTrue(fetch_button.is_displayed(), msg="Fetch Button is not displayed.")
            if input_source and input_destination and input_stock_request and input_remarks and input_date is not None:
                fetch_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
