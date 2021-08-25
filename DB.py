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


    def InputList(self):  # 리스트추가
        self.cur.execute("INSERT INTO playerdata (Playlist) VALUES('재생목록')")

        self.conn.commit()

    def DeleteList(self, listname) :
        self.cur.execute("DELETE FROM playerdata WHERE Playlist = '"+ listname + "'")

        self.conn.commit()
        
    def calllist(self) :
        self.cur.execute("SELECT * FROM playerdata")
        self.nowlist = self.cur.fetchall()
    
    
        
    # def login(self, id, password):  # 로그인
    #     self.cur.execute("SELECT * FROM playerdata WHERE ID = '" +
    #                      id + "' and Password = '" + password + "'")

    #     data = self.cur.fetchall()

    #     if len(data) == 0:
    #         return False
    #     else:
    #         return True

    #     def Signup(self, id, pw, name, phone, email):  # 회원가입
    #     self.cur.execute("INSERT INTO playerdata (ID,Password,Name,Phone,E_mail) VALUES('" + id + "', '" + pw + "', '" + name + "', '" + phone + "', '" + email + "')")

    #     self.conn.commit()

    # def checkId(self, id):
    #     self.cur.execute("SELECT * FROM playerdata WHERE id = '" + id + "'")
    #     data = self.cur.fetchall()

    #     if len(data) == 0:
    #         return False
    #     else:
    #         return True

       # def start(self):
       # self.a = input("1번째꺼 입렵")
       # self.b = input("2번째꺼 입력")

       # conn = sqlite3.connect('test.db')#괄호안에 DB이름 써야함, 대신 파일이랑 같은공간에 있어야함
       # cur = conn.cursor() # 커서라는 명령억 따로있음 / #데베랑 우리를 연결시켜주는 일꾼

        #cur.execute ("CREATE TABLE user (id TEXT, password TEXT)") #여기다가는 쿼리문입력 / user 테이블 생성 (id, password 컬럼생성) (한번만하고 주석처리)

        # cur.execute ("CREATE TABLE user3(id LONGTEXT PRIMARY KEY, password LONGTEXT)") # 기본키는 중복불가 알지

       # cur.execute("INSERT INTO user3 VALUES(?,?)",(self.a, self.b))
        
        # cur.execute("DELETE FROM user2 WHERE id='testId'")

        # cur.execute("DROP TABLE user") # 테이블삭제

        # cur.execute("INSERT INTO user2 VALUES('testId', '1234')")
        # cur.execute("UPDATE user2 SET id='test' WHERE id='testId' ")

        # cur.execute("SELECT * FROM user2")  # * 부분에 id, password치면 test, 1234이렇게 뜬다
                                            #

        #print(cur.fetchall()) # 컬이 들고온거를 디코딩(변환)시켜서 우리눈에 보여야함
        # 또는 변수에 저장시키고 싶으면 data = cur.fetchall() 해주면된다
        # data = cur.fetchall()  # cur은 한번사용하면 리셋이니 계속 해줘야함 ★★★★★★

        # recvId = data[0][0]    #[로우],[컬럼]  (x,y) 근데 3개다? x,y,z 3차원 개념
        # redcvPw = data[0][1]

        # print(recvId)
        # print(redcvPw)


if __name__ == "__main__":
    test = DataBase()