<<<<<<< HEAD
# Aplikasi-To-Do-List-Berbasis-CLI
=======
# 📝 To-Do List Application

Aplikasi sederhana untuk mencatat, mengubah, dan menghapus tugas sehari-hari. Cocok untuk mahasiswa baru belajar Python.

## 📌 Deskripsi Proyek

<b>Tujuan proyek:</b>

Membantu mahasiswa baru memahami konsep dasar Python: fungsi, list, dictionary, modul, input/output, dan unit testing.

Fitur Utama:

➕ Menambahkan tugas baru

📋 Menampilkan semua tugas

✅ Mengubah status tugas

🗑 Menghapus tugas dengan konfirmasi

📅 Validasi tanggal deadline dan ID unik

## 📁 Struktur Folder
├── features/        # Semua fitur aplikasi
│   ├── addTasks.py
│   ├── DeleteTasks.py
│   ├── StatusTasks.py
│   └── ViewTasks.py
├── models/          # Struktur data tugas
│   └── tasksModel.py
├── utils/           # Fungsi pembantu
│   ├── generatorID.py
│   └── validate.py
├── data/            # Menyimpan data tugas (list kosong)
├── test/            # Semua test script untuk unit testing
├── README.md        # Dokumentasi proyek

## ⚙️ Persiapan & Instalasi

Pastikan Python versi 3.10+ terinstal

Clone repository:

git clone <repository-url>


Masuk ke folder proyek:

cd <nama-folder>


Jalankan aplikasi:

python main.py

## 🛠 Cara Menggunakan

<b>1. Menambahkan tugas:</b>

Masukkan judul tugas: Belajar Python
Masukkan deskripsi tugas: Modul Pengenalan
Masukkan deadline (DD/MM/YYYY): 20/09/2025
✅ Tugas 'Belajar Python' berhasil ditambahkan


<b>2. Menampilkan semua tugas:</b>

📋 Daftar Tugas:
1. Belajar Python | Status: Belum Selesai


<b>3. Mengubah status tugas:</b>

Masukkan nomor tugas yang ingin diubah statusnya: 1
✅ Status tugas 'Belajar Python' berhasil diubah menjadi: Selesai
📅 Waktu terakhir diubah: 16/09/2025 10:00:00


<b>4. Menghapus tugas:</b>

Masukan nomor tugas yang ingin dihapus: 1
⚠️ Tugas 'Belajar Python' belum selesai. Yakin mau hapus? (y/n): y
✅ Tugas 'Belajar Python' berhasil dihapus


## 💡 Catatan Khusus

Semua fungsi terdokumentasi menggunakan docstring

Inline comment hanya untuk logika tricky

Cocok untuk belajar struktur proyek, modularisasi, testing, dan dokumentasi yang baik

## 🤝 Kontribusi

Fork repo

Buat fitur baru / perbaiki bug

Pull request diterima dengan senang hati 🎉

## 📄 Lisensi

MIT License atau sesuai kebutuhan

