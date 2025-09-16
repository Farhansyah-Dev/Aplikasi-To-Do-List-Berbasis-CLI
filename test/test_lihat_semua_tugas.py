import unittest
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from features.ViewTasks import lihat_semua_tugas

class TestLihatSemuaTugas(unittest.TestCase):

    def test_daftar_kosong(self):
        tasks = []
        buffer = StringIO()
        with redirect_stdout(buffer):
            with patch("builtins.input", return_value=""):  # mock input
                lihat_semua_tugas(tasks)

        output = buffer.getvalue()
        self.assertIn("Belum ada tugas", output)

    def test_daftar_berisi(self):
        tasks = [{
            "id": 1,
            "judul": "Belajar Python",
            "deskripsi": "Mempelajari dasar unit test",
            "status": "Pending",
            "deadline": "2025-09-20",
            "waktu_buat": "2025-09-16",
            "waktu_ubah": "2025-09-16"
        }]
        buffer = StringIO()
        with redirect_stdout(buffer):
            with patch("builtins.input", return_value=""):  # mock input
                lihat_semua_tugas(tasks)

        output = buffer.getvalue()
        self.assertIn("Daftar Tugas", output)
        self.assertIn("Belajar Python", output)
        self.assertIn("Pending", output)

if __name__ == "__main__":
    unittest.main()