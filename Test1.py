import vlc
import pafy
import urllib.request

class Test() :

    def __init__(self) :
        pass

    def videoplay(self, url) :
        # url = "https://youtu.be/Xln4crS82aM"
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        ins = vlc.Instance()
        self.player = ins.media_player_new()

        code = urllib.request.urlopen(url).getcode()
        if str(code).startswith('2') or str(code).startswith('3'):
            print('Stream is working')
        else:
            print('Stream is dead')

        Media = ins.media_new(playurl)
        Media.get_mrl()
        self.player.set_media(Media)
        self.player.play()

        good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
        while str(self.player.get_state()) in good_states:
            print('Stream is working. Current state = {}'.format(self.player.get_state()))

        print('Stream is not working. Current state = {}'.format(self.player.get_state()))
        self.player.stop()



# if __name__ == "__main__":
#      start = Test()