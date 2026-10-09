import os
import sys
import time

def mulai_visual_kode():
    print("Menginisialisasi sistem... (Menggunakan murni aliran teks, tanpa video)")
    print("Mengambil database frame teks Bad Apple...")
    
    # Kode ini akan otomatis menginstal paket ASCII murni bernama 'badapple'
    # Paket ini tidak menggunakan .mp4, melainkan menggunakan susunan teks yang dikompres
    os.system(f"{sys.executable} -m pip install badapple --quiet")
    
    time.sleep(1)
    
    # Membersihkan layar terminal agar bersih (mendukung Windows dan Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Menjalankan pemutar teks Bad Apple langsung di terminal Anda
    os.system("badapple")

if __name__ == "__main__":
    mulai_visual_kode()
