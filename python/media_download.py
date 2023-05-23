from pytube import YouTube
import os
import sys
import argparse
#ask for the link from user
def yt_video_download(link):
    yt = YouTube(link)

    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    #Starting download
    try:
        print("Downloading video...")
        ys.download()
        print("Download completed!!")
    except:
        print("Download failed!!")
        
def yt_audio_download(link):

    # Provide the YouTube video URL
    url = link

    # Create a YouTube object
    yt = YouTube(url)

    # Extract the audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Set the output path for the downloaded audio

    try:
        # Download the audio stream
        print("Downloading audio...")
        out_file=audio_stream.download()
        print("Download completed!!")
        # save the file
        print("Saving file....")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.wav'
        os.rename(out_file, new_file)
        print("File Saved")
    except:
        print("Download failed!!")

def spo_audio_download(link):
    print("spotify version: ",os.system("spotdl --version"))
    link=link
    try:
        print("Downloading audio...")
        os.system(f"spotdl {link}")
    except:
        print("Download failed!!")
    finally:
        os.chdir("..")

def main(args):
    os.makedirs("media_files",exist_ok = True)
    os.chdir("media_files")
    if (args.mode == 'video') or (args.mode == 'Video') or (args.mode == 'VIDEO'):
        yt_video_download(args.link)
    elif (args.mode == 'audio') or (args.mode == 'Audio') or (args.mode == 'AUDIO'):
        check = args.link.split("/")
        if check[2] == 'www.youtube.com':
            yt_audio_download(args.link)
        else:
            spo_audio_download(args.link)
    else:
        print("Bye Bye have a nice day.....")
if __name__=="__main__":  
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',type=str,help="Enter video or audio",required=True)
    parser.add_argument('--link',type=str,help="Enter link",required=True)
    args=parser.parse_args()
    sys.stdout.write(str(main(args)))