from CommonImportsPkg.common_imports import *

class AddSupplierCategoryTest(unittest.TestCase):
    def __init__(self, methodName='test_addSupplier_Category', data=None):
        super(AddSupplierCategoryTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_addSupplier_Category(self):
        if self.data:
            self.driver.maximize_window()

            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_addSupplier_Category']['username']
            password = self.data['test_addSupplier_Category']['password']
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

            menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
            self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
            menu_settings.click()
            time.sleep(5)

            sidebar_menu_supplier_category = self.driver.find_element(By.XPATH,
                                                                      "//span[text()='Supplier Category']")
            self.assertTrue(sidebar_menu_supplier_category.is_displayed(),
                            msg="Supplier Category menu is not displayed.")
            sidebar_menu_supplier_category.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            business_unit = self.data['test_addSupplier_Category']['Business_Unit']
            input_business_unit = self.driver.find_element(By.ID, "headerTab_92EB5F77E8AB463988C4210330135C5A")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            code = self.data['test_addSupplier_Category']['Code']
            input_code = self.driver.find_element(By.ID, "headerTab_BDB41292781044BC8D385C7F11249461")
            self.assertTrue(input_code.is_displayed(), msg="Code input is not displayed.")
            input_code.send_keys(code)
            time.sleep(5)

            category_name = self.data['test_addSupplier_Category']['Category_Name']
            input_category_name = self.driver.find_element(By.ID, "headerTab_AA15BE6AB52C43AAAE5A12ED46012E5D")
            self.assertTrue(input_category_name.is_displayed(), msg="Category Name input is not displayed.")
            input_category_name.send_keys(category_name)
            time.sleep(5)

            default_check = self.driver.find_element(By.ID, "headerTab_31119DADA57D4D68ABA36936671675D0")
            if not default_check.is_selected():
                default_check.click()

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_business_unit and input_code and input_category_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")