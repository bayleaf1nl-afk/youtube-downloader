import yt_dlp
import os
import sys
print(sys.argv)

ffmpeg_path = "/usr/bin/ffmpeg"


ydl_opts = {
    'postprocessors':
    [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0',
    }],
    'ffmpeg_location': ffmpeg_path,           
    'outtmpl': '%(title)s.%(ext)s',             
    'quiet': False,                             
    'noplaylist': True                           
}

while True:
    if input("download videos? y/n").lower() != 'y': break;
    try: 
        numVideos = int(input("how many?"));
    except:
        print("dumbass");
        continue;
    video_urls = [input("gimme") for _ in range(numVideos)];
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for video in video_urls:
            ydl.download([video]);
