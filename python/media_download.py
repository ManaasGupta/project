from pytube import YouTube
import os
os.makedirs("media_files",exist_ok = True)
#ask for the link from user
def yt_video_download(link):
    yt = YouTube(link)

    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    #Starting download
    try:
        print("Downloading video...")
        ys.download("media_files")
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
    output_path = "media_files\\"

    try:
        # Download the audio stream
        print("Downloading audio...")
        out_file=audio_stream.download(output_path=output_path)
        print("Download completed!!")
        # save the file
        print("Saving file....")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("File Saved")
    except:
        print("Download failed!!")

def spo_audio_download(link):
    os.chdir("media_files")
    print("spotify version: ",os.system("spotdl --version"))
    link=link
    try:
        print("Downloading audio...")
        os.system(f"spotdl {link}")
    except:
        print("Download failed!!")
    finally:
        os.system("cd ..")

def main():
    print("Welcome to YouTube Downloader V1.0")
    print("Please select the option you want to use:")
    print("1. Download Video")
    print("2. Download Audio")
    print("3. Exit")
    option = int(input("Enter your option: "))
    if option == 1:
        link = input("Enter the link: ")
        yt_video_download(link)
    elif option == 2:
        link = input("Enter the link: ")
        check = link.split("/")
        if check[2] == 'www.youtube.com':
            yt_audio_download(link)
        else:
            spo_audio_download(link)
    else:
        print("Bye Bye have a nice day.....")
if __name__=="__main__":  
    main()