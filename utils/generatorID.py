import random
# Fungsi untuk generate ID: 3 digit acak + index terakhir
def generate_task_id(index):
    
    """
    Fungsi untuk membuat ID tugas.
    ID terdiri dari 3 digit 3 angka acak + nomor urut tugas (index + 1).
    contoh hasil: "4821", "3052", dll.
    
    args
    """
    
    # Buat angka random 3 digit (100 - 999)
    random_part = random.randint(100, 999)
    # Gabungkan angka acak dengan index+1 (supaya dimulai dari 1, bukan 0).
    # ID dikembalikan dalam bentuk string agar konsisten (misalnya "1231").
    return f"{random_part}{index + 1}" #ditambahkan 1 agar dimulai dari 1