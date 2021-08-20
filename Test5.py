import sys

import vlc
import pafy

from PyQt5 import QtCore, QtGui, QtWidgets


class Player(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Player, self).__init__(parent)
        self.setWindowTitle("Media Player")
        # creating a basic vlc instance
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        ##########video frame
        self.videoframe = QtWidgets.QFrame(
            frameShape=QtWidgets.QFrame.Box, frameShadow=QtWidgets.QFrame.Raised
        )

        if sys.platform.startswith("linux"):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.videoframe.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(self.videoframe.winId())

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.addWidget(self.videoframe)

        url = "https://youtu.be/Xln4crS82aM"
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url

        # filename = "/path/of/your/video.mp4"
        media = self.instance.media_new(playurl)
        self.mediaplayer.set_media(media)
        self.mediaplayer.play()




        # url = "https://youtu.be/Xln4crS82aM"
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


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    player = Player()
    player.show()
    player.resize(640, 480)

    sys.exit(app.exec_())