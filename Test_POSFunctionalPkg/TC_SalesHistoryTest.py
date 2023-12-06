from CommonImportsPkg.common_imports import *

class SalesHistoryTest(unittest.TestCase):
    def __init__(self, methodName='test_salesHistory', data=None):
        super(SalesHistoryTest, self).__init__(methodName)
        self.data = data

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_salesHistory(self):
        self.driver.maximize_window()

        self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
        time.sleep(30)
        username = self.data['test_salesHistory']['username']
        password = self.data['test_salesHistory']['password']
        # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
        # username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
        # username_input.send_keys(username)

        # Step 5: Enter password in the password input box
        # password_input = self.driver.find_element(By.XPATH, "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
        # password_input.send_keys(password)

        # Step 6: Click on the login button
        # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
        # login_button.click()
        # Step 6: Select POS
        # pos = self.driver.find_element(By.XPATH, "//article[@class='bg-white mb-2 sm:mb-0 md:w-[180px] lg:w-[180px] sm:w-[200px] xs:w-full rounded-[12px] px-3 py-3 mr-2 sm:mr-4 justify-between relative'][1]")
        pos = self.driver.find_element(By.XPATH, "//h4[text()='POS']")
        if pos.is_displayed():
            pos.click()
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
        time.sleep(20)
        # till = self.driver.find_element(By.XPATH, "//div[@class='ant-card ant-card-bordered']")
        # till.click()
        # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/open-till-component")
        # insert amount into Amount Input box
        # json_amount = self.data['test_salesHistory']['amount']
        # amount = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
        # amount.send_keys(json_amount)

        # insert note into note input box
        # json_note = self.data['test_salesHistory']['note']
        # note = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
        # note.send_keys(json_note)

        # Click open till button
        # open_till_button = self.driver.find_element(By.XPATH, "//button[@id='step3']")
        # open_till_button.click()

        time.sleep(10)
        # menu_salesHistory = self.driver.find_element(By.XPATH, "//span[text()='Sales History']")
        # if menu_salesHistory.is_displayed():
        #     menu_salesHistory.click()
        #     time.sleep(5)
        #  Search Customer Name
        json_search_customer = self.data["test_salesHistory"]["search_customer"]
        search_customer = self.driver.find_element(By.XPATH, "//input[@class='ant-input ant-input-lg']")
        search_customer.send_keys(json_search_customer)
        search_customer.send_keys(Keys.RETURN)
        time.sleep(5)
        # Select Date
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        formatted_date = current_date.strftime("%Y-%m-%d")
        datepicker = self.driver.find_element(By.XPATH, "//input[@placeholder='Choose date range']")
        datepicker.send_keys(formatted_date)
        # Search Document Number
        json_document_no = self.data["test_salesHistory"]["document_no"]
        document_no = self.driver.find_element(By.XPATH,
                                               "//input[@class='ant-input ant-input-lg salesHistory-doc-input']")
        document_no.send_keys(json_document_no)
        # Select Right Arrow

        # right_arrow = self.driver.find_element(By.XPATH, "//span[@class='anticon anticon-right']")
        right_arrow = self.driver.find_element(By.XPATH, "//span[@role='img']")
        no_data = self.driver.find_element(By.XPATH, "//div[@class='ant-empty-description']").text
        if right_arrow.is_displayed():
            right_arrow.click()
            time.sleep(5)
            print_reciept = self.driver.find_element(By.XPATH, "//p[text()='Print receipt']")
            sales_return = self.driver.find_element(By.XPATH, "//p[text()='Sales Return']")

            if print_reciept.is_displayed():
                print_reciept.click()
            else:
                pass

            if sales_return.is_displayed():
                sales_return.click()
                remove_button = self.driver.find_element(By.XPATH, "//span[text()='Remove']")
                return_button = self.driver.find_element(By.XPATH,
                                                         "//button[@class='ant-btn focusDashboardCard']")
                if remove_button.is_displayed() and return_button.is_displayed():
                    time.sleep(5)
                    remove_button.click()

                else:
                    return_button.click()

            else:
                pass

        else:
            if no_data == "No Data":
                # Go to Point of Sale Page
                menu_point_of_sale = self.driver.find_element(By.XPATH, "//span[text()='Point of Sale']")
                menu_point_of_sale.click()