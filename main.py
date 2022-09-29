"""
Aplikasi Deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 28 September 2022
    Waktu: 12:44:25 WIB
    Magnitudo: 3.1
    Kedalaman: 11 km
    Lokasi: 5.25 LS - 122.03 BT
    Pusat gempa: berada di darat 7 km Barat Laut Kabaena Timur
    Keterangan: Dirasakan (Skala MMI): II - III Kabaena Timur
    :return:
    """
    hasil = dict()
    hasil["tanggal"] = "28 September 2022"
    hasil["waktu"] = "12:44:25 WIB"
    hasil["magnitudo"] = 3.1
    hasil["lokasi"] = {"ls": 5.25, "bt": 122.03}
    hasil["pusat"] = "Berada di darat 7 Km Barat Laut Kabaena Timur"
    hasil["ket"] = "Dirasakan (Skala MMI): II-III Kabanea Timur"

    return hasil


def tampilkan_data(result):
    print('\nGempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Lokasi: LS = {result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Pusat Gempa: {result['pusat']}")
    print(f"Keterangan: {result['ket']}")
    # print(result)


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)