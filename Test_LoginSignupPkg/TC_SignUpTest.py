from CommonImportsPkg.common_imports import *



class SignUpTest(unittest.TestCase):
    def __init__(self, methodName='test_signup', data=None):
        super(SignUpTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_signup(self):
        if self.data:
            self.driver.maximize_window()
            self.driver.get("https://test.cwcloud.in/")
            time.sleep(5)


