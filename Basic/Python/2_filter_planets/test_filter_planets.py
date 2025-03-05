import unittest
from filter_planets import shorten_planets

class TestFilterShortPlanets(unittest.TestCase):
    def test_general_case(self):
        planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        self.assertEqual(shorten_planets(planets), ["Venus", "Earth", "Mars"])

    def test_all_short_names(self):
        planets = ["Mars", "Pluto", "Luna"]
        self.assertEqual(shorten_planets(planets), ["Mars", "Pluto", "Luna"])

    def test_all_long_names(self):
        planets = ["Mercury", "Jupiter", "Saturn"]
        self.assertEqual(shorten_planets(planets), [])

    def test_mixed_case(self):
        planets = ["earth", "MARS", "venus", "SATURN"]
        self.assertEqual(shorten_planets(planets), ["earth", "MARS", "venus"])

    def test_empty_list(self):
        planets = []
        self.assertEqual(shorten_planets(planets), [])

if __name__ == '__main__':
    unittest.main()
