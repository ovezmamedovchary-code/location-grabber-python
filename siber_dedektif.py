import requests

def platform_kontrol(platform_ismi, url, headers):
    try:
        # 5 saniyelik zaman aşımı (timeout) ekledik
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            return f"[+] {platform_ismi}: BULUNDU! ({url})"
        elif response.status_code == 404:
            return f"[-] {platform_ismi}: Bulunamadı."
        else:
            return f"[!] {platform_ismi}: Engel/Hata (Kod: {response.status_code})"
    except:
        return f"[X] {platform_ismi}: Bağlantı kurulamadı."

print("========================================")
print("     OSINT - DİJİTAL AYAK İZİ TAKİBİ     ")
print("========================================")

user = input("Sorgulanacak Kullanıcı Adı: ")

# Tarayıcı gibi görünmek için Header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# Platform listesi ve adresleri
siteler = {
    "TikTok": f"https://www.tiktok.com/@{user}",
    "GitHub": f"https://github.com/S{user}",
    "Instagram": f"https://www.instagram.com/{user}/",
    "YouTube": f"https://www.youtube.com/@{user}"
}

print(f"\n[*] '{user}' için tarama başlatılıyor...\n")

for isim, link in siteler.items():
    sonuc = platform_kontrol(isim, link, headers)
    print(sonuc)

print("\n========================================")
input("Çıkmak için Enter'a basın...")
