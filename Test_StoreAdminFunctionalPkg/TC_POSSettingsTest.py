from CommonImportsPkg.common_imports import *

class PosSettingsTest(unittest.TestCase):
    def __init__(self, methodName='test_pos_settings', data=None):
        super(PosSettingsTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_pos_settings(self):
        if self.data:
            self.driver.maximize_window()
            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_POS_Settings']['username']
            password = self.data['test_POS_Settings']['password']
            username_input = self.driver.find_element(By.ID, "username")
            self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
            username_input.send_keys(username)
            time.sleep(5)

            # Step 5: Enter password in the password input box
            password_input = self.driver.find_element(By.ID, "password")
            self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
            password_input.send_keys(password)
            time.sleep(5)

            # Step 6: Click on the login button
            login_button = self.driver.find_element(By.ID, "login")
            self.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
            login_button.click()
            time.sleep(10)
            # Step 6: Select Store Admin
            store_admin = self.driver.find_element(By.XPATH, "//h4[text()='Store Admin']")
            # Check if the element is displayed
            self.assertTrue(store_admin.is_displayed(), msg="Store Admin is not displayed")
            store_admin.click()
            time.sleep(5)

            menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
            self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
            menu_settings.click()
            time.sleep(5)

            sidebar_menu_pos_settings = self.driver.find_element(By.XPATH, "//span[text()='POS Settings']")
            self.assertTrue(sidebar_menu_pos_settings.is_displayed(), msg="POS Settings menu is not displayed.")
            sidebar_menu_pos_settings.click()
            time.sleep(5)
            # Payments
            enable_cash_check = self.driver.find_element(By.ID, "mainForm_enableCash")
            self.assertTrue(enable_cash_check.is_displayed(), msg="Enable Cash Check is not displayed.")
            if not enable_cash_check.is_selected():
                enable_cash_check.click()

            enable_card_check = self.driver.find_element(By.ID, "mainForm_enableCard")
            self.assertTrue(enable_card_check.is_displayed(), msg="Enable Card Check is not displayed.")
            if not enable_card_check.is_selected():
                enable_card_check.click()

            # Check if enable_card_integration is displayed and selected
            enable_card_integration = self.driver.find_element(By.ID, "mainForm_enableCardIntegration")
            self.assertTrue(enable_card_integration.is_displayed(), msg="Enable Card Integration is not displayed.")
            if not enable_card_integration.is_selected():
                enable_card_integration.click()

            # Check if input_payment_combo_box is displayed
            payment_combo_box = self.data["test_POS_Settings"]["Payment_Mode"]
            input_payment_combo_box = self.driver.find_element(By.ID, "mainForm_enableCardIntegrationValue")
            self.assertTrue(input_payment_combo_box.is_displayed(), msg="Payment Combo Box is not displayed.")
            input_payment_combo_box.send_keys(payment_combo_box)
            # Customer
            customer_search_check = self.driver.find_element(By.ID, "mainForm_showCustomerSearch")
            self.assertTrue(customer_search_check.is_displayed(), msg="Customer Search Check box is not displayed.")
            if not customer_search_check.is_selected():
                customer_search_check.click()

            customer_search = self.data["test_POS_Settings"]["Customer_Search"]
            customer_search_combo = self.driver.find_element(By.ID, "mainForm_showCustomerSearchValue")
            self.assertTrue(customer_search_combo.is_displayed(), msg="Customer Search Combo is not displayed.")
            customer_search_combo.send_keys()

            search_by_check = self.driver.find_element(By.ID, "mainForm_defaultCustomerSearch")
            self.assertTrue(search_by_check.is_displayed(), msg="Search by check box is not displayed.")
            if not search_by_check.is_selected():
                search_by_check.click()

            by_name_check = self.driver.find_element(By.ID, "mainForm_byName")
            self.assertTrue(by_name_check.is_displayed(), msg="By Name Check box is not displayed")
            if not by_name_check.is_selected():
                by_name_check.click()

            by_number_check = self.driver.find_element(By.ID, "mainForm_byNumber")
            self.assertTrue(by_number_check.is_displayed(), msg="By Number Check box is not displayed")
            if not by_number_check.is_selected():
                by_number_check.click()
            # Cash Register
            enable_shift_open = self.driver.find_element(By.ID, "mainForm_showTillOpening")
            self.assertTrue(enable_shift_open.is_displayed(), msg="Enable Shift Open Check box is not displayed")
            if not enable_shift_open.is_selected():
                enable_shift_open.click()

            enable_shift_close = self.driver.find_element(By.ID, "mainForm_shiftClose")
            self.assertTrue(enable_shift_close.is_displayed(), msg="Enable Shift Close Check box is not displayed")
            if not enable_shift_close.is_selected():
                enable_shift_close.click()

            allow_petty_cash = self.driver.find_element(By.ID, "mainForm_pettyCash")
            self.assertTrue(allow_petty_cash.is_displayed(), msg="Allow Petty Cash Check box is not displayed")
            if not allow_petty_cash.is_selected():
                allow_petty_cash.click()

            allow_cash_in = self.driver.find_element(By.ID, "mainForm_cashIn")
            self.assertTrue(allow_cash_in.is_displayed(), msg="Allow Cash In Check box is not displayed")
            if not allow_cash_in.is_selected():
                allow_cash_in.click()

            allow_cash_out = self.driver.find_element(By.ID, "mainForm_cashOut")
            self.assertTrue(allow_cash_out.is_displayed(), msg="Allow Cash Out Check box is not displayed")
            if not allow_cash_out.is_selected():
                allow_cash_out.click()
            # POS
            allow_return_refund = self.driver.find_element(By.ID, "mainForm_allowReturnRefund")
            self.assertTrue(allow_return_refund.is_displayed(), msg="Allow Return and Refund Check box is not displayed")
            if not allow_return_refund.is_selected():
                allow_return_refund.click()

            allow_bill_parking = self.driver.find_element(By.ID, "mainForm_allowBillParking")
            self.assertTrue(allow_bill_parking.is_displayed(),
                            msg="Allow Bill Parking Check box is not displayed")
            if not allow_bill_parking.is_selected():
                allow_bill_parking.click()

            show_sales_return = self.driver.find_element(By.ID, "mainForm_showSalesReturn")
            self.assertTrue(show_sales_return.is_displayed(),
                            msg="Show Sales Return Check box is not displayed")
            if not show_sales_return.is_selected():
                show_sales_return.click()

            allow_return_exchange = self.driver.find_element(By.ID, "mainForm_showSalesReturn")
            self.assertTrue(allow_return_exchange.is_displayed(),
                            msg="Allow Return Exchange Check box is not displayed")
            if not allow_return_exchange.is_selected():
                allow_return_exchange.click()

            show_product_images = self.driver.find_element(By.ID, "mainForm_showImage")
            self.assertTrue(show_product_images.is_displayed(),
                            msg="Show Product Images Check box is not displayed")
            if not show_product_images.is_selected():
                show_product_images.click()
            # Sale Type
            cash_and_carry = self.driver.find_element(By.ID, "mainForm_cashCarry")
            self.assertTrue(cash_and_carry.is_displayed(),
                            msg="Cash and Carry Check box is not displayed")
            if not cash_and_carry.is_selected():
                cash_and_carry.click()

            save_button = self.driver.find_element(By.XPATH, "//span[text()='Save']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if enable_cash_check:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")