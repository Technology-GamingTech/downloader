import subprocess
import os
import sys
import tkinter as tk
from tkinter import filedialog

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
    print("======== Video Downloader ========")
    print("1. Download from YouTube")
    print("2. Download from Instagram")
    choice = input("Enter your choice (1 or 2): ").strip()

    # Detect if running on Termux/mobile or PC
    is_termux = False
    if sys.platform.startswith("linux") and "com.termux" in os.environ.get("PREFIX", ""):
        is_termux = True
    elif "ANDROID_ROOT" in os.environ or "ANDROID_DATA" in os.environ:
        is_termux = True

    if is_termux:
        output_dir = input("Enter the full path to the folder where you want to save the video: ").strip()
        if not output_dir or not os.path.isdir(output_dir):
            print("❌ Invalid or no folder provided. Exiting.")
            return
    else:
        root = tk.Tk()
        root.withdraw()
        output_dir = filedialog.askdirectory(title="Select folder to save the video")
        root.destroy()
        if not output_dir:
            print("❌ No folder selected. Exiting.")
            return
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
    print("Starting Video Downloader...\n")
    main()
