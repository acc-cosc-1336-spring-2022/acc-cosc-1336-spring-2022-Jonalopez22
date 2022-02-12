import unittest

from src.homework.b_in_proc_out.output import multiply_number
from src.homework.b_in_proc_out.output import test_config
 
class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual (True, test_config())
    
    def test_multiply_number_1(self):
        self.assertEqual(25, multiply_number(5, 5))
    
    def test_multiply_number_2(self):
        self.assertEqual(100, multiply_number(10, 10))


    

