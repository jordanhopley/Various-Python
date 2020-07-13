import unittest
import python_parser


class TestParser(unittest.TestCase):

    def test_download_JSON(self):
        returned_value = python_parser.download_json()
        assert isinstance(returned_value, list)

    def test_json_parser(self):
        test_dict = {"id": "1", "url": "2", "name": "3", }
        parsed_json = python_parser.parse_json(test_dict)
        if parsed_json == ["1", "2", "3"]:
            assert True
        else:
            assert False

    def test_nested_json_parser(self):
        test_dict = {
            "rating": {
                "average": "1"
            },
            "network": {
                "name": "2"
            },
            "image": {
                "original": "3"
            }
        }
        parsed_json = python_parser.parse_json(test_dict)
        if parsed_json == ["1", "2", "3"]:
            assert True
        else:
            assert False


if __name__ == '__main__':
    unittest.main()
