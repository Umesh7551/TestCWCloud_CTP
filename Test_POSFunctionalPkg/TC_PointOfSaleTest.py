import time

from CommonImportsPkg.common_imports import *

class PointOfSaleTest(unittest.TestCase):
    def __init__(self, methodName='test_point_of_sale', data=None):
        super(PointOfSaleTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
        # print(self.data)
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_point_of_sale(self):
        # Access the JSON data within your test method
        if self.data:
            self.driver.maximize_window()
            # Step 1: Open the URL
            # self.driver.get("https://test.cwcloud.in/")
            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            self.assertEqual(self.driver.current_url, "https://test-auth.cwcloud.in:8412/sign-in")
            # Step 2: Click on the "Login" link text
            # login_link = self.driver.find_element(By.LINK_TEXT, "Login")
            # login_link = self.driver.find_element(By.XPATH, "//span[@class='ff-Inter text-xs text-darkBlack mr-4 xl:mr-10 hover:opacity-70 transition-all duration-200 ease-in hidden sm:block']")
            # login_link.click()
            # self.assertEqual(self.driver.current_url, "https://test-auth.cwcloud.in:8412/sign-in")
            # Step 3: Switch to the new tab or window
            # Get the current window handle (main window)
            # main_window = self.driver.current_window_handle
            #
            # # Get all window handles (including the main window)
            # all_handles = self.driver.window_handles
            #
            # # Switch to the new window
            # for handle in all_handles:
            #     if handle != main_window:
            #         self.driver.switch_to.window(handle)
            #         break

            # Now you're in the new tab/window.
            time.sleep(10)
            username = self.data['test_point_of_sale']['username']
            # print(username)
            password = self.data['test_point_of_sale']['password']
            # Step 4: Enter username in the username input box

            # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
            # username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
            username_input = self.driver.find_element(By.ID, "username")
            self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
            username_input.send_keys(username)

            # Step 5: Enter password in the password input box
            # password_input = self.driver.find_element(By.XPATH, "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
            password_input = self.driver.find_element(By.ID, "password")
            self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
            password_input.send_keys(password)

            # Step 6: Click on the login button
            # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
            login_button = self.driver.find_element(By.ID, "login")
            self.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
            login_button.click()
            time.sleep(10)
            # self.assertEqual(self.driver.current_url, "https://test-app.cwcloud.in:8412/my-apps")

            # Step 6: Select POS
            # pos = self.driver.find_element(By.XPATH, "//article[@class='bg-white mb-2 sm:mb-0 md:w-[180px] lg:w-[180px] sm:w-[200px] xs:w-full rounded-[12px] px-3 py-3 mr-2 sm:mr-4 justify-between relative'][1]")
            pos = self.driver.find_element(By.XPATH, "//h4[text()='POS']")
            self.assertTrue(pos.is_displayed(), msg="POS Article is not displayed.")
            # pos = self.driver.find_element(By.XPATH, "//h4[@class='text-[#101828] font-semibold ff-inter text-[18px]']")
            pos.click()
            time.sleep(10)
            # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/")
            # self.driver.implicitly_wait(5)

            # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/")
            # # Loop through the handles to find the handle of the third window
            # for handle1 in all_handles:
            #     if handle1 != main_window and handle1 != handle1:
            #         self.driver.switch_to.window(handle1)
            #         break

            # Get the current window handle (main window)
            main_window = self.driver.current_window_handle

            # Get all window handles (including the main window)
            all_handles = self.driver.window_handles

            # Switch to the new window
            for handle in all_handles:
                if handle != main_window:
                    self.driver.switch_to.window(handle)
                    break
            # Click on Till
            time.sleep(15)

            till = self.driver.find_element(By.XPATH, "//div[@class='ant-card-body']")
            till.click()
            # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/open-till-component")
            # insert amount into Amount Input box
            json_amount = self.data['test_point_of_sale']['amount']
            # amount = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
            # amount.send_keys(json_amount)
            # time.sleep(5)
            # insert note into note input box
            json_note = self.data['test_point_of_sale']['note']
            # note = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
            # note.send_keys(json_note)
            # time.sleep(5)
            # Click open till button
            # open_till_button = self.driver.find_element(By.XPATH, "//button[@id='step3']")
            # open_till_button.click()

            # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/pos")
            # logging.info("Login Test Passed")

            # pos_search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Search for products by code/name']")
            # pos_search_input.send_keys("Blue Water Bottle")

            wait = WebDriverWait(self.driver, 20)
            search_customer = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter customer number/name']")))
            # Search Customer Name or Number
            # search_customer = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter customer number/name']")
            # search_customer = self.driver.find_element(By.XPATH, "//input[@class='ant-input']")
            # search_customer.click()
            # if search_customer.is_displayed():
            #     json_customer_search = self.data['test_login']['customer_search']
            #     # popup_search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            #     popup_search = self.driver.find_element(By.XPATH, "//input[@class='ant-input ant-input-lg']")
            #     popup_search.send_keys(json_customer_search)
            #     # print(popup_search.text)
            #     popup_search.send_keys(Keys.RETURN)
            #     if popup_search.is_displayed():
            #         # Select searched customer
            #         self.driver.find_element(By.XPATH, "//div[@class='ant-col ant-col-17 ant-col-offset-1']").click()
            #     else:
            #         # Add New Customer
            #         self.driver.find_element(By.XPATH, "//div[@class='ant-row ant-row-center']").click()
            #         time.sleep(5)
            #         #First Name
            #         json_first_name = self.data['test_point_of_sale']['firstname']
            #         first_name = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_name']")
            #         first_name.clear()
            #         first_name.send_keys(json_first_name)
            #
            #         # Last Name
            #         json_last_name = self.data['test_point_of_sale']['lastname']
            #         last_name = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_lastName']")
            #         last_name.send_keys(json_last_name)
            #
            #         #Email
            #         json_email = self.data['test_point_of_sale']['email']
            #         email = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_email']")
            #         email.send_keys(json_email)
            #
            #         # Contact Number
            #         json_phone = self.data['test_point_of_sale']['phone']
            #         phone = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_mobile']")
            #         phone.send_keys(json_phone)
            #
            #         # Pincode
            #         json_pincode = self.data['test_point_of_sale']['pincode']
            #         pincode = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_pincode']")
            #         pincode.send_keys(json_pincode)
            #
            #         # Create New Customer Button
            #         create_new_customer_button = self.driver.find_element(By.XPATH, "//button[@class='ant-btn customerDetailsSubmitBtnBtn']")
            #         create_new_customer_button.click()

            # Wait for the input element to be present and visible
            wait = WebDriverWait(self.driver, 20)
            pos_search_input = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Search for products by code/name']")))

            # Now you can interact with the input element
            json_pos_search_input = self.data['test_point_of_sale']['pos_search_input']
            pos_search_input.send_keys(json_pos_search_input)
            # Simulate pressing the Enter keyole
            pos_search_input.send_keys(Keys.RETURN)
            time.sleep(10)

            # Increase and Decrease Quantity buttons are showing on double-clicking

            # increase_qty = self.driver.find_element(By.XPATH, "//span[@title='Increase Qty']")
            # increase_qty = self.driver.find_element(By.XPATH, "//span[@class='anticon anticon-plus']")
            # Perform a double click
            # action_chains = ActionChains(self.driver)
            # action_chains.double_click(increase_qty).perform()
            # time.sleep(10)
            #
            # decrease_qty = self.driver.find_element(By.XPATH, "//span[@class='anticon anticon-minus']")
            # decrease_qty.click()

            # Search Customer Name or Number
            # search_customer = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter customer number/name']")
            # search_customer.click()
            #
            # popup_search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            # popup_search.send_keys("Umesh")
            # popup_search.send_keys(Keys.RETURN)

            # Wait for some time for the search result to appear
            # time.sleep(10)

            pay_button = self.driver.find_element(By.XPATH, "//button[@id='step11']")
            pay_button.click()
            # self.driver.implicitly_wait(10)
            time.sleep(10)
            # Cash Button
            cash_button = self.driver.find_element(By.XPATH, "//button[text()='Cash']")
            cash_button.click()
            if cash_button.is_enabled():
                pass
            else:
                # Card Button
                card_button = self.driver.find_element(By.XPATH, "//button[text()='Card']")
                card_button.click()

            # Add Payment Button
            add_payment = self.driver.find_element(By.XPATH, "//span[text()='Add Payment']")
            add_payment.click()

            # Complete Order Button
            # complete_order = self.driver.find_element(By.XPATH, "//span[text()='Complete Order']")
            # complete_order.click()

            # Handle New Chrome Window for print Reciept
            new_window_handle = None

            for handle in all_handles:
                if handle != main_window:
                    new_window_handle = handle
                    break

            if new_window_handle:
                self.driver.switch_to.window(new_window_handle)
            time.sleep(10)
            # save_button = self.driver.find_element(By.XPATH, "//cr-button[text()='Save']")
            # save_button.click()

            self.driver.switch_to.window(main_window)
            # messagebox.showinfo("Success", "You have passed Point of Sale test case. ")
            flash(f"You have passed { self.test_name.upper() } Test case.", "success")
        else:
            flash("You have not passed { self.test_name.upper() } Test case.", "error")
            # print("No test data provided")
            # messagebox.showerror("Error", "You have not passed Point of Sale test case. ")
