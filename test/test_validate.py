import unittest
from unittest.mock import patch
from datetime import datetime
from utils.validate import validate_deadline


class TestValidateDeadline(unittest.TestCase):

    @patch("utils.validate.datetime")
    def test_tanggal_valid_di_hari_ini(self, mock_datetime):
        # Mock datetime.now() → 16/09/2025
        mock_datetime.now.return_value = datetime(2025, 9, 16, 10, 0, 0)
        mock_datetime.strptime = datetime.strptime
        mock_datetime.replace = datetime.replace

        self.assertTrue(validate_deadline("16/09/2025"))

    @patch("utils.validate.datetime")
    def test_tanggal_valid_di_masa_depan(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2025, 9, 16, 10, 0, 0)
        mock_datetime.strptime = datetime.strptime
        mock_datetime.replace = datetime.replace

        self.assertTrue(validate_deadline("20/09/2025"))

    @patch("utils.validate.datetime")
    def test_tanggal_valid_di_masa_lalu(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2025, 9, 16, 10, 0, 0)
        mock_datetime.strptime = datetime.strptime
        mock_datetime.replace = datetime.replace

        self.assertFalse(validate_deadline("10/09/2025"))

    def test_format_salah(self):
        # Format tidak sesuai DD/MM/YYYY
        self.assertFalse(validate_deadline("2025-09-16"))
        self.assertFalse(validate_deadline("16-09-2025"))
        self.assertFalse(validate_deadline("abcd"))


if __name__ == "__main__":
    unittest.main()
