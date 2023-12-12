from CommonImportsPkg.common_imports import *
from login import Login


class AddProductsTest(unittest.TestCase):
    def __init__(self, methodName='test_addProducts', data=None):
        super(AddProductsTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_addProducts(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addProducts']['username']
            # password = self.data['test_addProducts']['password']
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
            # Step 6: Select POS
            # pos = self.driver.find_element(By.XPATH, "//article[@class='bg-white mb-2 sm:mb-0 md:w-[180px] lg:w-[180px] sm:w-[200px] xs:w-full rounded-[12px] px-3 py-3 mr-2 sm:mr-4 justify-between relative'][1]")
            store_admin = self.driver.find_element(By.XPATH, "//h4[text()='Store Admin']")
            # Check if the element is displayed
            self.assertTrue(store_admin.is_displayed(), msg="Store Admin is not displayed")
            store_admin.click()
            time.sleep(10)

            menu_products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            self.assertTrue(menu_products.is_displayed(), msg="Products Menu is not Displayed")
            menu_products.click()

            sidebar_menu_product = self.driver.find_element(By.XPATH, "//span[text()='Product']")
            self.assertTrue(sidebar_menu_product.is_displayed(), msg="Product menu is not displayed.")
            sidebar_menu_product.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New Button is not displayed")
            add_new_button.click()
            time.sleep(10)

            product_info = self.data["test_addProducts"]["product_info"]
            product_name = product_info["Product Name"]
            product_category = product_info["Product Category"]
            uom = product_info["UOM"]
            tax_category = product_info["Tax Category"]
            sales_price = product_info["Sales Price"]
            list_price = product_info["List Price"]
            purchase_price = product_info["Purchase Price"]
            upc = product_info["UPC"]
            product_description = product_info["Product Description"]
            image_url = product_info["Image URL"]
            product_catalogue = product_info["Product Catalogue"]

            input_product_name = self.driver.find_element(By.ID, "headerTab_05DF4D54F56544E7BB875B7CFB935C8C")
            self.assertTrue(input_product_name.is_displayed(), msg="Product Name Input box is not displayed")
            input_product_name.clear()
            input_product_name.send_keys(product_name)
            time.sleep(5)

            input_product_category = self.driver.find_element(By.ID, "headerTab_C836ADF14C7046CAB505735A9C75A9A2")
            self.assertTrue(input_product_category.is_displayed(), msg="Product Category is not displayed.")
            input_product_category.clear()
            input_product_category.send_keys(product_category)
            time.sleep(5)

            input_uom = self.driver.find_element(By.ID, "headerTab_311BAEAB192E4CED9C6375C24E5FCB4A")
            self.assertTrue(input_uom.is_displayed(), msg="UOM is not displayed.")
            input_uom.clear()
            input_uom.send_keys(uom)
            time.sleep(5)

            input_tax_category = self.driver.find_element(By.ID, "headerTab_C4AE5CADA4AA46B583BE475719287EAF")
            self.assertTrue(input_tax_category.is_displayed(), msg="Tax Category is not displayed.")
            input_tax_category.send_keys(tax_category)
            time.sleep(5)

            input_sales_price = self.driver.find_element(By.ID, "headerTab_9401293BAC5A432F81EC52E65AEAC96E")
            self.assertTrue(input_sales_price.is_displayed(), msg="Sales Price is not displayed.")
            input_sales_price.clear()
            input_sales_price.send_keys(sales_price)
            time.sleep(5)

            input_list_price = self.driver.find_element(By.ID, "headerTab_1026DF342BBD4DA0A678C2BAC4AE2600")
            self.assertTrue(input_list_price.is_displayed(), msg="List Price is not Displayed.")
            input_list_price.send_keys(list_price)
            time.sleep(5)
            input_purchase_price = self.driver.find_element(By.ID, "headerTab_842952C5B7A94B01BE5B2B61D3EC7E36")
            self.assertTrue(input_purchase_price.is_displayed(), msg="Purchase Price is not displayed.")
            input_purchase_price.send_keys(purchase_price)
            time.sleep(5)

            input_upc = self.driver.find_element(By.ID, "headerTab_95761154135347DCBF37F158165AE03E")
            self.assertTrue(input_upc.is_displayed(), msg="UPC is not displayed.")
            input_upc.clear()
            input_upc.send_keys(upc)
            time.sleep(5)

            input_product_description = self.driver.find_element(By.ID,
                                                                 "headerTab_A367F6AC04954C6CA4076E72343253CB")
            self.assertTrue(input_product_description.is_displayed(), msg="Product Description is not displayed.")
            input_product_description.clear()
            input_product_description.send_keys(product_description)
            time.sleep(5)

            input_image_url = self.driver.find_element(By.XPATH, "//span[text()='Upload']")
            self.assertTrue(input_image_url.is_displayed(), msg="Image Upload is not displayed.")
            # input_image_url.clear()
            input_image_url.send_keys(image_url)
            time.sleep(5)

            input_product_catalogue = self.driver.find_element(By.ID, "headerTab_D3F455D32BCA4802816CC0CEFB89D64F")
            self.assertTrue(input_product_catalogue.is_displayed(), msg="Product Catalogue is not displayed.")
            input_product_catalogue.clear()
            input_product_catalogue.send_keys(product_catalogue)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel button is not displayed.")
            if input_product_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
