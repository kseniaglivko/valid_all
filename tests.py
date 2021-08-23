from utils import process_json, output_validation
import unittest


class TestTreatmentOfGoods(unittest.TestCase):

    def test_wrong_format(self):
        self.assertRaises(Exception, process_json, "./test_files/wrong_format.json")

    def test_wrong_result(self):
        self.assertRaises(Exception, output_validation, "./test_files/wrong_email.json")

    def test_wrong_field(self):
        self.assertRaises(Exception, process_json, "./test_files/wrong_number.json")

if __name__ == "__main__":
    unittest.main()
