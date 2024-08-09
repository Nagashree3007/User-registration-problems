import unittest
from use_registration import check_name
from use_registration import check_mail
from use_registration import check_phonenumber
from use_registration  import check_password

class TestCheckName(unittest.TestCase):
    def test_check_name_valid(self):
        self.assertEqual(check_name('John'), 1)
        self.assertEqual(check_name('Alice'), 1)
        self.assertEqual(check_name('Jo'), 0)
        self.assertEqual(check_name('john'), 0) 
        self.assertEqual(check_name('al'), 0)
        self.assertEqual(check_name('aLice'), 0)
        
    def test_check_email_valid(self):
        self.assertTrue(check_mail('abc.xyz@bl.co.in'))
        self.assertTrue(check_mail('example@bl.co'))
        self.assertTrue(check_mail('example@bl.co.in'))
        self.assertFalse(check_mail('abc@xyz.co'))
        self.assertFalse(check_mail('example@bl.com'))
        
    def test_check_phone_valid(self):
        self.assertTrue(check_phonenumber('+91 9919819801'))
        self.assertTrue(check_phonenumber('91 9919819801'))
        self.assertFalse(check_phonenumber('919919819801'))
        self.assertFalse(check_phonenumber('+91-9919819801'))
        self.assertFalse(check_phonenumber('91 99198198'))
        
    def test_check_password_valid(self):
        self.assertEqual(check_password('Password1'), 1)
        self.assertEqual(check_password('A1bB2c3d4'), 1)
        self.assertEqual(check_password('sPass1'), 0)
        self.assertEqual(check_password('short1'), 0  )
        self.assertEqual(check_password('password'), 1)
        

if __name__ == '__main__':
    unittest.main()