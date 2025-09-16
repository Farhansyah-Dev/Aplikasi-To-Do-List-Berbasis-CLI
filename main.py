import sys


from features.ViewTasks import lihat_semua_tugas
from features.addTasks import tambah_tugas

from features.StatusTasks import ubah_status
from features.DeleteTasks import hapus_tugas_with_warning
from data.dummy_data import tasks



def menu():
    print("\n=== Aplikasi To-Do List ===")
    print("1. Lihat semua tugas")
    print("2. Tambah tugas")
    print("3. Ubah status tugas")
    print("4. Hapus tugas")
    print("5. Keluar")

def main():
    while True:
        menu()
        pilihan = input("Masukkan pilihan anda: ").strip()

        if pilihan == "1":
            lihat_semua_tugas(tasks)
        elif pilihan == "2":
            tambah_tugas(tasks)
        elif pilihan == "3":
            ubah_status(tasks)
        elif pilihan == "4":
            hapus_tugas_with_warning(tasks)
        elif pilihan == "5":
            print('👋 Terimakasih sudah menggunakan Apps To-Do List.')
            sys.exit(0)
        else:
            print("⚠️ Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()









    







def exit():
    pass

def menu():
    print('Selamat Datang di Aplikasi To-Do List')
    print('1. Lihat semua tugas')
    print('2. Tambah Tugas')
    print('3. Status')
    print('4. Hapus Tugas')
    print('5. Keluar')

    
def main():
     while True:
        menu()
        choice = input('Masukan pilihan anda: ')
        
        if choice == '1':
            #Logika untuk menampilkan tugas
            lihat_semua_tugas(tasks)
            
        elif choice == '2':
            #Logika untuk menambahkan tugas
            tambah_tugas(tasks)
            
        elif choice == '3':
            #Logika untuk status
            ubah_status(tasks)
            
        elif choice == '4':
            #logika menghapus tugas
            hapus_tugas_with_warning(tasks)
            
        elif choice == '5':
            #Logika keluar aplikasi
            print('Terima kasih sudah menggunakan Aplikas To-Do List.')
            sys.exit(0)
        else:
            print('Pilihan tidak valid. Silahkan coba lagi')
    
if __name__=="__main__":
    main()