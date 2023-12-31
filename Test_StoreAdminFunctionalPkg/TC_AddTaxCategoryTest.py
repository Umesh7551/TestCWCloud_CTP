from CommonImportsPkg.common_imports import *
from login import Login


class AddTaxCategoryTest(unittest.TestCase):
    def __init__(self, methodName='test_add_tax_category', data=None):
        super(AddTaxCategoryTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_add_tax_category(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addTax_Category']['username']
            # password = self.data['test_addTax_Category']['password']
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

            sidebar_menu_tax_category = self.driver.find_element(By.XPATH, "//span[text()='Tax Category']")
            self.assertTrue(sidebar_menu_tax_category.is_displayed(), msg="Tax Category menu is not displayed.")
            sidebar_menu_tax_category.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            business_unit = self.data['test_add_tax_category']['Business_Unit']
            input_business_unit = self.driver.find_element(By.ID, "headerTab_3D64DCD5949449A68576ACE794200D5D")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            name = self.data['test_add_tax_category']['Name']
            input_name = self.driver.find_element(By.ID, "headerTab_7DA02A5644AE424EB3B4CB308144CE27")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            description = self.data['test_add_tax_category']['Description']
            input_description = self.driver.find_element(By.ID, "headerTab_F724B12D741A4FF0A6B293808713658D")
            self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
            input_description.send_keys(description)
            time.sleep(5)

            intra_region_tax = self.data['test_add_tax_category']['Intra_Region_Tax']
            input_intra_region_tax = self.driver.find_element(By.ID, "headerTab_4AFDB8C5C1BE4A3DBFEBBAE45205AEF2")
            self.assertTrue(input_intra_region_tax.is_displayed(), msg="Intra Region Tax input is not displayed.")
            input_intra_region_tax.send_keys(intra_region_tax)
            time.sleep(5)

            inter_region_tax = self.data['test_add_tax_category']['Inter_Region_Tax']
            input_inter_region_tax = self.driver.find_element(By.ID, "headerTab_646A99E284794CC4A811921C16C24CEB")
            self.assertTrue(input_inter_region_tax.is_displayed(), msg="Inter Region Tax input is not displayed.")
            input_inter_region_tax.send_keys(inter_region_tax)
            time.sleep(5)

            is_default_check = self.driver.find_element(By.ID, "headerTab_81D0B599D6FF4A4A9EF97EF1B24DF1DF")
            if is_default_check.is_selected():
                pass
            else:
                is_default_check.click()

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_business_unit and input_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
