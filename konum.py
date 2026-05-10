import folium

# Bu koordinatları bir API'den veya izinle aldığını varsayalım
enlem = 37.9500 # Örnek Aşkabat enlemi
boylam = 58.3833 # Örnek Aşkabat boylamı

# Haritayı oluştur
harita = folium.Map(location=[enlem, boylam], zoom_start=15)

# Konuma bir işaretçi (marker) ekle
folium.Marker([enlem, boylam], popup="Hedef Konum").add_to(harita)

# Haritayı kaydet
harita.save("konum_detay.html")

print("Harita 'konum_detay.html' olarak kaydedildi. Tarayıcında açabilirsin.")