from CommonImportsPkg.common_imports import *

class SalesByProductCategoryTest(unittest.TestCase):
    def __init__(self, methodName='test_Sales_by_Product_Category', data=None):
        super(SalesByProductCategoryTest, self).__init__(methodName)
        self.data = data

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_Sales_by_Product_Category(self):
        if self.data:
            self.driver.maximize_window()
            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_Sales_by_Product_Category']['username']
            password = self.data['test_Sales_by_Product_Category']['password']
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

            menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
            self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
            menu_reports.click()
            time.sleep(5)

            sidebar_menu_sales_by_product_category = self.driver.find_element(By.XPATH,
                                                                              "//span[text()='Sales by Product Category Report']")
            self.assertTrue(sidebar_menu_sales_by_product_category.is_displayed(),
                            msg="Sales By Product Category menu is not displayed.")
            sidebar_menu_sales_by_product_category.click()
            time.sleep(5)

            store = self.data['test_Sales_by_Product_Report']['Store']
            input_store = self.driver.find_element(By.ID, "cs_bunit_id")
            self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
            input_store.send_keys(store)
            time.sleep(5)

            product_category = self.data['test_Sales_by_Product_Report']['Product_Category']
            input_product_category = self.driver.find_element(By.ID, "m_product_category_id")
            self.assertTrue(input_product_category.is_displayed(), msg="Product Category input is not displayed.")
            input_product_category.send_keys(product_category)
            time.sleep(5)

            run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
            self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
            if input_store and input_product_category is not None:
                run_button.click()

            flash("You have passed Test case.", "success")
        else:
            flash("You have not passed Test case.", "error")