import subprocess
import os

def download_youtube(url, filetype):
    try:
        if filetype == 'mp4':
            cmd = ['yt-dlp', '-f', 'best', url]
        elif filetype == 'mp3':
            cmd = ['yt-dlp', '-x', '--audio-format', 'mp3', url]
        else:
            print("❌ Invalid format. Use 'mp4' or 'mp3'.")
            return

        print(f"🔽 Downloading YouTube {filetype.upper()}...")
        subprocess.run(cmd, check=True)
        print("✅ Download complete!\n")

    except subprocess.CalledProcessError as e:
        print(f"❌ YouTube download failed: {e}")

def download_instagram(url):
    try:
        # This downloads Instagram video or reel
        cmd = ['yt-dlp', url]
        print("🔽 Downloading Instagram video...")
        subprocess.run(cmd, check=True)
        print("✅ Download complete!\n")

    except subprocess.CalledProcessError as e:
        print(f"❌ Instagram download failed: {e}")

def main():
    print("======== Video Downloader ========")
    print("1. Download from YouTube")
    print("2. Download from Instagram")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        link = input("Enter YouTube video URL: ").strip()
        filetype = input("Enter format (mp4 or mp3): ").strip().lower()
        download_youtube(link, filetype)

    elif choice == '2':
        link = input("Enter Instagram video URL: ").strip()
        download_instagram(link)

    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    print("Starting Video Downloader...\n")
    main()
