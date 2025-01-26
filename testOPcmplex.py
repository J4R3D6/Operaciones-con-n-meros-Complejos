import OPcmplex as lc
import unittest

class TestOpcmplex (unittest.TestCase):

    def test_upper(self):
        self.assertEqual(lc.sum((3.5,6),(-6.7,2)),(-3.2, 8))
        self.assertEqual(lc.res((3.5,6),(-6.7,2)),(10.2, 4))
        self.assertEqual(lc.mult((3.5,6),(-6.7,2)),(-35.45, -33.2))
        div=lc.div((3.5,6),(-6.7,2))
        self.assertAlmostEqual(div[0],-0.2341992) 
        self.assertAlmostEqual(div[1],-0.9654326)
        self.assertAlmostEqual(lc.module((-6.7,2)),6.992138442565336)
        self.assertEqual(lc.conjugado((-6.7,2)),(-6.7, -2))
        car_a_pol=lc.cartesiana_a_polar((-6.7,2))
        self.assertAlmostEqual(car_a_pol[0], 6.9921384)
        self.assertAlmostEqual(car_a_pol[1], 2.8515057)
        pol_a_car=lc.polar_a_cartesiana((6.992138442565336,2.851505721268765))
        self.assertAlmostEqual(pol_a_car[0],-6.7)
        self.assertAlmostEqual(pol_a_car[1],2)


if __name__ == '__main__':
    unittest.main()