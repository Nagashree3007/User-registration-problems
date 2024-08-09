import unittest
from use_registration import check_name

class TestCheckName(unittest.TestCase):
    def test_check_name_valid(self):
        self.assertEqual(check_name('John'), 1)
        self.assertEqual(check_name('Alice'), 1)
        self.assertEqual(check_name('Jo'), 0)
        self.assertEqual(check_name('john'), 0)
        self.assertEqual(check_name('al'), 0)
        self.assertEqual(check_name('aLice'), 0)

if __name__ == '__main__':
    unittest.main()



