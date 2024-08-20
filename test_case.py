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
        self.assertTrue(check_mail('abc@yahoo.com'))
        self.assertTrue(check_mail('abc-100@yahoo.com'))
        self.assertTrue(check_mail('abc.100@yahoo.com'))
        self.assertTrue(check_mail('abc111@abc.com'))
        self.assertTrue(check_mail('abc-100@abc.net'))
        self.assertTrue(check_mail('abc.100@abc.com.au'))
        self.assertTrue(check_mail('abc@1.com'))
        self.assertTrue(check_mail('abc@gmail.com.com'))
        self.assertTrue(check_mail('abc+100@gmail.com'))
        self.assertFalse(check_mail('abc'))
        self.assertFalse(check_mail('abc@.com.my'))
        self.assertFalse(check_mail('abc123@gmail.a'))
        self.assertFalse(check_mail('abc123@.com'))
        self.assertFalse(check_mail('abc123@.com.com'))
        self.assertFalse(check_mail('abc()*@gmail.com'))
        self.assertFalse(check_mail('.abc@abc.com'))
        self.assertFalse(check_mail('abc@%*.com'))
        self.assertFalse(check_mail('abc..2002@gmail.com'))
        self.assertFalse(check_mail('abc@abc@gmail.com'))
        self.assertFalse(check_mail('abc@gmail.com.1a'))
        self.assertFalse(check_mail('abc@gmail.com.aa.au'))
        
    def test_check_phone_valid(self):
        self.assertTrue(check_phonenumber('+91 9919819801'))
        self.assertTrue(check_phonenumber('91 9919819801'))
        self.assertFalse(check_phonenumber('919919819801'))
        self.assertFalse(check_phonenumber('+91-9919819801'))
        self.assertFalse(check_phonenumber('91 99198198'))
        
    def test_check_password_valid(self):
        self.assertEqual(check_password('abc'),0)
        self.assertEqual(check_password('abc@.com.my'),0)
        self.assertEqual(check_password('abc123@gmail.a'),0)
        self.assertEqual(check_password('abc123@.com'),0)
        self.assertEqual(check_password('abc123@.com.com'),0)
        self.assertEqual(check_password('Abcyah12@oocom'),1)
        self.assertEqual(check_password('abc-100@yaHoocom'),1)
        self.assertEqual(check_password('Abc100@yahoocom'),1)
       

if __name__ == '__main__':
    unittest.main()