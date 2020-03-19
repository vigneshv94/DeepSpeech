import unittest

from argparse import Namespace
from .importers import validate_label_eng, get_validate_label

class TestValidateLabelEng(unittest.TestCase):

    def test_numbers(self):
        label = validate_label_eng("this is a 1 2 3 test")
        self.assertEqual(label, None)

class TestGetValidateLabel(unittest.TestCase):

    def test_no_validate_label_locale(self):
        f = get_validate_label(Namespace())
        self.assertEqual(f('toto'), 'toto')
        self.assertEqual(f('toto1234'), None)
        self.assertEqual(f('toto1234[{[{[]'), None)

    def test_validate_label_locale_default(self):
        f = get_validate_label(Namespace(validate_label_locale=None))
        self.assertEqual(f('toto'), 'toto')
        self.assertEqual(f('toto1234'), None)
        self.assertEqual(f('toto1234[{[{[]'), None)

    def test_get_validate_label_missing(self):
        args = Namespace(validate_label_locale='util/test_data/validate_locale_ger.py')
        f = get_validate_label(args)
        self.assertEqual(f, None)

    def test_get_validate_label(self):
        args = Namespace(validate_label_locale='util/test_data/validate_locale_fra.py')
        f = get_validate_label(args)
        l = f('toto')
        self.assertEqual(l, 'toto')

if __name__ == '__main__':
    unittest.main()
