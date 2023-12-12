from CommonImportsPkg.common_imports import *
from login import Login


class AddBrandTest(unittest.TestCase):
    def __init__(self, methodName='test_addBrand', data=None):
        super(AddBrandTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_addBrand(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addBrand']['username']
            # password = self.data['test_addBrand']['password']
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
            time.sleep(5)

            menu_products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            self.assertTrue(menu_products.is_displayed(), msg="Products Menu is not Displayed")
            menu_products.click()
            time.sleep(5)

            sidebar_menu_brand = self.driver.find_element(By.XPATH,
                                                          "//span[text()='Brand']")
            self.assertTrue(sidebar_menu_brand.is_displayed(),
                            msg="Brand menu is not displayed.")
            sidebar_menu_brand.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            brand_name = self.data["test_addBrand"]["Brand Name"]
            input_brand_name = self.driver.find_element(By.ID, "headerTab_406034723F6E4DC4BC8352D364E3A188")
            self.assertTrue(input_brand_name.is_displayed(), msg="Brand Name input box is not displayed.")
            input_brand_name.send_keys(brand_name)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_brand_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
