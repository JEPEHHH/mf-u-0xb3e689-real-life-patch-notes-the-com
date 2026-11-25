# Rencana Kerja: Real-Life Patch Notes: The Comedy Changelog

## Ringkasan Tugas
Membuat program `program/v1` yang menulis satu baris *software patch note* komedi tentang bug kehidupan nyata/biologi manusia (maks. 160 karakter UTF-8) ke `/output/entry.txt`. Penilaian dilakukan secara *pairwise* oleh juri AI berdasarkan: kecocokan format & tema, kelucuan langsung (*first-read punch*), gaya *release note* otentik (versi + nada teknis kering), spesifisitas bug sehari-hari/tubuh, serta efisiensi karakter (*tie-break* pada ukuran byte lebih kecil).

## Langkah Kerja
1. **Inisialisasi & Lisensi**
   - Tambahkan berkas `LICENSE` (MIT) sesuai syarat lisensi OSI kompetisi.
   - Commit milestone inisialisasi.
2. **Eksplorasi & Seleksi Kandidat Patch Note**
   - Rancang beberapa kandidat *one-line patch note* dengan format versi (`vX.Y.Z:`), register teknis kering, bug tubuh/harian yang sangat spesifik, dan punchline tajam tanpa padding.
   - Evaluasi silang antar kandidat terhadap 5 kriteria juri secara berurutan, lalu pilih kandidat terkuat dengan jumlah byte efisien.
3. **Implementasi Entrypoint (`main.py`)**
   - Buat `main.py` (runtime `python3.13`, tanpa dependensi eksternal/jaringan) yang memastikan direktori `/output` ada dan menulis teks final ke `/output/entry.txt` dalam UTF-8.
   - Commit milestone implementasi awal.
4. **Iterasi & Penyempurnaan Teks**
   - Lakukan revisi terukur pada `main.py` untuk menajamkan diksi, ritme komedi, dan efisiensi byte (memenuhi syarat revisi kode).
   - Commit milestone penyempurnaan.
5. **Verifikasi Lokal & Finalisasi**
   - Buat dan jalankan `verify.py` untuk memvalidasi gate: file `/output/entry.txt` terbentuk, UTF-8 valid, tepat 1 baris, panjang 1–160 karakter, non-whitespace, dan deterministik.
   - Lengkapi `README.md` dan pastikan status git bersih serta siap diperiksa.

## Daftar Berkas yang Akan Dibuat
- `PLAN.md` — Rencana kerja dan daftar berkas (berkas ini).
- `LICENSE` — Lisensi MIT (OSI-approved) wajib untuk submisi.
- `main.py` — Program entrypoint `program/v1` yang menghasilkan `/output/entry.txt`.
- `verify.py` — Skrip pengujian lokal untuk memeriksa kepatuhan gate dan batasan karakter/byte.
- `README.md` — Dokumentasi singkat cara menjalankan dan memverifikasi entri.
