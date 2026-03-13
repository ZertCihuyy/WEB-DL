# CIHUY WEB-DL v1.0

### The Ultimate Omniversal Downloader

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-green?style=for-the-badge&logo=ffmpeg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

CIHUY WEB-DL adalah script Python downloader yang menggunakan engine
**yt-dlp** untuk mengunduh berbagai media dari internet.\
Tool ini mendukung download **video, audio, hingga slideshow foto** dari
berbagai platform hanya dengan satu link.

Repository: https://github.com/ZertCihuyy/WEB-DL
:::

------------------------------------------------------------------------

# Kekuatan Utama

-   **Omniversal Download** -- Support YouTube, Bilibili, TikTok,
    Instagram, X/Twitter, Facebook, dan ribuan situs lain.
-   **Auto Dependency Installer** -- Script akan otomatis menginstal
    library yang dibutuhkan.
-   **JSON Subtitle’ SRT Converter** -- Mengubah subtitle JSON dari
    Inspect Element menjadi file `.srt`.
-   **Audio Extraction Mode** -- Ekstrak audio menjadi `.mp3` kualitas
    tinggi.
-   **Cookie Injector** -- Bypass batasan resolusi atau age restriction
    menggunakan cookie browser.

------------------------------------------------------------------------

# Requirements

Pastikan sistem kamu memiliki:

-   Python **3.8+**
-   **FFmpeg**
-   Internet connection

Download Python: https://www.python.org

------------------------------------------------------------------------

# Install FFmpeg

## Windows

Cara cepat:

``` cmd
winget install ffmpeg
```

Atau download manual dari: https://www.gyan.dev/ffmpeg/builds/

Tambahkan folder `bin` ke **Environment Variables PATH**.

------------------------------------------------------------------------

## Linux (Arch Linux / Manjaro)

``` bash
sudo pacman -S ffmpeg python python-pip
```

------------------------------------------------------------------------

## macOS

``` bash
brew install ffmpeg
```

------------------------------------------------------------------------

# Quick Install

Clone repository:

``` bash
git clone https://github.com/ZertCihuyy/WEB-DL
cd WEB-DL
python cihuy.py
```

------------------------------------------------------------------------

# Cara Penggunaan

Jalankan script:

```bash
python cihuy.py
```

Lalu:

1.  Masukkan link video
2.  Pilih mode download
3.  Tunggu proses selesai

Semua hasil download akan tersimpan di folder:

    downloads/

------------------------------------------------------------------------

# Cookie Injector

Beberapa situs memiliki pembatasan seperti:

-   Bilibili 1080p+
-   Video age restricted di YouTube
-   Konten login-only

Untuk bypass gunakan **cookies.txt**.

Langkah:

1.  Install extension **Get cookies.txt LOCALLY**
2.  Login ke situs target
3.  Export cookies
4.  Rename file menjadi:

```{=html}
<!-- -->
```
    cookies.txt

5.  Letakkan file di folder yang sama dengan `cihuy.py`

Jika berhasil akan muncul:

    >> Cookie berhasil dimuat!
    >> Mode Premium aktif

------------------------------------------------------------------------

# Supported Platforms

CIHUY WEB-DL menggunakan **yt-dlp** sehingga mendukung lebih dari
**1000+ website**, termasuk:

-   YouTube
-   TikTok
-   Bilibili
-   Instagram
-   Facebook
-   X / Twitter
-   Reddit
-   Vimeo

------------------------------------------------------------------------

# Kontributor

**Zerty\_ (ZertCihuyy)**\
Backend Developer / Automator

GitHub: https://github.com/ZertCihuyy

YouTube: https://youtube.com/@Zertcihuy

------------------------------------------------------------------------

# Star Repository

Jika project ini membantu kamu, jangan lupa beri **Star** di repository:

https://github.com/ZertCihuyy/WEB-DL

Dukungan kamu membantu project ini berkembang.

------------------------------------------------------------------------

# License

Project ini menggunakan **MIT LiceLicen
