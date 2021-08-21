import vlc
import pafy
import urllib.request
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Test() :

    def __init__(self) :

        # self.url = "https://youtu.be/qwqweqe"

        # self.instance = vlc.Instance()
        # self.mediaplayer = self.instance.media_player_new()
        # video = pafy.new(self.url)
        # best = video.getbest()
        # playurl = best.url
                
        # media = self.instance.media_new(playurl)
        # self.mediaplayer.set_media(media)
        # self.mediaplayer.play()

        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        

    def videoplay(self, url) :



        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
                
        media = self.instance.media_new(playurl)
        self.mediaplayer.set_media(media)
        self.mediaplayer.play()
        

        # url = "https://youtu.be/Xln4crS82aM"
        # video = pafy.new(url)
        # best = video.getbest()
        # playurl = best.url


        # if sys.platform.startswith("linux"):  # for Linux using the X Server
        #     self.mediaplayer.set_xwindow(self.videoframe.winId())
        # elif sys.platform == "win32":  # for Windows
        #     self.mediaplayer.set_hwnd(self.videoframe.winId())
        # elif sys.platform == "darwin":  # for MacOS
        #     self.mediaplayer.set_nsobject(self.videoframe.winId())


        

        # filename = "/path/of/your/video.mp4"
        # media = self.instance.media_new(playurl)
        # self.mediaplayer.set_media(media)
        # self.mediaplayer.play()


        # # url = "https://youtu.be/Xln4crS82aM"
        # video = pafy.new(url)
        # best = video.getbest()
        # playurl = best.url
        # ins = vlc.Instance()
        # self.player = ins.media_player_new()

        # code = urllib.request.urlopen(url).getcode()
        # if str(code).startswith('2') or str(code).startswith('3'):
        #     print('Stream is working')
        # else:
        #     print('Stream is dead')

        # Media = ins.media_new(playurl)
        # Media.get_mrl()
        # self.player.set_media(Media)
        # self.player.play()

        # good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
        # while str(self.player.get_state()) in good_states:
        #     print('Stream is working. Current state = {}'.format(self.player.get_state()))

        # print('Stream is not working. Current state = {}'.format(self.player.get_state()))
        # self.player.stop()



# if __name__ == "__main__":
#      start = Test()

