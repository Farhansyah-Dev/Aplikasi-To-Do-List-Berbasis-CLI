from models.tasksModel import create_task
from utils.generatorID import generate_task_id
from utils.validate import validate_deadline


def input_task_data():
    """
    Meminta input user saat menambahkan tugas baru.

    Returns:
        tuple: (judul, deskripsi, deadline) jika input valid
        None: jika input tidak valid / kosong

    Example:
        >>> data = input_task_data()
        Masukkan judul tugas: Belajar Python
        Masukkan deskripsi tugas: Modul pengenalan Python
        Masukkan deadline (DD/MM/YYYY): 20/09/2025
        >>> data
        ('Belajar Python', 'Modul pengenalan Python', '20/09/2025')
    """
    while True:
        # Input judul, tidak boleh kosong
        judul = input("Masukkan judul tugas: ").strip()
        if not judul:
            print("❌ Judul tidak boleh kosong!")
            return None

        # Input deskripsi, tidak boleh kosong
        deskripsi = input("Masukkan deskripsi tugas: ").strip()
        if not deskripsi:
            print("❌ Deskripsi tidak boleh kosong!")
            return None

        # Input deadline, tidak boleh kosong
        deadline = input("Masukkan deadline (DD/MM/YYYY): ").strip()
        if not deadline:
            print("❌ Deadline tidak boleh kosong!")
            return None

        return judul, deskripsi, deadline


def tambah_tugas(tasks: list):
    """
    Menambahkan tugas baru ke daftar tasks.

    Proses:
        1. Meminta input judul, deskripsi, deadline dari user
        2. Memvalidasi format tanggal deadline (DD/MM/YYYY) dan past date
        3. Generate ID unik berdasarkan jumlah tugas saat ini
        4. Membuat task baru dengan create_task()
        5. Menambahkan task ke list tasks

    Args:
        tasks (list): List yang berisi semua tugas saat ini

    Returns:
        None

    Example:
        >>> tasks = []
        >>> tambah_tugas(tasks)
        Masukkan judul tugas: Belajar Python
        Masukkan deskripsi tugas: Modul pengenalan Python
        Masukkan deadline (DD/MM/YYYY): 20/09/2025
        Tugas 'Belajar Python' berhasil ditambahkan dengan ID 101
    """
    print("\n--- Tambah Tugas Baru ---")

    data = input_task_data()
    if data is None:
        # Input tidak valid / user kosongkan
        return

    judul, deskripsi, deadline = data

    # Tricky: pastikan deadline valid sebelum menambahkan task
    if not validate_deadline(deadline):
        print("Format tanggal salah! Harus DD/MM/YYYY. Tugas dibatalkan.\n")
        return

    # Generate ID berdasarkan index terakhir dalam list tasks
    index = len(tasks)
    task_id = generate_task_id(index)

    # Buat task baru
    task = create_task(task_id, judul, deskripsi, deadline)

    # Tambahkan task ke daftar
    tasks.append(task)
    print(f"Tugas '{judul}' berhasil ditambahkan dengan ID {task_id}.\n")
