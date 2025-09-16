import unittest
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from features.StatusTasks import ubah_status

class TestUbahStatus(unittest.TestCase):

    def test_daftar_kosong(self):
        tasks = []
        buffer = StringIO()
        with redirect_stdout(buffer):
            ubah_status(tasks)
        output = buffer.getvalue()
        self.assertIn("Tidak ada tugas", output)

    @patch("builtins.input", side_effect=["abc"])  # input bukan angka
    def test_input_bukan_angka(self, mock_input):
        tasks = [{"judul": "Tugas 1", "status": "Belum Selesai", "waktu_ubah": ""}]
        buffer = StringIO()
        with redirect_stdout(buffer):
            ubah_status(tasks)
        output = buffer.getvalue()
        self.assertIn("Input tidak valid", output)

    @patch("builtins.input", side_effect=["5"])  # nomor di luar jangkauan
    def test_nomor_tugas_tidak_ditemukan(self, mock_input):
        tasks = [{"judul": "Tugas 1", "status": "Belum Selesai", "waktu_ubah": ""}]
        buffer = StringIO()
        with redirect_stdout(buffer):
            ubah_status(tasks)
        output = buffer.getvalue()
        self.assertIn("Nomor tugas tidak ditemukan", output)

    @patch("builtins.input", side_effect=["1"])  # pilih tugas pertama
    @patch("features.StatusTasks.datetime")      # mock datetime
    def test_toggle_belum_selesai_ke_selesai(self, mock_datetime, mock_input):
        mock_datetime.now.return_value.strftime.return_value = "16/09/2025 10:00:00"
        tasks = [{"judul": "Tugas 1", "status": "Belum Selesai", "waktu_ubah": ""}]
        buffer = StringIO()
        with redirect_stdout(buffer):
            ubah_status(tasks)
        output = buffer.getvalue()

        self.assertEqual(tasks[0]["status"], "Selesai")
        self.assertEqual(tasks[0]["waktu_ubah"], "16/09/2025 10:00:00")
        self.assertIn("berhasil diubah menjadi: Selesai", output)

    @patch("builtins.input", side_effect=["1"])  # pilih tugas pertama
    @patch("features.StatusTasks.datetime")      # mock datetime
    def test_toggle_selesai_ke_belum_selesai(self, mock_datetime, mock_input):
        mock_datetime.now.return_value.strftime.return_value = "16/09/2025 11:00:00"
        tasks = [{"judul": "Tugas 1", "status": "Selesai", "waktu_ubah": ""}]
        buffer = StringIO()
        with redirect_stdout(buffer):
            ubah_status(tasks)
        output = buffer.getvalue()

        self.assertEqual(tasks[0]["status"], "Belum Selesai")
        self.assertEqual(tasks[0]["waktu_ubah"], "16/09/2025 11:00:00")
        self.assertIn("berhasil diubah menjadi: Belum Selesai", output)


if __name__ == "__main__":
    unittest.main()
