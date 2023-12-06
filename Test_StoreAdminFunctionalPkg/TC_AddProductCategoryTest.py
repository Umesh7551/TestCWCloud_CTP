from CommonImportsPkg.common_imports import *

class AddProductCategoryTest(unittest.TestCase):
    def __init__(self, methodName='test_addProductCategory', data=None):
        super(AddProductCategoryTest, self).__init__(methodName)
        self.data = data

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_addProductCategory(self):
        if self.data:
            self.driver.maximize_window()
            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(10)
            username = self.data['test_addProductCategory']['username']
            password = self.data['test_addProductCategory']['password']
            # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
            username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
            self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
            username_input.send_keys(username)
            time.sleep(5)

            # Step 5: Enter password in the password input box
            password_input = self.driver.find_element(By.XPATH,
                                                      "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
            self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
            password_input.send_keys(password)
            time.sleep(5)

            # Step 6: Click on the login button
            login_button = self.driver.find_element(By.XPATH,
                                                    "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
            self.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
            login_button.click()
            time.sleep(10)
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

            sidebar_menu_product_category = self.driver.find_element(By.XPATH, "//span[text()='Product Category']")
            self.assertTrue(sidebar_menu_product_category.is_displayed(),
                            msg="Product Category menu is not displayed.")
            sidebar_menu_product_category.click()
            time.sleep(5)

            # Add New Button
            add_new_button = self.driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            category_code = self.data["test_addProductCategory"]["Category Code"]
            input_category_code = self.driver.find_element(By.ID, "headerTab_DCDD6A1D18CD4FF29A65AD6CB6626080")
            self.assertTrue(input_category_code.is_displayed(), msg="Category code Input box is not displayed.")
            input_category_code.send_keys(category_code)
            time.sleep(5)

            category_name = self.data["test_addProductCategory"]["Category Name"]
            input_category_name = self.driver.find_element(By.ID, "headerTab_09862BBB54134EA88CD96A1120BA7470")
            self.assertTrue(input_category_name.is_displayed(), msg="Category Name input box is not displayed.")
            input_category_name.send_keys(category_name)
            time.sleep(5)

            parent_category = self.data["test_addProductCategory"]["Parent Category"]
            input_parent_category = self.driver.find_element(By.ID, "headerTab_864BED62888C409B91883A2C59AE6EE3")
            self.assertTrue(input_parent_category.is_displayed(), msg="Parent Category input is not displayed.")
            input_parent_category.send_keys(parent_category)
            time.sleep(5)

            category_description = self.data["test_addProductCategory"]["Category Description"]
            input_category_description = self.driver.find_element(By.ID,
                                                                  "headerTab_1F2F4DC8A00343CC9791790D57E1B087")
            self.assertTrue(input_category_description.is_displayed(),
                            msg="Category Description input box is not displayed.")
            input_category_description.send_keys(category_description)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not displayed")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if category_code and category_name is not None:
                save_button.click()
                time.sleep(5)
            else:
                cancel_button.click()
                time.sleep(5)
            flash("You have passed Add Product Category Test case.", "success")
        else:
            flash("You have not passed Add Product Category Test case.", "error")