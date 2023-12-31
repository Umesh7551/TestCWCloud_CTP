from CommonImportsPkg.common_imports import *
from login import Login


class AddProductCatalogueTest(unittest.TestCase):
    def __init__(self, methodName='test_add_product_catalogue', data=None):
        super(AddProductCatalogueTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_add_product_catalogue(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addProductCatalogue']['username']
            # password = self.data['test_addProductCatalogue']['password']
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

            menu_products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            self.assertTrue(menu_products.is_displayed(), msg="Products Menu is not Displayed")
            menu_products.click()
            time.sleep(5)

            sidebar_menu_product_catalogue = self.driver.find_element(By.XPATH,
                                                                      "//span[text()='Product Catalogue']")
            self.assertTrue(sidebar_menu_product_catalogue.is_displayed(),
                            msg="Product Catalogue menu is not displayed.")
            sidebar_menu_product_catalogue.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            product_catalogue = self.data['test_add_product_catalogue']['Product_Catalogue_Name']
            input_product_catalogue = self.driver.find_element(By.ID, "headerTab_02C771DA4EAC43B1B4DFA1B26CDB05A7")
            self.assertTrue(input_product_catalogue.is_displayed(),
                            msg="Product Catalogue input box is not displayed.")
            input_product_catalogue.send_keys(product_catalogue)
            time.sleep(5)

            active_checkbox = self.driver.find_element(By.ID, "headerTab_339E009F5745408FB2ADF8C83E05373D")
            self.assertTrue(active_checkbox.is_selected(), msg="Active Check box is not Selected.")
            if active_checkbox.is_selected():
                pass
            else:
                # If it's not selected, select the checkbox
                active_checkbox.click()

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_product_catalogue is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
