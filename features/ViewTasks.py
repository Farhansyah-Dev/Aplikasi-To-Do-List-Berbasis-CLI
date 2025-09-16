def lihat_semua_tugas(tasks):
    """
    Menampilkan semua tugas yang ada di daftar tasks.

    Args:
        tasks (list): List yang berisi semua tugas saat ini. 
                      Setiap tugas adalah dictionary dengan key:
                      'id', 'judul', 'deskripsi', 'status', 'deadline', 'waktu_buat', 'waktu_ubah'

    Returns:
        None

    Process:
        - Jika list kosong, tampilkan pesan "Belum ada tugas"
        - Jika ada tugas, tampilkan satu per satu dengan nomor urut
        - Menunggu input Enter sebelum menampilkan tugas berikutnya

    Example:
        >>> tasks = [{"id":"101", "judul":"Belajar Python", "deskripsi":"Modul pengenalan",
                      "status":"Belum Selesai", "deadline":"20/09/2025",
                      "waktu_buat":"16/09/2025 10:00:00", "waktu_ubah":"16/09/2025 10:00:00"}]
        >>> lihat_semua_tugas(tasks)
        Daftar Tugas:
        Tugas ke-1
        ID         : 101
        Judul      : Belajar Python
        Deskripsi  : Modul pengenalan
        Status     : Belum Selesai
        Deadline   : 20/09/2025
        Waktu Buat : 16/09/2025 10:00:00
        Waktu Ubah : 16/09/2025 10:00:00
        --------------------------------------------------
        Tekan Enter untuk melihat tugas berikutnya...
    """
    if not tasks:
        print("\n🔎 Belum ada tugas.\n")
    else:
        # Tricky: tampilkan semua tugas satu per satu dan tunggu Enter setiap kali
        for i, task in enumerate(tasks, start=1):
            print(f"Tugas ke-{i}")
            print(f"ID         : {task['id']}")
            print(f"Judul      : {task['judul']}")
            print(f"Deskripsi  : {task['deskripsi']}")
            print(f"Status     : {task['status']}")
            print(f"Deadline   : {task['deadline']}")
            print(f"Waktu Buat : {task['waktu_buat']}")
            print(f"Waktu Ubah : {task['waktu_ubah']}")
            print("-"*50)
            input("Tekan Enter untuk melihat tugas berikutnya...")
