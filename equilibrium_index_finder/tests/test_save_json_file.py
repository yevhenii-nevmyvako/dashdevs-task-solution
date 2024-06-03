import json
import os
import tempfile
import unittest

from equilibrium_index_finder.core.base import save_result_to_json


class TestSaveResultToJson(unittest.TestCase):
    def test_save_result_to_json(self):
        result_data = 3

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            dst_filepath = temp_file.name
            save_result_to_json(result_data, dst_filepath)

            self.assertTrue(os.path.exists(dst_filepath))
            with open(dst_filepath, 'r') as f:
                saved_data = json.load(f)
                self.assertEqual(saved_data['equilibrium_index'], result_data)

            os.remove(dst_filepath)


if __name__ == '__main__':
    unittest.main()
