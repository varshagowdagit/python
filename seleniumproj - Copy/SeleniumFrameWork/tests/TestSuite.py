# 1. Import the files
import unittest
from SeleniumFrameWork.tests.test_login import LoginTest
from SeleniumFrameWork.tests.test_scrollPage import AddCartTest  #scrolling
from SeleniumFrameWork.tests.test_filter import FilterDropdownTest
from SeleniumFrameWork.tests.test_addCart import CartTest
from SeleniumFrameWork.tests.test_cartpage import CartPageTest
from SeleniumFrameWork.tests.test_checkout import CheckOut
from SeleniumFrameWork.tests.test_burgermenu import BurgerMenuTest



# 2. Create the object of the class using unitTest
a = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
b = unittest.TestLoader().loadTestsFromTestCase(AddCartTest)
c = unittest.TestLoader().loadTestsFromTestCase(FilterDropdownTest)
d = unittest.TestLoader().loadTestsFromTestCase(CartTest)
e = unittest.TestLoader().loadTestsFromTestCase(CartPageTest)
f = unittest.TestLoader().loadTestsFromTestCase(CheckOut)
g= unittest.TestLoader().loadTestsFromTestCase(BurgerMenuTest)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([a,b,c,d,e,f,g])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)


