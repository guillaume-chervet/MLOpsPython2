import unittest
from pathlib import Path

from extraction import extract_images_from_pdf

BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH / "output"
input_directory = BASE_PATH / "input"
class MyTestCase(unittest.TestCase):
    def test_something(self):
        images = extract_images_from_pdf(str(input_directory), str(output_directory))
        expected_result = ['0a2e1fd1-1cd8-43d9-a2d0-79a222e858e6_page0_index0.png',
                           '0a2e1fd1-1cd8-43d9-a2d0-79a222e858e6_page1_index0.png',
                           '0a2e1fd1-1cd8-43d9-a2d0-79a222e858e6_page2_index0.png',
                           '0a2e1fd1-1cd8-43d9-a2d0-79a222e858e6_page3_index0.png']
        self.assertEqual(expected_result, images)  # add assertion here


if __name__ == '__main__':
    unittest.main()
