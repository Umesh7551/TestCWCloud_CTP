
from CommonImportsPkg.common_imports import *


class Login:

    def login(self, username, password):
        self.driver.maximize_window()
        self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
        time.sleep(5)

        username_input = self.find_element_with_wait(By.XPATH, "//input[@placeholder='Enter Email']")
        self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
        username_input.send_keys(username)
        time.sleep(5)

        password_input = self.find_element_with_wait(By.XPATH, "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
        self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
        password_input.send_keys(password)
        time.sleep(5)

        login_button = self.find_element_with_wait(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
        self.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
        login_button.click()
        time.sleep(10)

    def find_element_with_wait(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )
