import os
from pytube import YouTube
from pydub import AudioSegment

def download_song():
    #downloads the song from youtube in mp4 format
    video_to_download = input('insert the link of the youtube song that you want to download: ')
    print(video_to_download)
    YouTube(video_to_download).streams.first().download()
    yt = YouTube(video_to_download)
    global video
    video= yt.streams.filter(progressive=True, file_extension='mp4').first()
    destination = "temp_audio"

def file_conversion():
    #converts the file into mp3 format
    global out_file
    out_file = video.download(output_path="destination path")
    base, ext = os.path.splitext(out_file)
    audio = AudioSegment.from_file(out_file)
    mp3_file = base + '.mp3'
    audio.export(mp3_file,format='mp3')

def remove_mp4():
    #deletes the original mp4 file
    os.remove(out_file)

def repeat():
    #asks if you want to download more songs
    question = input('do you want to download another song? Yes/No? ' )
    if question == 'yes':
        youtube_download()
    else:
        exit()

def youtube_download():
    download_song()
    file_conversion()
    remove_mp4()
    repeat()

youtube_download()
