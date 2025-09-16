import unittest
from unittest.mock import patch
from features.DeleteTasks import (
    tampilkan_tugas,
    pilih_tugas,
    konfirmasi_hapus,
    hapus_tugas_with_warning,
)


class TestDeleteTasks(unittest.TestCase):

    def setUp(self):
        self.tasks = [
            {"id": "1", "judul": "Tugas 1", "deskripsi": "Deskripsi 1", "status": "Belum Selesai", "deadline": "20/09/2025", "waktu_buat": "16/09/2025", "waktu_ubah": "16/09/2025"},
            {"id": "2", "judul": "Tugas 2", "deskripsi": "Deskripsi 2", "status": "Selesai", "deadline": "21/09/2025", "waktu_buat": "16/09/2025", "waktu_ubah": "16/09/2025"},
        ]

    # ------------------------
    # Unit tests
    # ------------------------
    def test_tampilkan_tugas_kosong(self):
        with patch("builtins.print") as mock_print:
            result = tampilkan_tugas([])
            self.assertFalse(result)
            mock_print.assert_any_call("Belum ada tugas yang tersimpan.")

    def test_tampilkan_tugas_berisi(self):
        with patch("builtins.print"):
            result = tampilkan_tugas(self.tasks)
            self.assertTrue(result)

    def test_pilih_tugas_valid(self):
        with patch("builtins.input", return_value="1"):
            index = pilih_tugas(self.tasks)
            self.assertEqual(index, 0)

    def test_pilih_tugas_invalid_number(self):
        with patch("builtins.input", return_value="5"), patch("builtins.print") as mock_print:
            index = pilih_tugas(self.tasks)
            self.assertIsNone(index)
            mock_print.assert_any_call("❌ Nomor tugas tidak valid.")

    def test_pilih_tugas_invalid_input(self):
        with patch("builtins.input", return_value="abc"), patch("builtins.print") as mock_print:
            index = pilih_tugas(self.tasks)
            self.assertIsNone(index)
            mock_print.assert_any_call("❌ Input harus berupa angka.")

    def test_konfirmasi_hapus_yes(self):
        task = self.tasks[0]
        with patch("builtins.input", return_value="y"):
            result = konfirmasi_hapus(task)
            self.assertTrue(result)

    def test_konfirmasi_hapus_no(self):
        task = self.tasks[0]
        with patch("builtins.input", return_value="n"):
            result = konfirmasi_hapus(task)
            self.assertFalse(result)

    # ------------------------
    # Integration tests
    # ------------------------
    def test_hapus_tugas_with_warning_yes(self):
        with patch("builtins.input", side_effect=["1", "y"]), patch("builtins.print"):
            hapus_tugas_with_warning(self.tasks)
        self.assertEqual(len(self.tasks), 1)  # Tugas pertama terhapus
        self.assertEqual(self.tasks[0]["judul"], "Tugas 2")

    def test_hapus_tugas_with_warning_no(self):
        with patch("builtins.input", side_effect=["1", "n"]), patch("builtins.print"):
            hapus_tugas_with_warning(self.tasks)
        self.assertEqual(len(self.tasks), 2)  # Tidak ada yang dihapus


if __name__ == "__main__":
    unittest.main()
