# import modul datetime untuk memproses tanggal
from datetime import datetime

# Fungsi untuk mendapatkan tanggal sekarang dalam format DD/MM/YYYY
def validate_deadline(deadline: str) -> bool:
    
    """
    Memvalidasi input tanggal deadline dari user.
    Aturan validasi:
        - format haru DD/MM/YYYY
        - Tidak boleh tanggal dimasa lalu 
        
    args:
        deadline str: tanggal deadline dalam format DD/MM/YYYY
        

    Returns:
        bool: True jika valid, False jika tidak valid
    """ 
    
    try:
        # konversi string menjadi object datetime sesuai format
        deadline_date = datetime.strptime(deadline, "%d/%m/%Y")
        
        # ambil tanggal hari ini, set jam/menit/detik ke 0 supaya bandingkan tanggal
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        #deadline valid jika sama atau setelah hari ini
        return deadline_date >= today
    except ValueError:
        # jika format salah langsung return false
        return False
