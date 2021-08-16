import sqlite3

class DataBase () :

    def __init__(self) :
        self.conn = sqlite3.connect('playerdata.db')
        self.cur = self.conn.cursor()

    def insert(self) :
        

        def __init__(self) :
        # conn = sqlite3.connect('playerdata.db') #괄호안에 DB이름 써야함, 대신 파일이랑 같은공간에 있어야함
        # cur = conn.cursor() 

        self.conn = sqlite3.connect('playerdata.db')
        self.cur = self.conn.cursor()

        # cur.execute ("CREATE TABLE playerdata (No integer primary key, ID TEXT, Password TEXT, Name TEXT, Phone TEXT, E_mail TEXT)") #여기다가는 쿼리문입력 / user 테이블 생성 (id, password 컬럼생성) (한번만하고 주석처리)
        # https://araikuma.tistory.com/690 auto increment 여기 참고
        # cur.execute("INSERT INTO playerdata (ID,Password,Name,Phone,E_mail) VALUES('1234', '1234', '이병도', '01022939123', '1234@naver.com')")

        # cur.execute("SELECT * FROM playerdata order by ID asc")
        # result = cur.fetchall()
        # print(result)

        # conn.commit()  #데이터 넣을때 써야함 ok하는뜻  ★데이터 INSERT나 수정할때만 쓰는걸로!!! SELECT는 안써도되는듯
        # conn.close() #닫아줘야 안전함
    
    def login(self, id, password):  # 로그인
        self.cur.execute("SELECT * FROM playerdata WHERE ID = '" +
                         id + "' and Password = '" + password + "'")

        data = self.cur.fetchall()

        if len(data) == 0:
            return False
        else:
            return True