import os
import sys
import subprocess

def download_youtube(url, filetype, output_dir):
    try:
        if filetype == 'mp4':
            cmd = ['yt-dlp', '-f', 'best', '-P', output_dir, url]
        elif filetype == 'mp3':
            cmd = ['yt-dlp', '-x', '--audio-format', 'mp3', '-P', output_dir, url]
        else:
            print("❌ Invalid format. Use 'mp4' or 'mp3'.")
            return
        print(f"🔽 Downloading YouTube {filetype.upper()} to: {output_dir}")
        subprocess.run(cmd, check=True)
        print("✅ Download complete!\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ YouTube download failed: {e}")

def download_instagram(url, output_dir):
    try:
        cmd = ['yt-dlp', '-P', output_dir, url]
        print(f"🔽 Downloading Instagram video to: {output_dir}")
        subprocess.run(cmd, check=True)
        print("✅ Download complete!\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Instagram download failed: {e}")

def main():
    print("======== Mobile Video Downloader ========")
    print("1. Download from YouTube")
    print("2. Download from Instagram")
    choice = input("Enter your choice (1 or 2): ").strip()
    output_dir = "/data/data/com.termux/files/home/storage/downloads"
    print(f"Videos will be saved to: {output_dir}\n")
    if choice == '1':
        link = input("Enter YouTube video URL: ").strip()
        filetype = input("Enter format (mp4 or mp3): ").strip().lower()
        download_youtube(link, filetype, output_dir)
    elif choice == '2':
        link = input("Enter Instagram video URL: ").strip()
        download_instagram(link, output_dir)
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    print("Starting Mobile Video Downloader...\n")
    main()
