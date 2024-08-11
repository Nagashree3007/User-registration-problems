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
        self.assertEqual(check_password('abc'),0)
        self.assertEqual(check_password('abc@.com.my'),0)
        self.assertEqual(check_password('abc123@gmail.a'),0)
        self.assertEqual(check_password('abc123@.com'),0)
        self.assertEqual(check_password('abc123@.com.com'),0)
        self.assertEqual(check_password('.abc@abc.com'),0)
        self.assertEqual(check_password('abc()*@gmail.com'),0)
        self.assertEqual(check_password('abc@%*.com'),0)
        self.assertEqual(check_password('abc..2002@gmail.com'),0)
        self.assertEqual(check_password('abc.@gmail.com'),0)
        self.assertEqual(check_password('abc@abc@gmail.com'),0)
        self.assertEqual(check_password('abc@gmail.com.1a'),0)
        self.assertEqual(check_password('abc@gmail.com.aa.au'),0)
        self.assertEqual(check_password('abc111@abccom'),0)

        self.assertEqual(check_password('Abcyah12@oocom'),1)
        self.assertEqual(check_password('abc-100@yaHoocom'),1)
        self.assertEqual(check_password('Abc100@yahoocom'),1)
        self.assertEqual(check_password('aBc111@abcnet'),1)
        self.assertEqual(check_password('abc100@Abccomau'),1)
        self.assertEqual(check_password('abc@1cOm'),1)
        self.assertEqual(check_password('abc@gmailC7omcom'),1)
        self.assertEqual(check_password('aBc100@gmailcom'),1)



if __name__ == '__main__':
    unittest.main()