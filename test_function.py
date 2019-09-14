import unittest
import area_functions as af

class AFTestCase(unittest.TestCase):
    '''tests for area_functions.py.'''

    def test_area_rect(self):
        '''Test a simple rectangle.'''
        area = af.area_rect(3,4)
        self.assertEqual(area, 12)

if __name__ == '__main__':
    unittest.main()
