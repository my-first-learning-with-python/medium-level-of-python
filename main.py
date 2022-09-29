"""
Aplikasi Deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
Modularisasi Dengan Package
"""
# from gempat_terkini import tampilkan_data, ekstraksi_data
import gempat_terkini

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempat_terkini.ekstraksi_data()
    gempat_terkini.tampilkan_data(result)
