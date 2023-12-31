from CommonImportsPkg.common_imports import *
from login import Login


class AddImageLibraryTest(unittest.TestCase):
    def __init__(self, methodName='test_add_image_library', data=None):
        super(AddImageLibraryTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_add_image_library(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addImageLibrary']['username']
            # password = self.data['test_addImageLibrary']['password']
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
            # # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
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

            sidebar_menu_image_library = self.driver.find_element(By.XPATH,
                                                                  "//span[text()='Image Library']")
            self.assertTrue(sidebar_menu_image_library.is_displayed(),
                            msg="Image Library menu is not displayed.")
            sidebar_menu_image_library.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            image_name = self.data["test_add_image_library"]["Image"]
            input_image_name = self.driver.find_element(By.ID, "")
            self.assertTrue(input_image_name.is_displayed(), msg="Image Name input box is not displayed.")
            input_image_name.send_keys(image_name)
            time.sleep(5)

            description = self.data["test_add_image_library"]["Description"]
            input_description = self.driver.find_element(By.ID, "headerTab_9D891ED6164E4CEDBEA4B3A8C078FFD6")
            self.assertTrue(input_description.is_displayed(), msg="Description input box is not displayed.")
            input_description.send_keys(description)
            time.sleep(5)

            image_group = self.data["test_add_image_library"]["Image_Group"]
            input_image_group = self.driver.find_element(By.ID, "headerTab_E7E96A631EE44F3FB601A462F70B2AD3")
            self.assertTrue(input_image_group.is_displayed(), msg="Image Group Combo box is not displayed.")
            input_image_group.send_keys(image_group)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_image_name and input_description and input_image_group is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
