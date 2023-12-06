from CommonImportsPkg.common_imports import *
from Test_LoginSignupPkg.TC_LoginTest import LoginTest
from Test_LoginSignupPkg.TC_SignUpTest import SignUpTest
from Test_POSFunctionalPkg.TC_PointOfSaleTest import PointOfSaleTest
from Test_StoreAdminFunctionalPkg.TC_AddBrandTest import AddBrandTest

# Get all Tests from TC_LoginTest, TC_SignUpTest, and so on
# logintest_suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
# signuptest_suite = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
pointofsaletest_suite = unittest.TestLoader().loadTestsFromTestCase(PointOfSaleTest)
# addbrand_suite = unittest.TestLoader().loadTestsFromTestCase(AddBrandTest)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(Test_SignUp)

# Creating TestSuites
# sanityTestSuite = unittest.TestSuite([logintest_suite, signuptest_suite]) # Sanity Test Suite
# functionalTestSuite = unittest.TestSuite([pointofsaletest_suite, addbrand_suite])
functionalTestSuite = unittest.TestSuite([pointofsaletest_suite])
# unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)
unittest.TextTestRunner(verbosity=2).run(functionalTestSuite)
