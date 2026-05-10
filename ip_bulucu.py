import socket

# Hedefimizi belirliyoruz
hedef_site = "google.com"

try:
    print(f"[*] {hedef_site} adresi sorgulanıyor...")
    # Bu satır internetin telefon rehberine sorar: Google'ın IP'si ne?
    ip = socket.gethostbyname(hedef_site)
    
    print(f"\n--- ANALİZ SONUCU ---")
    print(f"Hedef Site: {hedef_site}")
    print(f"IP Adresi: {ip}")
    print("---------------------\n")
    print("[!] İlk siber aracın başarıyla çalıştı!")
except:
    print("[X] Hata: Bağlantı kurulamadı.")