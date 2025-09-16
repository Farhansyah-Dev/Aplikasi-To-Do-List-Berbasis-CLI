import unittest
from unittest.mock import patch
from utils.generatorID import generate_task_id


class TestGenerateTaskID(unittest.TestCase):

    def test_format_id_string(self):
        """ID harus berupa string"""
        with patch("random.randint", return_value=456):
            task_id = generate_task_id(0)  # index = 0 → jadi "4561"
            self.assertIsInstance(task_id, str)

    def test_id_mengandung_random_dan_index(self):
        """ID terdiri dari 3 digit random + (index+1)"""
        with patch("random.randint", return_value=789):
            task_id = generate_task_id(4)  # index = 4 → jadi "7895"
            self.assertEqual(task_id, "7895")

    def test_random_part_dalam_rentang(self):
        """Random part harus selalu 100–999"""
        for _ in range(50):
            random_part = int(generate_task_id(0)[:-1])  # ambil 3 digit pertama
            self.assertGreaterEqual(random_part, 100)
            self.assertLessEqual(random_part, 999)

    def test_index_increment(self):
        """Pastikan index + 1 ditambahkan dengan benar"""
        with patch("random.randint", return_value=123):
            self.assertEqual(generate_task_id(0), "1231")
            self.assertEqual(generate_task_id(1), "1232")
            self.assertEqual(generate_task_id(9), "12310")


if __name__ == "__main__":
    unittest.main()
