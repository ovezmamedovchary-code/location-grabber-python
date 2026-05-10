import requests

# Test için daha kolay bir site seçelim (Örn: github)
target_user = input("Kontrol edilecek kullanıcı adı: ")
url = f"https://www.tiktok.com/@{target_user}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print(f"\n[*] {url} adresine bağlanılmaya çalışılıyor...")

try:
    # timeout=10 ekliyoruz ki internet yavaşsa sonsuza kadar beklemesin
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        print(f"\n[+] BAŞARILI: '{target_user}' kullanıcısı bulundu!")
    elif response.status_code == 404:
        print(f"\n[-] HATA: Kullanıcı bulunamadı (404).")
    else:
        print(f"\n[!] ENGEL: Siteye ulaşıldı ama kod: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("\n[X] BAĞLANTI HATASI: VPN açık olsa bile Python siteye ulaşamıyor.")
    print("İpucu: VPN'in 'Global Mode' veya 'TUN Mode' özelliğini açmayı dene.")
except Exception as e:
    print(f"\n[X] Beklenmedik bir hata oluştu: {e}")

input("\nÇıkmak için Enter'a basın...")
