from CommonImportsPkg.common_imports import *
from login import Login


class PurchaseSummaryReportTest(unittest.TestCase):
    def __init__(self, methodName='test_purchase_summary_report', data=None):
        super(PurchaseSummaryReportTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_purchase_summary_report(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_purchase_summary_report']['username']
            # password = self.data['test_purchase_summary_report']['password']
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

            sidebar_menu_purchase_summary_report = self.driver.find_element(By.XPATH,
                                                                            "//span[text()='Purchase Summary Report']")
            self.assertTrue(sidebar_menu_purchase_summary_report.is_displayed(),
                            msg="Purchase Summary Report menu is not displayed.")
            sidebar_menu_purchase_summary_report.click()
            time.sleep(5)

            business_unit = self.data['test_purchase_summary_report']['Business_Unit']
            input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            order_status = self.data['test_purchase_summary_report']['Order_Status']
            input_order_status = self.driver.find_element(By.ID, "docstatus")
            self.assertTrue(input_order_status.is_displayed(), msg="Order Status input is not displayed.")
            input_order_status.send_keys(order_status)
            time.sleep(5)

            supplier = self.data['test_purchase_summary_report']['Supplier']
            input_supplier = self.driver.find_element(By.ID, "p_supplier_id")
            self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
            input_supplier.send_keys(supplier)
            time.sleep(5)

            run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
            self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
            if input_business_unit is not None:
                run_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
