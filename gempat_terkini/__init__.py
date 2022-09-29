import none as none
from bs4 import BeautifulSoup
import requests


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(',')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        pusat = None
        ket = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                pusat = res.text
            elif i == 5:
                ket = res.text
            i = i+1

        hasil = dict()
        hasil["tanggal"] = tanggal
        hasil["waktu"] = waktu
        hasil["magnitudo"] = magnitudo
        hasil["kedalaman"] = kedalaman
        hasil["koordinat"] = {"ls": ls, "bt": bt}
        hasil["pusat"] = pusat
        hasil["ket"] = ket
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak dapat Menemukan Data Gempa Terkini")
        return

    print('\nGempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi Koordinat: LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"Lokasi Gempa: {result['pusat']}")
    print(f"Keterangan: {result['ket']}")

# print("ini adalah PAckage Gempa Terkini\n")

# package init.py akan dieksekusi pertamakali sebelum main.py
# dengan syarat ada di paling kiri atau tanpa indentasi
# tetapi jika telah berbentuk fungsi atau if atau yang lainnya
# package init.py tidak akan dieksekusi