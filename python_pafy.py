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
    import pdb;pdb.set_trace()
    if v:
        best = video.getbest()
        print ("Downloading video %s  , resolution = %s" %(video.title,best.resolution))
        best.download(quiet = False)
    elif a:
	streams = video.audiostreams
	print streams
	input = int(raw_input("Enter audio index to be downloaded."))
        print ("Downloading audio %s  , bitrate = %s" %(streams[input].title,streams[input].bitrate))
        streams[input].download()

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser("YouTube Downloader script")
    parser.add_argument('-u', '--url', help='URL of the YouTube video to be downloaded .',
                        required=True)
    parser.add_argument('--audio', action='store_true') 
    parser.add_argument('--video', action='store_true') 
    args = parser.parse_args()
    main(args.url,args.video,args.audio)
