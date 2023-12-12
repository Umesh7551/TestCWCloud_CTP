from CommonImportsPkg.common_imports import *

class AddPOSOrdersTest(unittest.TestCase):
    def __init__(self, methodName='test_posOrders', data=None):
        super(AddPOSOrdersTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)
    def tearDown(self):
        self.driver.close()

    def test_posOrders(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_posOrders']['username']
            # password = self.data['test_posOrders']['password']
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

            menu_sales = self.driver.find_element(By.XPATH, "//span[text()='Sales']")
            self.assertTrue(menu_sales.is_displayed(), msg="Sales Menu is not Displayed")
            menu_sales.click()
            time.sleep(5)

            sidebar_menu_pos_orders = self.driver.find_element(By.XPATH,
                                                               "//span[text()='POS Orders']")
            self.assertTrue(sidebar_menu_pos_orders.is_displayed(),
                            msg="Pos Orders menu is not displayed.")
            sidebar_menu_pos_orders.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            store = self.data["test_posOrders"]["Store"]
            input_store = self.driver.find_element(By.ID, "headerTab_4364D3A8153E4B5A96EFBAAFA884A257")
            self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
            input_store.send_keys(store)
            time.sleep(5)

            sale_type = self.data["test_posOrders"]["Sale Type"]
            input_sale_type = self.driver.find_element(By.ID, "headerTab_4870F8FD52FD491E91D23A51E47C835D")
            self.assertTrue(input_sale_type.is_displayed(), msg="Sale Type input is not displayed.")
            input_sale_type.send_keys(sale_type)
            time.sleep(5)

            document_type = self.data["test_posOrders"]["Document Type"]
            input_document_type = self.driver.find_element(By.ID, "headerTab_F099D992F66C4328840B015336C388D9")
            self.assertTrue(input_document_type.is_displayed(), msg="Document Type input is not displayed.")
            input_document_type.send_keys(document_type)
            time.sleep(5)

            document_no = self.data["test_posOrders"]["Document No"]
            input_document_no = self.driver.find_element(By.ID, "headerTab_514DB285761544BFB842D31AD90490D5")
            self.assertTrue(input_document_no.is_displayed(), msg="Document Number input is not displayed")
            input_document_no.send_keys(document_no)
            time.sleep(5)

            order_date = self.data["test_posOrders"]["Order Date"]
            input_order_date = self.driver.find_element(By.ID, "headerTab_A999CD069E704FB889A7348DEEC20AE2")
            self.assertTrue(input_order_date.is_displayed(), msg="Order date input is not displayed.")
            input_sale_type.send_keys(order_date)
            time.sleep(5)

            order_time = self.data["test_posOrders"]["Order Time"]
            input_order_time = self.driver.find_element(By.ID, "headerTab_474B0303FE73478194D0FA96E9487BDF")
            self.assertTrue(input_order_time.is_displayed(), msg="Order Time input is not displayed.")
            input_order_time.send_keys(order_time)
            time.sleep(5)

            b2c_customer = self.data["test_posOrders"]["B2C Customer"]
            input_b2c_customer = self.driver.find_element(By.ID, "headerTab_C1889B9E3ECB4A6ABE088526465CBB28")
            self.assertTrue(input_b2c_customer.is_displayed(), msg="B2C Customer input is not displayed.")
            input_b2c_customer.send_keys(b2c_customer)
            time.sleep(5)

            price_list = self.data["test_posOrders"]["Price_List"]
            input_price_list = self.driver.find_element(By.ID, "headerTab_E01845685600402097E7D7E582706F1A")
            self.assertTrue(input_price_list.is_displayed(), msg="Price List input is not displayed.")
            input_price_list.send_keys(price_list)
            time.sleep(5)

            payment_method = self.data["test_posOrders"]["Payment Method"]
            input_payment_method = self.driver.find_element(By.ID, "headerTab_578D3AF8FDB6424EA807B1375619ADF8")
            self.assertTrue(input_payment_method.is_displayed(), msg="Payment Method input is not displayed.")
            input_payment_method.send_keys(payment_method)
            time.sleep(5)

            sales_rep = self.data["test_posOrders"]["Sales Rep"]
            input_sales_rep = self.driver.find_element(By.ID, "headerTab_B22065C7EB1E4AFF8FFA6FA6EB3797DC")
            self.assertTrue(input_sales_rep.is_displayed(), msg="Sales Rep input is not displayed.")
            input_sales_rep.send_keys(sales_rep)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_store and input_document_type and input_document_no and input_order_date and input_price_list is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")