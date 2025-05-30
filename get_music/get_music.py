import os
from pytubefix import YouTube
from pydub import AudioSegment
AudioSegment.converter = "/usr/bin/ffmpeg"
  # Adjust this path if ffmpeg is located elsewhere
def download_song():
    #downloads the song from youtube in mp4 format
    url = input('insert the link of the youtube song that you want to download: ')
    yt = YouTube(url)
    video= yt.streams.filter(progressive=True, file_extension='mp4').first()
    output_dir = "temp_audio"
    os.makedirs(output_dir, exist_ok=True)
    out_file = video.download(output_path=output_dir)
    return out_file

def file_conversion(out_file):
    #converts the file into mp3 format
    base, ext = os.path.splitext(out_file)
    audio = AudioSegment.from_file(out_file)
    mp3_file = base + '.mp3'
    audio.export(mp3_file,format='mp3')
    return mp3_file

def remove_mp4(out_file):
    #deletes the original mp4 file
    os.remove(out_file)

def youtube_download():
    out_file= download_song()
    mp3_file = file_conversion(out_file)
    remove_mp4(out_file)
    print(f"Downloaded and converted to {mp3_file}")
    repeat()

def repeat():
    #asks if you want to download more songs
    question = input('do you want to download another song? Yes/No? ' )
    if question == 'yes':
        youtube_download()
    else:
        exit()

if __name__ == "__main__":
    youtube_download()