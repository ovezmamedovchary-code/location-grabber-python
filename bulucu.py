import requests
import time

def kontrol_et(isim, platformlar, headers):
    # Boşlukları ve büyük harfleri temizle
    isim = isim.lower().replace(" ", "")
    print(f"\n[>>>] '{isim}' taranıyor...")
    
    for platform, url_taslagi in platformlar.items():
        url = url_taslagi.format(user=isim)
        try:
            time.sleep(0.4) # Ban yememek için bekleme
            response = requests.get(url, headers=headers, timeout=5)
            
            if response.status_code == 200:
                print(f"  [+] {platform}: BULUNDU! -> {url}")
        except:
            pass

# --- AYARLAR ---
ad = input("Hedef kişinin adı (Örn: nur): ").strip().lower()
soyad = input("Varsa soyadı (Yoksa boş bırak): ").strip().lower()

# Olasılıkları burada türetiyoruz
kombinasyonlar = set()
kombinasyonlar.add(ad) # nur

ekler = ["1", "12", "01", "2011", "vips", "off", "_", "x", "real"]

for ek in ekler:
    kombinasyonlar.add(ad + ek)        # nur1, nurvips
    kombinasyonlar.add(ek + ad)        # xnur, realnur
    if soyad:
        kombinasyonlar.add(ad + soyad) # nurkaya
        kombinasyonlar.add(ad + "_" + soyad) # nur_kaya
        kombinasyonlar.add(ad[0] + soyad)    # nkaya (ismin ilk harfi + soyad)

siteler = {
    "TikTok": "https://www.tiktok.com/@{user}",
    "Instagram": "https://www.instagram.com/{user}/",
    "GitHub": "https://github.com/{user}",
    "YouTube": "https://www.youtube.com/@{user}"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

print(f"\n[*] Toplam {len(kombinasyonlar)} farklı olasılık denenecek...")

for aday in kombinasyonlar:
    if len(aday) > 2: # Çok kısa isimleri tarama (hata payı yüksek olur)
        kontrol_et(aday, siteler, headers)

print("\n[*] Tarama bitti.")
input("Kapatmak için Enter'a basın...")