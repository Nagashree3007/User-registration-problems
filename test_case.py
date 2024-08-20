'''

@Author: Nagashree C R
@Date: 2024-08-8-07
@Last Modified by: Nagashree C R
@Last Modified: 2024-08-07
@Title :User registration problems UC7-User need to follow pre-defined Password rules.
        Rule4– Should have exactly 1 Special Character  test case

'''
import unittest
from use_registration import check_password, check_name, check_mail, check_phonenumber

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
        
    def test_check_phone_valid(self):
        self.assertTrue(check_phonenumber('+91 9919819801'))
        self.assertTrue(check_phonenumber('91 9919819801'))
        self.assertFalse(check_phonenumber('919919819801'))
        self.assertFalse(check_phonenumber('+91-9919819801'))
        self.assertFalse(check_phonenumber('91 99198198'))
        
    def test_check_password_valid(self):
        self.assertEqual(check_password('Password1@'), 1, "Failed for 'Password1@'")
        self.assertEqual(check_password('A1@abcdefgh'), 1, "Failed for 'A1@abcdefgh'")
        self.assertEqual(check_password('Short1@'), 0, "Failed for 'Short1@'")
        self.assertEqual(check_password('Pwd1@'), 0, "Failed for 'Pwd1@'")

if __name__ == '__main__':
    unittest.main()