"""Unit tests for cleaning functions."""
import unittest
import pandas as pd
import cleaning_utils as cu

REST_FILE_SHAPE = (24941, 6)


class TestCleaningFunctions(unittest.TestCase):
    """Contains test cases for various scenarios."""

    def test_spitZip(self):
        """Check if zip code splits correctly."""
        testzip = "11426.0-1175"
        actualzip = "11426"
        self.assertEqual(cu.splitZip(testzip), actualzip)

    def test_rest_name(self):
        """Check if restaurant name splits from address correctly."""
        comb_name = "Restaurant Name 11(Buliding Number) Address Zipcode"
        actual_name = "Restaurant Name"
        self.assertEqual(cu.rest_name(comb_name), actual_name)

    def test_add(self):
        """Check if Address added correctly."""
        row = pd.DataFrame(columns=['Restaurant', 'Name'])
        row.loc[0] = ["Restaurant Name 11(Buliding Number) Address Zipcode",
                      "Restaurant Name"]
        address = " 11(Buliding Number) Address Zipcode"
        add = row.apply(cu.rest_add, axis=1)[0]
        self.assertEqual(add, address)

    def test_clean_restaurants_go(self):
        """Check if file is cleaned correctly."""
        fileDetails = pd.read_csv("./Data/NYC Restaurants \
            Geocoded - Sheet1.csv")
        final_df = cu.clean_restraunts_geo(fileDetails)
        self.assertEqual(final_df.shape, REST_FILE_SHAPE)


if __name__ == "__main__":
    unittest.main()
