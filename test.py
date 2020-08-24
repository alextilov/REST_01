from base import Countries
import yaml
import unittest
import HtmlTestRunner


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("./config.yml", "r") as config:
            cfg = yaml.safe_load(config)

        url = cfg['api'].get('url')
        o = Countries(url)
        cls.capital_by_code = o.get_capital_by_code("LVA")
        cls.capital_by_name = o.get_capital_by_country_name("Latvia")
        cls.capital_by_index = o.get_capital_by_index(124)

    def test_country_code(self):
        self.assertTrue(self.capital_by_code == "Riga", "Test failed: capital by code")

    def test_country_name(self):
        self.assertTrue(self.capital_by_name == "Riga", "Test failed: capital by name")

    def test_country_index(self):
        self.assertTrue(self.capital_by_index == "Riga", "Test failed: capital by index")


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='test-reports',
            open_in_browser=True,
            combine_reports=True
            )
        )


