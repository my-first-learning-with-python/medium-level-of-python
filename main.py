"""
Aplikasi Deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
Modularisasi Dengan Package
"""
# from gempat_terkini import tampilkan_data, ekstraksi_data
import latestearthquake

if __name__ == '__main__':
    print('~~~Live Earthquake Application~~~')
    result = latestearthquake.ekstraksi_data()
    latestearthquake.show_data(result)
