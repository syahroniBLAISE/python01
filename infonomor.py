import phonenumbers  #1
from phonenumbers import carrier, geocoder, timezone  #2
nomor_telepon = phonenumbers.parse('+628818527856')  #4
isp = carrier.name_for_number(nomor_telepon, 'en')  #5
zona_waktu = timezone.time_zones_for_number(nomor_telepon) #6
lokasi = geocoder.description_for_number(nomor_telepon, 'en')  #7
print(f"[+] Zona waktu : {zona_waktu}")  #8
print(f"[+] ISP : {isp}")  #9
print(f"[+] Lokasi : {lokasi}")  #10