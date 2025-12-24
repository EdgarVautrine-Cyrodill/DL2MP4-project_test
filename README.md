# 📥 DL2MP4 (Video Downloader & File Converter)
DL2MP4 adalah website yang berbasis **Flask (Python)** yang menyediakan fitur:
1. **Download & Convert Video** dari YouTube.
2. **MP4** dengan pilihan resolusi.
3. Support **MP3**.
4. **Konversi File DOCX ke PDF** (Experimental)

Project ini dibuat untuk pengguna yang akan mengunduh video favorite dari platform terkenal dan menyimpannya secara offline.

---

## 🚀 Fitur Utama
1. Mengunduh Video dari berbagai website (Youtube, Facebook, Instagram)
2. Pilihan MP3
3. MP4 Support resolusi (Memilih AUTO akan mengakitbatkan video yang diunduh menjadi UHD.)
4. Convert .docx ke .pdf
### 🎬 Video Download
- Download video dari YouTube
- Pilihan format:
  - MP4 (Video + Audio) 
  - MP3 (Audio saja)
- Pilihan resolusi:
  - Auto
  - 1080p
  - 720p
  - 480p
- Output MP4 (bukan WebM)
- Menggunakan **yt-dlp + FFmpeg**

### 📄 DOCX to PDF Converter (Experimental)
- Upload file `.docx`
- Konversi ke `.pdf`
- File PDF di-generate otomatis
- Menggunakan **python-docx** & **ReportLab**

---

## 🛠️ Tools & Library yang Digunakan

- **Python 3**
- **Flask**
- **yt-dlp**
- **FFmpeg**
- **python-docx**
- **ReportLab**
- **HTML, CSS, JavaScript (Frontend)**

---

## 📂 Struktur Folder Project

project/ │ 
├── app.py 
├── requirements.txt │ 
├── templates/ │   
  └── index.html │
├── static/ │   
├── css/ │   
└── js/ │ 
├── downloads/  # hasil video / audio 
├── uploads/  # file DOCX 
├── converted/  # hasil PDF

---

## ⚙️ Instalasi & Menjalankan Project

### 1️⃣ Clone / Extract Project
```bash
git clone https://github.com/EdgarVautrine-Cyrodill/DL2MP4-project_test
git pull
```
Atau extract file ZIP:
1. Klik <> Code
2. Download ZIP

---

## 2️⃣ Install Dependency
```python
pip install flask yt-dlp python-docx reportlab
```

---

## 3️⃣ Install FFmpeg

Download FFmpeg (Windows)

Extract

Pastikan path FFmpeg sesuai di app.py:

```python
ffmpeg_location = r'C:\ffmpeg\bin'
```

---

## 4️⃣ Jalankan Aplikasi
```python
python app.py
```
Buka browser:
```Firefox, Chrome, Edge, Opera, Brave, LibreWolf, Waterfox, Floorp
http://127.0.0.1:5000
```

---

## 🔁 Alur Kerja Aplikasi

**Video Downloader**

1. User memasukkan URL video.

2. (MP4) Memilih resolusi.

3. Data dikirim ke backend (/download).

4. yt-dlp & ffmpeg memproses video.

5. File disimpan ke folder downloads.



**DOCX to PDF**

1. User upload file .docx

2. File disimpan di uploads

3. Dibaca menggunakan python-docx

4. PDF dibuat menggunakan ReportLab

5. File PDF disimpan di converted


---

## ❗ Catatan Penting

Pastikan **FFmpeg** sudah ter-install

Jika hasil download berupa .webm, pastikan:

Format dipaksa mp4 & Resolusi diproses di backend

Gunakan koneksi internet stabil saat download video


---
📌 Lisensi

Project ini dibuat untuk keperluan edukasi dan pembelajaran.
