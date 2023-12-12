from CommonImportsPkg.common_imports import *
from login import Login


class SalesTaxReportTest(unittest.TestCase):
    def __init__(self, methodName='test_sales_tax_report', data=None):
        super(SalesTaxReportTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_sales_tax_report(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_sales_tax_report']['username']
            # password = self.data['test_sales_tax_report']['password']
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

            menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
            self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
            menu_reports.click()
            time.sleep(5)

            sidebar_menu_sales_tax_report = self.driver.find_element(By.XPATH,
                                                                     "//span[text()='Sales Tax Report']")
            self.assertTrue(sidebar_menu_sales_tax_report.is_displayed(),
                            msg="Sales Tax Report menu is not displayed.")
            sidebar_menu_sales_tax_report.click()
            time.sleep(5)

            store = self.data['test_sales_tax_report']['Store']
            input_store = self.driver.find_element(By.ID, "cs_bunit_id")
            self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
            input_store.send_keys(store)
            time.sleep(5)

            run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
            self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
            if input_store is not None:
                run_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
