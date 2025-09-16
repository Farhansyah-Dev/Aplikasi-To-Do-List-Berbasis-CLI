import unittest
from unittest.mock import patch
from datetime import datetime
from models.tasksModel import create_task


class TestTasksModel(unittest.TestCase):

    @patch("models.tasksModel.datetime")
    def test_create_task_structure(self, mock_datetime):
        # Mock datetime.now() → 16/09/2025 10:00:00
        mock_datetime.now.return_value = datetime(2025, 9, 16, 10, 0, 0)
        mock_datetime.strftime = datetime.strftime

        task = create_task("101", "Judul Tugas", "Deskripsi Tugas", "20/09/2025")

        # Cek semua key ada
        expected_keys = ["id", "judul", "deskripsi", "status", "deadline", "waktu_buat", "waktu_ubah"]
        for key in expected_keys:
            self.assertIn(key, task)

        # Cek value sesuai input
        self.assertEqual(task["id"], "101")
        self.assertEqual(task["judul"], "Judul Tugas")
        self.assertEqual(task["deskripsi"], "Deskripsi Tugas")
        self.assertEqual(task["status"], "Belum Selesai")
        self.assertEqual(task["deadline"], "20/09/2025")

        # Cek waktu_buat dan waktu_ubah sesuai mock
        expected_time = "16/09/2025 10:00:00"
        self.assertEqual(task["waktu_buat"], expected_time)
        self.assertEqual(task["waktu_ubah"], expected_time)


if __name__ == "__main__":
    unittest.main()
