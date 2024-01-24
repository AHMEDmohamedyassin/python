from pytube import YouTube , Playlist
from math import ceil
import inquirer
import os
from progress.bar import ChargingBar
from pystyle import Write, Colors
from art import tprint


errorMsg = 'Something happened on Downloading'
AllResChoise = [inquirer.List('start', message="which resolution you want ? ", choices=[144 , 240 , 360 , 480 , 720 , 1080 , 2160] )]
writingInterval = 0.03

# the progress function 
def theProgress(yt , theStream) :
    print(f'Downloading with resolution : {theStream.resolution} , size : {ceil(theStream.filesize_mb)} MB \n the title : {yt.title}')
    bar = ChargingBar('Downloading', max=theStream.filesize , suffix='%(percent)d%%' )
    for i in range(theStream.filesize):
        yt.register_on_progress_callback(lambda a , b , c : bar.next(c))
    bar.finish()

# video data function
def getVideoData (streams , audio = False , res = 0) : # if res is setted the function will return this resolution if available or greater
    if (audio): 
        return {
            "size" : f"{ceil(streams.get_audio_only().filesize_mb)} MB",
            "type" : 'audio',
        }
    videoData = [] 
    selectedRes = 0
    minRes = 10000000
    maxRes = 0
    for e in streams:
        if(e.mime_type.find('mp4') == -1 or e.is_progressive == False): continue
        data = {
            "res" : int(e.resolution.replace('p' , '')),
            "size" : f"{ceil(e.filesize_mb)} MB",
            "type" : e.type,
        }
        videoData.append(data)
        #check if needed certain resolution to return it or greater than it
        if(res > 0 and selectedRes < 1):
            if(data['res'] < minRes ): minRes = data['res']
            if(data['res'] > maxRes ): maxRes = data['res']
            if(data['res'] >= res ) :
                selectedRes = data['res'] 
    
    if res < 1 :
        return videoData
    if selectedRes < 1 and res < minRes : 
        return minRes
    if selectedRes < 1 and res > maxRes : 
        return maxRes
    return selectedRes


# download audio
def DownloadAudio (url) :
    try :
        yt = YouTube(url)
        theStream = yt.streams.get_audio_only()
        theProgress(yt , theStream)
        theStream.download()
    except : Write.Print(errorMsg, Colors.red, interval=writingInterval)

# download video
def DownloadVideo (url) :
    try : 
        yt = YouTube(url)
        data = getVideoData(yt.streams)
        res = []
        for e in data : res.append(e['res'])
        startChoises = [inquirer.List('start', message="which resolution you want ? ", choices=res )]
        
        selectedres = inquirer.prompt(startChoises)
        for e in data : 
            if e['res'] == selectedres['start']:
                data = e
                break
        theStream = yt.streams.get_by_resolution(selectedres['start'])
        theProgress(yt , theStream)
        theStream.download()
    except : Write.Print(errorMsg, Colors.red, interval=writingInterval)

# download playlist 
def DownloadPlayList (url , res = False):
    try :
        p = Playlist(url)

        # optimize name and path of dir
        name = p.title
        while os.listdir(os.getcwd()).__contains__(name):
            name = name + '-1'
        path = f'{os.getcwd()}/{name}'
        os.mkdir(path)

        selectedres = 0
        if res == False : 
            selectedres = inquirer.prompt(AllResChoise)
        else: selectedres = res
        
        for key , url in enumerate(p.video_urls):
            try : PlaylistVideo(url , selectedres['start' ] , path , key )
            except : Write.Print(errorMsg, Colors.red, interval=writingInterval)
    except : Write.Print(errorMsg, Colors.red, interval=writingInterval)

# helper function for DownloadPlayList function 
def PlaylistVideo(url , res , path , key):
    try : 
        yt = YouTube(url)
        res = getVideoData(yt.streams , res=res)
        theStream = yt.streams.get_by_resolution(res)

        theProgress(yt , theStream)
        theStream.download(output_path=path , filename_prefix=f'{key + 1} - ')
    except : Write.Print(errorMsg, Colors.red, interval=writingInterval)

#download multi playlists
def DownloadMultiPlaylists():
    state = True
    urls = []
    inputingway = [inquirer.List('start', message="which resolution you want ? ", choices=['one by one' , 'separated by simicolon " , " '] )]
    inputingwayChoise = inquirer.prompt(inputingway)
    
    if(inputingwayChoise['start'] == 'one by one'):
        url = Write.Input("Enter url of Any video in playlist  ->  ", Colors.red_to_purple, interval=writingInterval)
        urls = [url]
        while state : 
            url = Write.Input("Enter url of Any video in play list if there is no type ok  ->  ", Colors.red_to_purple, interval=writingInterval)
            if(url == 'ok') : state = False
            else : urls.append(url)
    else :
        url = Write.Input("Enter All urls separated by simicolon ' , '  ->  ", Colors.red_to_purple, interval=writingInterval)
        urls = url.split(',')
    
    res = inquirer.prompt(AllResChoise)
    for url in urls :
        try :
            yt = YouTube(url)
            if yt.check_availability() == None :
                DownloadPlayList(url , res)
        except: Write.Print(f'{url} \t is not found \n', Colors.red, interval=writingInterval)

#measure playlist
def Measure_playlist():
    try :
        url = Write.Input("Enter url of Any video in playlist  ->  ", Colors.red_to_purple, interval=writingInterval)
        p = Playlist(url)
        size = 0
        thefinalres = 0
        selectedres = inquirer.prompt(AllResChoise)

        Write.Print('loading please wait ....... \n\n\n' , Colors.blue_to_cyan , interval=0.05)
        
        for key , url in enumerate(p.video_urls):
            try : 
                yt = YouTube(url)
                res = getVideoData(yt.streams , res=selectedres['start'])
                theStream = yt.streams.get_by_resolution(res)
                size = theStream.filesize_mb + size
                thefinalres = res
            except : Write.Print(errorMsg, Colors.red, interval=writingInterval)
        Write.Print(f'the size is {size} MB with resolution {thefinalres}p \n\n\n' , Colors.green_to_cyan , interval=0.05)
    except : Write.Print(errorMsg, Colors.red, interval=writingInterval)

def start ():
    tprint('Downloader')
    Write.Print('Made By Ahmed Yassin \n\n\n' , Colors.blue_to_green , interval=0.05)
    state = True
    startChoises = [
        inquirer.List('start',
            message="what is the type of installation you want ? ",
            choices=["Audio" , "Video" , "Playlist" , "Playlists" , "Measure_playlist" , 'Exit'],
            ),
    ]

    while state :
        startAnswer = inquirer.prompt(startChoises)
        if startAnswer == None : 
            state = False
            continue

        if(startAnswer['start'] == 'Audio') :
            url = Write.Input("Place Audio url  ->  ", Colors.red_to_purple, interval=writingInterval)
            DownloadAudio(url)
        elif(startAnswer['start'] == 'Video') :
            url = Write.Input("Place Video url  ->  ", Colors.red_to_purple, interval=writingInterval)
            DownloadVideo(url)
        elif(startAnswer['start'] == 'Playlist'):
            url = Write.Input("Place url of Video in Playlist  ->  ", Colors.red_to_purple, interval=writingInterval)
            DownloadPlayList(url)
        elif(startAnswer['start'] == 'Playlists'):
            DownloadMultiPlaylists()
        elif(startAnswer['start'] == 'Measure_playlist'):
            Measure_playlist()
        else : state = False

start()