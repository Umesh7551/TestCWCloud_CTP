from CommonImportsPkg.common_imports import *

class AddTaxTest(unittest.TestCase):
    def __init__(self, methodName='test_addTax', data=None):
        super(AddTaxTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_addTax(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addTax']['username']
            # password = self.data['test_addTax']['password']
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

            menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
            self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
            menu_settings.click()
            time.sleep(5)

            sidebar_menu_tax = self.driver.find_element(By.XPATH, "//span[text()='Tax']")
            self.assertTrue(sidebar_menu_tax.is_displayed(), msg="Tax menu is not displayed.")
            sidebar_menu_tax.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            business_unit = self.data['test_addTax']['Business_Unit']
            input_business_unit = self.driver.find_element(By.ID, "headerTab_DFD3F62756804A85B45F107FA2BDA845")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            name = self.data['test_addTax']['Name']
            input_name = self.driver.find_element(By.ID, "headerTab_7DF2751B3FFC41ECAEFF6437499439A1")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            tax_category = self.data['test_addTax']['Tax_Category']
            input_tax_category = self.driver.find_element(By.ID, "headerTab_973974F051234486A457D13DCBC6F16C")
            self.assertTrue(input_tax_category.is_displayed(), msg="Tax Category input is not displayed.")
            input_tax_category.send_keys(tax_category)
            time.sleep(5)

            rate = self.data['test_addTax']['Rate']
            input_rate = self.driver.find_element(By.ID, "headerTab_B04D8168AAA44E1A98E79D7DBC7593BB")
            self.assertTrue(input_rate.is_displayed(), msg="Rate input is not displayed.")
            input_rate.send_keys(rate)
            time.sleep(5)

            parent_tax_rate = self.data['test_addTax']['Parent_Tax_Rate']
            input_parent_tax_rate = self.driver.find_element(By.ID, "headerTab_AB3C0217E29D46C0B724813E2B50D2E0")
            self.assertTrue(input_parent_tax_rate.is_displayed(), msg="Parent Tax Rate input is not displayed.")
            input_parent_tax_rate.send_keys(parent_tax_rate)
            time.sleep(5)

            description = self.data['test_addTax']['Description']
            input_description = self.driver.find_element(By.ID, "headerTab_5BE3F41C5F904E6298351B164B2D21C6")
            self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
            input_description.send_keys(description)
            time.sleep(5)

            is_default_check = self.driver.find_element(By.ID, "headerTab_B80E5787B5B548E48843C37E346D5CE3")
            if not is_default_check.is_selected():
                is_default_check.click()

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_business_unit and input_name and input_tax_category and input_rate is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
