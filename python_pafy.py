'''
URL = https://pypi.python.org/pypi/pafy#downloads
Ubuntu - install python-pafy
sudo pip install youtube-dl
sudo pip install pafy

How to use it -

python python_pafy.py -u "URL" --video/--audio
'''

import pafy

def main(url,v,a):
    video = pafy.new(url)
    if v:
        best = video.getbest()
        print ("Downloading video %s  , resolution = %s" %(video.title,best.resolution))
        best.download(quiet = False)
    elif a:
        bestaudio = video.getbestaudio()
        print ("Downloading audio %s  , bitrate = %s" %(video.title,bestaudio.bitrate))
        bestaudio.download()

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser("YouTube Downloader script")
    parser.add_argument('-u', '--url', help='URL of the YouTube video to be downloaded .',
                        required=True)
    parser.add_argument('--audio', action='store_true') // to download audio
    parser.add_argument('--video', action='store_true') // to download video
    args = parser.parse_args()
    main(args.url,args.video,args.audio)
