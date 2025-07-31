import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2),3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(2,1),1)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(-1,-1),1)
        self.assertEqual(mul(5,-1),-5)
        self.assertEqual(mul(2,3),6)

    def test_divide(self): # 3 assertions
        self.assertEqual((div(-1,10)),-10)
        self.assertEqual((div(2,10)),5)
        self.assertAlmostEqual((div(10,0.3)),33.33, places=2)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2,2),1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(2, 0)
        with self.assertRaises(ValueError):
            log(2, -1)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(-5,-5),7.07, places=2)
        self.assertAlmostEqual(hypotenuse(5,-5),7.07, places=2)
        self.assertAlmostEqual(hypotenuse(6,-6), 8.48, places=2)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-10)
        self.assertEqual(square_root(0),0.0)
        self.assertEqual(square_root(36),6.0)
           
        
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()