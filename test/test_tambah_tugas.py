import unittest
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from features.addTasks import input_task_data, tambah_tugas  # ✅ ganti dengan lokasi asli

class TestInputTaskData(unittest.TestCase):

    @patch("builtins.input", side_effect=[""])
    def test_judul_kosong(self, mock_input):
        buffer = StringIO()
        with redirect_stdout(buffer):
            result = input_task_data()
        output = buffer.getvalue()

        self.assertIsNone(result)
        self.assertIn("Judul tidak boleh kosong", output)

    @patch("builtins.input", side_effect=["Belajar Python", ""])
    def test_deskripsi_kosong(self, mock_input):
        buffer = StringIO()
        with redirect_stdout(buffer):
            result = input_task_data()
        output = buffer.getvalue()

        self.assertIsNone(result)
        self.assertIn("Judul tidak boleh kosong", output)

    @patch("builtins.input", side_effect=["Belajar Python", "Unit testing", "20/09/2025"])
    def test_valid_input(self, mock_input):
        result = input_task_data()
        self.assertEqual(result, ("Belajar Python", "Unit testing", "20/09/2025"))


class TestTambahTugas(unittest.TestCase):

    @patch("features.addTasks.input_task_data", return_value=None)
    def test_input_none(self, mock_func):
        buffer = StringIO()
        tasks = []
        with redirect_stdout(buffer):
            tambah_tugas(tasks)
        output = buffer.getvalue()

        self.assertEqual(tasks, [])
        self.assertIn("Tambah Tugas Baru", output)

    @patch("features.addTasks.input_task_data", return_value=("Judul", "Desk", "20-09-2025"))
    @patch("features.addTasks.validate_deadline", return_value=False)
    def test_deadline_invalid(self, mock_deadline, mock_input):
        buffer = StringIO()
        tasks = []
        with redirect_stdout(buffer):
            tambah_tugas(tasks)
        output = buffer.getvalue()

        self.assertEqual(tasks, [])
        self.assertIn("Format tanggal salah", output)

    @patch("features.addTasks.input_task_data", return_value=("Judul", "Desk", "20/09/2025"))
    @patch("features.addTasks.validate_deadline", return_value=True)
    @patch("features.addTasks.generate_task_id", return_value="TASK-1")
    @patch("features.addTasks.create_task", return_value={"id": "TASK-1", "judul": "Judul", "deskripsi": "Desk", "deadline": "20/09/2025", "status": "Pending"})
    def test_tambah_sukses(self, mock_create, mock_id, mock_deadline, mock_input):
        buffer = StringIO()
        tasks = []
        with redirect_stdout(buffer):
            tambah_tugas(tasks)
        output = buffer.getvalue()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["id"], "TASK-1")
        self.assertIn("berhasil ditambahkan", output)


if __name__ == "__main__":
    unittest.main()
