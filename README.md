# Studi_Kasus_5_Efraim-Juniar-Tonda-kala-

Nama : Efraim Juniar Tonda Kala'

NIM : 2609116064

**Kode function:**
Program ini saya buat untuk menghitung biaya parkir kendaraan, baik itu mobil ataupun motor, berdasarkan berapa lama kendaraannya parkir. Tarifnya beda-beda: mobil Rp5.000 per jam, motor Rp3.000 per jam.

Di bagian ini saya bikin satu function khusus yang tugasnya hanya buat menghitung biaya. Function ini menerima dua data: jenis kendaraannya apa, dan berapa lama parkirnya (dalam jam).

Buat menentukan tarifnya, saya pakai if/elif — kalau kendaraannya "mobil" tarifnya 5000/jam, kalau "motor" tarifnya 3000/jam. Kalau ternyata user mengetik selain dua itu, programnya akan kasih tau kalau jenis kendaraannya tidak dikenali, terus balikin 0 (biar tidak error pas dihitung).

Setelah tarifnya ketemu, akan dikali dengan lama parkirnya buat dapat total biaya, lalu di-return supaya angkanya bisa dipakai lagi di luar function.

<img width="327" height="208" alt="image" src="https://github.com/user-attachments/assets/f6b73d50-1c91-435c-9919-1758ef9e1c15" />

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
**Kode program utama:**
di bagian ini saya minta user masukkan jenis kendaraan, jam masuk, dan jam keluar. Dari situ saya hitung dulu selisihnya buat dapat lama parkir (jam keluar dikurangi jam masuk) — ini sengaja saya taruh di luar function, jadi function-nya tidak perlu tau soal jam masuk/keluar, cukup terima hasil lama parkirnya aja.

Setelah itu baru saya panggil function-nya, passing jenis kendaraan dan lama parkir tadi, dan hasilnya (total biaya) saya simpan ke variabel total_biaya.

Terakhir, semua informasinya saya tampilkan dalam bentuk struk — jenis kendaraan, jam masuk, jam keluar, lama parkir, sampai total biaya yang harus dibayar.

<img width="276" height="165" alt="image" src="https://github.com/user-attachments/assets/b6a98dd4-e428-4f6e-b851-a466c2ea40e7" />

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**HASIL OUTPUT:**

<img width="195" height="112" alt="image" src="https://github.com/user-attachments/assets/5dba2f80-98c7-4f32-b775-f9db254a9d24" />
