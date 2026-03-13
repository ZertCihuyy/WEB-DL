import os
import sys
import subprocess
import platform
import json
import urllib.request
import http.cookiejar
import re
import time

# ==========================================
# 🌀 KUCHIYOSE NO JUTSU: AUTO INSTALLER 🌀
# ==========================================
def install_dependencies():
    """Auto-install modul yang kurang, cross-platform!"""
    required_packages = {
        "yt_dlp": "yt-dlp", 
        "questionary": "questionary", 
        "rich": "rich"
    }
    
    needs_restart = False
    for module_name, pip_name in required_packages.items():
        try:
            __import__(module_name)
        except ImportError:
            print(f"[*] Mengeksekusi summoning jutsu untuk {pip_name}...")
            # Otomatis menyesuaikan dengan OS (Windows/Linux/Mac)
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name, "--quiet", "--upgrade"])
            needs_restart = True

    if needs_restart:
        print("[!] Semua dependensi berhasil di-summon! Merestart program...\n")
        os.execv(sys.executable, ['python'] + sys.argv)

install_dependencies()

# Import setelah dipastikan terinstall
import yt_dlp
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()
COOKIE_FILE = "cookies.txt"

# ==========================================
# 🛡️ SYSTEM UTILITIES 🛡️
# ==========================================
def clear_screen():
    """Mendeteksi OS dan membersihkan layar layaknya sihir pembersih."""
    current_os = platform.system().lower()
    if current_os == "windows":
        os.system('cls')
    else:
        os.system('clear')

def check_ffmpeg():
    """Mendeteksi apakah FFmpeg terinstall (Penting untuk merge video/audio)."""
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def display_header():
    clear_screen()
    header_text = """
 ██████╗██╗██╗  ██╗██╗   ██╗██╗   ██╗
██╔════╝██║██║  ██║██║   ██║╚██╗ ██╔╝
██║     ██║███████║██║   ██║ ╚████╔╝ 
██║     ██║██╔══██║██║   ██║  ╚██╔╝  
╚██████╗██║██║  ██║╚██████╔╝   ██║   
 ╚═════╝╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   
 ██╗    ██╗███████╗██████╗     ██████╗ ██╗     
 ██║    ██║██╔════╝██╔══██╗    ██╔══██╗██║     
 ██║ █╗ ██║█████╗  ██████╔╝    ██║  ██║██║     
 ██║███╗██║██╔══╝  ██╔══██╗    ██║  ██║██║     
 ╚███╔███╔╝███████╗██████╔╝    ██████╔╝███████╗
  ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═════╝ ╚══════╝
    [ v1.0 - OMNIVERSAL EDITION (ALL PLATFORM) ]
    [ Supports: Bilibili, TikTok, YouTube, DLL ]
    """
    console.print(Panel(Text(header_text, style="bold cyan", justify="center"), border_style="bold magenta"))
    
    # Deteksi OS dan FFmpeg status
    os_name = platform.system()
    ffmpeg_status = "[bold green]Terdeteksi[/bold green]" if check_ffmpeg() else "[bold red]Tidak Terdeteksi (Beberapa format mungkin gagal di-merge)[/bold red]"
    console.print(f"[dim]OS Aktif: {os_name} | Status FFmpeg: {ffmpeg_status}[/dim]\n")

# ==========================================
# 🍪 SKILL: COOKIE INJECTOR 🍪
# ==========================================
def setup_cookie_opener():
    cj = http.cookiejar.MozillaCookieJar(COOKIE_FILE)
    if os.path.exists(COOKIE_FILE):
        try:
            cj.load(ignore_discard=True, ignore_expires=True)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            urllib.request.install_opener(opener)
            console.print("[dim green]>> Cookie berhasil dimuat! Mode Premium aktif.[/dim green]")
            return True
        except Exception:
            console.print("[dim red]>> Cookie gagal dimuat. Berjalan di mode Normal.[/dim red]")
            pass
    return False

# ==========================================
# 📜 SKILL: BILIBILI JSON TO SRT TRANSMUTER
# ==========================================
def format_time_srt(seconds_float):
    hours = int(seconds_float // 3600)
    minutes = int((seconds_float % 3600) // 60)
    seconds = int(seconds_float % 60)
    milliseconds = int(round((seconds_float - int(seconds_float)) * 1000))
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def download_and_convert_json_sub(url):
    os.makedirs('downloads/subs', exist_ok=True)
    filename = f"downloads/subs/Bilibili_Sub_{int(time.time())}.srt"
    
    console.print("[bold yellow]Memproses URL JSON Subtitle Asli...[/bold yellow]")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
        subtitles = data.get('body', [])
        if not subtitles:
            console.print("[bold red]Data 'body' tidak ditemukan di JSON.[/bold red]")
            return

        with open(filename, 'w', encoding='utf-8') as f:
            for index, sub in enumerate(subtitles, start=1):
                start_time = format_time_srt(sub['from'])
                end_time = format_time_srt(sub['to'])
                text = sub['content'].replace('\n', ' ')
                
                f.write(f"{index}\n")
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"{text}\n\n")
                
        console.print(f"\n[bold cyan]✨ TRANSMUTASI BERHASIL! ✨[/bold cyan]")
        console.print(f"[bold green]File SRT siap tempur disimpan di: {filename}[/bold green]")
        
    except Exception as e:
        console.print(f"[bold red]Gagal memproses JSON: {e}[/bold red]")

# ==========================================
# 👁️ SKILL: OMNI-SCANNER (YT-DLP) 👁️
# ==========================================
def get_media_info(url):
    ydl_opts = {'quiet': True, 'no_warnings': True}
    if os.path.exists(COOKIE_FILE):
        ydl_opts['cookiefile'] = COOKIE_FILE
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            return ydl.extract_info(url, download=False)
        except Exception as e:
            console.print(f"[bold red]Gagal memindai: {e}[/bold red]")
            return None

# ==========================================
# 🚀 MAIN EXECUTION 🚀
# ==========================================
def main():
    display_header()
    has_cookie = setup_cookie_opener()
    
    url = questionary.text("🔗 Masukkan Link (Video / Foto / TikTok / Bilibili / F12 JSON):").ask()
    if not url:
        return

    # AUTO-ROUTER: Tangkap link F12 Bilibili Subtitle
    if 's.bstarstatic.com' in url or url.endswith('.json') or 'auth_key=' in url:
        console.print("\n[bold cyan]👁️ Byakugan mendeteksi: DIRECT LINK JSON SUBTITLE (F12)![/bold cyan]")
        download_and_convert_json_sub(url)
        return

    # LOGIKA MEDIA NORMAL (Video / Foto / Audio)
    resolutions = []
    is_playlist = False
    
    with console.status("[bold cyan]👁️ Memindai metadata dari isekai...[/bold cyan]", spinner="aesthetic"):
        info = get_media_info(url)
        if info:
            if 'entries' in info:
                is_playlist = True
                console.print(f"[bold magenta]📚 Playlist/Slideshow terdeteksi: {len(list(info['entries']))} item![/bold magenta]")
            
            formats = info.get('formats', [])
            res_set = set(f.get('height') for f in formats if f.get('height'))
            resolutions = sorted(list(res_set), reverse=True)

    if not info:
        console.print("[bold red]Gagal. Pastikan link valid dan dapat diakses.[/bold red]")
        return

    title_text = info.get('title', 'Unknown Media')
    console.print(f"\n[bold green]📌 Target Terkunci:[/bold green] {title_text}")

    # Pilihan Kualitas
    res_choices = [f"{r}p" for r in resolutions] if resolutions else []
    res_choices = ["Terbaik (Auto-Best)"] + res_choices + ["Hanya Audio (MP3)"]
    
    res_choice = questionary.select("📺 Pilih Resolusi / Format:", choices=res_choices).ask()

    # Setup yt-dlp Options
    os.makedirs('downloads', exist_ok=True)
    ydl_opts = {
        'outtmpl': 'downloads/%(playlist_title)s/%(title)s.%(ext)s' if is_playlist else 'downloads/%(title)s.%(ext)s',
        'concurrent_fragment_downloads': 10,
        'writethumbnail': True, # Sedot gambar thumbnail/cover art
    }

    if has_cookie:
        ydl_opts['cookiefile'] = COOKIE_FILE

    # Logika Format Download
    if res_choice == "Hanya Audio (MP3)":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }, {'key': 'EmbedThumbnail'}]
        })
    elif res_choice == "Terbaik (Auto-Best)":
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mkv',
            'postprocessors': [{'key': 'FFmpegMetadata'}, {'key': 'EmbedThumbnail'}]
        })
    else:
        height = res_choice.replace('p', '')
        ydl_opts.update({
            'format': f'bestvideo[height<={height}]+bestaudio/best',
            'merge_output_format': 'mkv',
            'postprocessors': [{'key': 'FFmpegMetadata'}, {'key': 'EmbedThumbnail'}]
        })

    # Jika targetnya TikTok Foto (Slideshow), yt-dlp otomatis menanganinya jika format best dipilih.
    if questionary.confirm("🔥 Lepaskan segel dan mulai unduh?").ask():
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            console.print("\n[bold cyan]✨ MISSION ACCOMPLISHED! File aman di folder 'downloads'. ✨[/bold cyan]")
        except Exception as e:
            console.print(f"\n[bold red]FATAL ERROR: {e}[/bold red]")
            console.print("[dim]Tips: Jika error terkait 'merge', pastikan FFmpeg terinstall di OS kamu![/dim]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]🛑 Operasi dibatalkan secara paksa! Sayonara![/bold red]")
