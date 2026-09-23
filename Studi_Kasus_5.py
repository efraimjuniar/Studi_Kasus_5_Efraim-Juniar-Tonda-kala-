def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    """
    Menghitung total biaya parkir berdasarkan jenis kendaraan
    dan lama parkir (dalam jam).

    Tarif:
        Mobil : Rp5.000 / jam
        Motor : Rp3.000 / jam
    """
   
    if jenis_kendaraan.lower() == "mobil":
        tarif_per_jam = 5000
    elif jenis_kendaraan.lower() == "motor":
        tarif_per_jam = 3000
    else:
        print("Jenis kendaraan tidak dikenali! Gunakan 'Mobil' atau 'Motor'.")
        return 0

    total_biaya = lama_parkir * tarif_per_jam
    return total_biaya


jenis_kendaraan = input("Masukkan jenis kendaraan (Mobil/Motor): ")
jam_masuk = int(input("Masukkan jam masuk (contoh: 8): "))
jam_keluar = int(input("Masukkan jam keluar (contoh: 12): "))


lama_parkir = jam_keluar - jam_masuk
total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)


print("\n========== STRUK PARKIR ==========")
print(f"Jenis Kendaraan : {jenis_kendaraan}")
print(f"Jam Masuk       : {jam_masuk}:00")
print(f"Jam Keluar      : {jam_keluar}:00")
print(f"Lama Parkir     : {lama_parkir} jam")
print(f"Total Biaya     : Rp{total_biaya:,}")
print("===================================")