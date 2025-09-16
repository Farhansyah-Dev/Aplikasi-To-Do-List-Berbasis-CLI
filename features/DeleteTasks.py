TAKS_STATUS_DONE = 'Selesai'

def tampilkan_tugas(tasks: list) -> bool:
    """
    Menampilkan daftar tugas ke layar.

    Args:
        tasks (list): List yang berisi semua tugas saat ini. 
                      Setiap tugas adalah dictionary dengan key:
                      'id', 'judul', 'deskripsi', 'status', 'deadline', 'waktu_buat', 'waktu_ubah'

    Returns:
        bool: True jika ada tugas, False jika list kosong

    Example:
        >>> tasks = [{"id":"101", "judul":"Belajar Python", "status":"Belum Selesai"}]
        >>> tampilkan_tugas(tasks)
        1. Belajar Python | Status: Belum Selesai
    """
    print('\n--- Daftar Tugas ---')

    if not tasks:
        print('Belum ada tugas yang tersimpan.')
        return False  # Mengembalikan False agar fungsi pemanggil tahu tidak ada tugas

    # Tampilkan semua tugas dengan nomor urut mulai dari 1
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t['judul']} | Status: {t['status']}")
    return True


def pilih_tugas(tasks):
    """
    Meminta user memilih nomor tugas yang valid dari daftar.

    Args:
        tasks (list): List tugas saat ini

    Returns:
        int | None: Index tugas yang dipilih (0-based) atau None jika input tidak valid
    """
    try:
        pilihan = int(input('\nMasukan nomor tugas yang ingin dihapus: '))
        if 1 <= pilihan <= len(tasks):
            return pilihan - 1  # Convert ke index 0-based
        else:
            print("❌ Nomor tugas tidak valid.")
            return None
    except ValueError:
        # Jika input bukan angka
        print("❌ Input harus berupa angka.")
        return None


def konfirmasi_hapus(task):
    """
    Meminta konfirmasi sebelum menghapus tugas.
    Jika tugas belum selesai, tampilkan peringatan ekstra.

    Args:
        task (dict): Tugas yang akan dihapus

    Returns:
        bool: True jika user yakin, False jika dibatalkan
    """
    if task['status'] != TAKS_STATUS_DONE:
        # Tricky: beri peringatan ekstra jika tugas belum selesai
        confirm = input(f"⚠️ Tugas '{task['judul']}' belum selesai. Yakin mau hapus? (y/n): ")
    else:
        confirm = input(f"Apakah yakin ingin menghapus '{task['judul']}'? (y/n): ")

    return confirm.strip().lower() == 'y'


def hapus_tugas_with_warning(tasks):
    """
    Menghapus tugas dari daftar dengan konfirmasi.
    Jika tugas belum selesai, beri warning ekstra.

    Args:
        tasks (list): List semua tugas saat ini

    Returns:
        None

    Process:
        1. Tampilkan semua tugas
        2. Minta user memilih tugas
        3. Minta konfirmasi penghapusan
        4. Hapus tugas jika user yakin, atau batalkan
    """
    # Tampilkan daftar tugas, jika kosong langsung keluar
    if not tampilkan_tugas(tasks):
        return

    # Minta user memilih tugas
    index = pilih_tugas(tasks)
    if index is None:
        return

    task = tasks[index]

    # Tricky: konfirmasi penghapusan, beri warning jika belum selesai
    if konfirmasi_hapus(task):
        tasks.pop(index)  # Hapus tugas dari list
        print(f"✅ Tugas '{task['judul']}' berhasil dihapus.")
    else:
        print("❌ Penghapusan dibatalkan.")
