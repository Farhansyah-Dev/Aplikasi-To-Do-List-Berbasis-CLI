from datetime import datetime

def create_task(id_tugas: str, judul: str, deskripsi: str, deadline: str):
    """
    Factory function untuk membuat struktur data task baru
    dengan atribut lengkap sesuai standar aplikasi.
    """
    
    now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return {
        "id": id_tugas,  # ID unik tugas
        "judul": judul,  # Judul singkat tugas
        "deskripsi": deskripsi,  # Keterangan detail
        "status": "Belum Selesai",  # Status default selalu "Belum Selesai"
        "deadline": deadline,  # Deadline tugas
        "waktu_buat": now_str,  # Timestamp saat dibuat
        "waktu_ubah": now_str
    }
    