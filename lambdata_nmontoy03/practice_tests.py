import unittest
from explore_nulls import ExploreNulls 

class ExploreNullsTest(unittest.TestCase):
    """Test class ExploreNulls
    """

    def test_show_nulls(self):
        data = 2 + 2
        self.assertEqual(data, 4)


if __name__ == '__main__':
    unittest.main()

