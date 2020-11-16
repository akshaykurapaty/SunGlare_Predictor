import unittest
from API.PredictGlare import predict_glare;

class MyTestCase(unittest.TestCase):
    def test_Predict_glare(self):
        self.assertEqual(type(predict_glare().detect_glare(latitude=49.2699648, longitude=-123.1290368, epoch=1588704959.321, orientation=-10.2)), bool)
    def test_get_local_timezone(self):
        self.assertEqual(predict_glare().get_local_timezone(latitude=49.2699648, longitude=-123.1290368),'America/Vancouver');
    # Write rest of the unit test cases
    def test_get_localtime(self):
        self.assertEqual(True, False);
    def get_car_azimuth(self):
        self.assertEqual(True, False);
    def get_sun_azimuth_altitude(self):
        self.assertEqual(True, False);
    def get_azimuthal_difference(self):
        self.assertEqual(True, False);
    def get_is_possible_glare(self):
        self.assertEqual(True, False);

if __name__ == '__main__':
    unittest.main()
