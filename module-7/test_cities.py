import unittest
from city_functions import city_country

class CityUnitTest(unittest.TestCase):

    def test_city_country(self):
        santiago_chili = city_country('Santiago', 'Chile')
        self.assertEqual(santiago_chili, 'Santiago, Chile')
        paris_france = city_country('Paris', 'France')
        self.assertEqual(paris_france, 'Paris, France')
        tokoyo_japan = city_country('Tokyo', 'Japan')
        self.assertEqual(tokoyo_japan, 'Tokyo, Japan')
if __name__ == '__main__':
    unittest.main()

