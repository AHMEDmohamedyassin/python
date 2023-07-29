from pytube import YouTube , Playlist
import inquirer

def Choises(my_video):
    questions = [
                inquirer.List('audio_only',
                                message="do you need to install audio only ?",
                                choices=['yes' , 'no'],
                            ),
            ]
    answers = inquirer.prompt(questions)

    my_video_down = None

    if(answers["audio_only"] == "yes"):

        my_video_down = my_video.streams.get_audio_only()

    else:
        questions = [
            inquirer.List('resolution',
                message="do you need to install audio only ?",
                choices=["144p" , "240p" , "360p" , "480p" , "720p" , "1080p"],
                ),
        ]
        answers = inquirer.prompt(questions)
        my_video_down = my_video.streams.get_by_resolution(answers["resolution"])
    
    return my_video_down


def Video(): 
    state = True
    while state :
        try :
            url = input('enter url here : ')

            my_video = YouTube(url)

            my_video_down = Choises(my_video)

            print("downloading")

            my_video_down.download()
            state = False
        
        except : 
            print('something went wrong please try again')

    print("done")

def Playlist_func(): 
    state = True
    while state :
        try :
            url = input('enter url here : ')

            my_playlist = Playlist(url)

            print("downloading")

            for video in my_playlist.videos:
                video.streams.first().download()

            state = False
        
        except : 
            print('something went wrong please try again')

    print("done")

Playlist_func()