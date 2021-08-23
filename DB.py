import sqlite3

class DataBase () :

    def __init__(self) :
        self.conn = sqlite3.connect('playlist.db')
        self.cur = self.conn.cursor()

        # self.cur.execute("INSERT INTO playerdata (Playlist) VALUES('운동')")
        
        

        # self.conn.commit()
        # self.conn.close()

    def __del__(self):
        self.conn.close()


    def InputList(self, listname):  # 리스트추가
        self.cur.execute("INSERT INTO playerdata (Playlist) VALUES('"+ listname +"')")

        self.conn.commit()

    def DeleteList(self, listname) :
        self.cur.execute("DELETE FROM playerdata WHERE Playlist = '"+ listname + "'")

        self.conn.commit()
        
    # def login(self, id, password):  # 로그인
    #     self.cur.execute("SELECT * FROM playerdata WHERE ID = '" +
    #                      id + "' and Password = '" + password + "'")

    #     data = self.cur.fetchall()

    #     if len(data) == 0:
    #         return False
    #     else:
    #         return True


if __name__ == "__main__":
    test = DataBase()