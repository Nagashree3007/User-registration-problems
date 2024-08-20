'''

@Author: Nagashree C R
@Date: 2024-08-8-07
@Last Modified by: Nagashree C R
@Last Modified: 2024-08-07
@Title :User registration problems UC3-User need to enter a valid email test case.

'''

import unittest
from use_registration import check_name
from use_registration import check_mail

class TestCheckName(unittest.TestCase):
    def test_check_name_valid(self):
        self.assertEqual(check_name('John'), 1)
        self.assertEqual(check_name('Alice'), 1)
        self.assertEqual(check_name('Jo'), 0)
        self.assertEqual(check_name('john'), 0)
        self.assertEqual(check_name('al'), 0)
        self.assertEqual(check_name('aLice'), 0)
        
    def test_check_email_valid(self):
        self.assertTrue(check_mail('abc@1.com'))
        self.assertTrue(check_mail('abc@gmail.com.com'))
        self.assertTrue(check_mail('abc+100@gmail.com'))
        self.assertFalse(check_mail('abc'))
        self.assertFalse(check_mail('abc@.com.my'))
        self.assertFalse(check_mail('abc123@gmail.a'))
        

if __name__ == '__main__':
    unittest.main()



