import os
import sys
import shutil
import argparse

global args
print(sys.argv)
def argparsers():
    parser = argparse.ArgumentParser(description="download YouTube videos as mp3")
    parser.add_argument("urls", nargs='+', help="one or more youtube URLs")
    parser.add_argument("--playlist", action="store_true", default=False, help="allow playlist downloads")
    parser.add_argument("--quality", "-q", default=0, help="mp3 quality (0 best, 9 worst)")
    parser.add_argument("--outputLocation", "--o", default='%(title)s.%(ext)s', help="where to output the files?")
    parser.add_argument("--verbose", "-v", default=False, action="store_true", help="do you want the program to list everything it runs?")
    args = parser.parse_args()
    return args
def main():
    ffmpeg_path = shutil.which("ffmpeg")
    if (ffmpeg_path is None):
        print("ffmpeg not found! install it before you run this script & ensure its in your PATH.")
        if(os.name=="nt"): 
            print("""for Windows, try using Chocolatey in your Powershell: choco install ffmpeg
                    or simply install it from the official website: https://www.ffmpeg.org/""")
        
        else: print
        (
            """
        for Unix-like operating systems, try using MacPorts, Homebrew (if on MacOS)
        or your favorite linux package manager: 
        sudo port install ffmpeg
        brew install ffmpeg
        sudo apt install ffmpeg
        sudo pacman -S ffmpeg  
            """
        )
        sys.exit(1)
    try:
        import yt_dlp
    except ModuleNotFoundError:
        print("yt_dlp is not installed. install it with: pip install yt_dlp")
        sys.exit(1)
    
    args = argparsers()

    ydl_opts = {
    'postprocessors':
    [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': args.quality,
    }],
    'ffmpeg_location': ffmpeg_path,           
    'outtmpl': args.outputLocation,             
    'quiet': args.verbose,                             
    'noplaylist': args.playlist                           
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for video in args.urls:
            ydl.download([video]);



if __name__ == "__main__":
    main()