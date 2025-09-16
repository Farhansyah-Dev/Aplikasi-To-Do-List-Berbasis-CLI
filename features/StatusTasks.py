from datetime import datetime

def ubah_status(tasks):
    """
    Mengubah status tugas antara 'Belum Selesai' dan 'Selesai'.
    Setiap kali status berubah, 'waktu_ubah' juga diperbarui otomatis.

    Args:
        tasks (list): List yang berisi semua tugas saat ini.
                      Setiap tugas adalah dictionary dengan key:
                      'id', 'judul', 'deskripsi', 'status', 'deadline', 'waktu_buat', 'waktu_ubah'

    Returns:
        None

    Process:
        - Menampilkan daftar tugas dengan nomor urut
        - Meminta user memilih nomor tugas
        - Mengubah status tugas yang dipilih
        - Update waktu terakhir diubah

    Example:
        >>> tasks = [{"id":"101", "judul":"Belajar Python", "status":"Belum Selesai"}]
        >>> ubah_status(tasks)
        Masukkan nomor tugas yang ingin diubah statusnya: 1
        ✅ Status tugas 'Belajar Python' berhasil diubah menjadi: Selesai
        📅 Waktu terakhir diubah: 16/09/2025 10:00:00
    """
    # Jika daftar tugas kosong, beri informasi ke user
    if not tasks:
        print("⚠️ Tidak ada tugas yang tersedia.")
        return

    # Tampilkan semua tugas agar user tahu nomor urutnya
    print("\nDaftar Tugas:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['judul']} - status: {task['status']}")

    try:
        # Meminta input user untuk nomor tugas
        pilihan = int(input("Masukkan nomor tugas yang ingin diubah statusnya: "))

        # Validasi nomor tugas
        if 1 <= pilihan <= len(tasks):
            task = tasks[pilihan - 1]

            print(f"Status saat ini: {task['status']}")

            # Tricky: toggle status antara 'Belum Selesai' <-> 'Selesai'
            if task["status"].lower() == "belum selesai":
                task["status"] = "Selesai"
            else:
                task["status"] = "Belum Selesai"

            # Update waktu terakhir diubah
            task["waktu_ubah"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            # Konfirmasi ke user
            print(f"✅ Status tugas '{task['judul']}' berhasil diubah menjadi: {task['status']}")
            print(f"📅 Waktu terakhir diubah: {task['waktu_ubah']}")
        else:
            print("⚠️ Nomor tugas tidak ditemukan.")
    except ValueError:
        # Input bukan angka
        print("⚠️ Input tidak valid, harap masukkan angka.")
        return
