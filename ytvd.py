import sys
import pytube
def main(link):
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    # stream.download('/Volumes/my_docs/Video_Youtube_DL')
    stream.download('Path_To_Video_Youtube_Download')

if __name__ == "__main__":
    main(sys.argv[1])