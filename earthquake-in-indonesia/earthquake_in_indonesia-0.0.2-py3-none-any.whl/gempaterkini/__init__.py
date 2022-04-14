import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 29 Maret 2022,
    Waktu: 05:56:49 WIB
    Magnitudo: 3.7
    Kedalaman: 1 km
    Lokasi: LS=3.85  - BT=122.83
Pusat Gempa: Pusat gempa berada di laut 20 km Timur Laut Soropia, Kab. Konawe
Dirasakan: Dirasakan (Skala MMI): II - III Kendari, II - III Konawe
    :return:
    """

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        kedalaman = None
        dirasakan = None
        lokasi = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2 :
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi == res.text
            elif i == 5:
                dirasakan == res.text

            i = i + 1



        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("tidak bisa menampilkan data terkini")
        return
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Koordinat = LS = {result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Dirasakan {result['dirasakan']}")


# if __name__ == '__main__':
   # print('ini adalah package gempa terkini')
   # print('hai')
if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)