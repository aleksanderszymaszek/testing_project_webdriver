__author__ = 'aleksander.szymaszek'

import unittest
import sys
import os

sys.path.append('\\'.join(os.path.dirname(os.path.abspath(__file__)).split("\\")[:-1]))

from test_case_driver import SeleniumTestCasesWebdriver



def suite():



    test_suite = unittest.TestLoader().loadTestsFromTestCase(SeleniumTestCasesWebdriver)



    #===========================================================================

    #                            Test cases

    #===========================================================================

    #test_suite.addTest(SeleniumTestCasesWebdriver('test_three'))



    return test_suite



if __name__ == '__main__':

    result=unittest.TextTestRunner(verbosity=2).run(suite())

    sys.exit(not result.wasSuccessful())