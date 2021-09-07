from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from google.auth.environment_vars import AWS_DEFAULT_REGION

import DB
import SearchUi
import Pop_up
from googleapiclient.discovery import build
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# from oauth2client.tools import argparser

class SearchPage() : # 검색창 

    def __init__(self,SearchBtn) :
        
        self.SearchUi = SearchUi.Ui_SearchUi() # 검색창UI
        self.SearchUiBtn = SearchBtn
        self.Popup = Pop_up.Popup_Window() # 팝업창UI
        self.SearchUiBtn.mousePressEvent = lambda event : self.SearchUiShowEvent(event)
        self.SearchUi.AddBtn.mousePressEvent = lambda event : self.SaveDBEvent(event)
        
        DEVELOPER_KEY = "AIzaSyCvq5k8yE26NlsZaA23MDMSUleJs97Flds"
        YOUTUBE_API_SERVICE_NAME="youtube"
        YOUTUBE_API_VERSION="v3"
        self.youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)


    def SearchUiShowEvent(self, event) :
        self.SearchUi.SearchUi.show()


    def SaveDBEvent(self, event) :

        db = DB.DataBase()
        db.calllist()

        playlist_text = self.SearchUi.PlaylistText.text()
        self.ExtractURL(self.SearchUi.SearchText.text()) # 검색값을 API이용한 함수들로 입력
        self.ExtractTitle(self.SearchUi.SearchText.text())
        self.ExtractThumbnails(self.SearchUi.SearchText.text())
        
        db.SearchPlaylistNo(playlist_text)
        playlist_db = db.list[0][0] #2차원배열 0번째[0]가 튜플 1번째[0]가 튜플안 원소를 가르킨다 / 만약 원소가 리스트라면 3차원배열인것
        db.Inputurllist(str(playlist_db),str(self.url),str(self.title),str(self.thumbnails))

        self.SearchUi.PlaylistText.clear()
        self.SearchUi.SearchText.clear()
        self.SearchUi.SearchUi.close()


    def ExtractURL(self, keyword) : # API로 URL검출

        search_response = self.youtube.search().list(q = str(keyword), #검색어
                                                    order = "relevance",  #정렬방법
                                                    part = "snippet", #필수 매개변수
                                                    maxResults = 1
                                                    ).execute()

        if search_response['items'][0]['id']['kind'] == "youtube#channel" : #검색어에 채널입력시 첫영상이 동영상이 아니므로 팝업창 처리
            self.Popup.Popup_Window.show()
        else :
            self.url = search_response['items'][0]['id']['videoId']
            return self.url
     

    def ExtractTitle(self, keyword) : # API로 Title검출
            
        search_response = self.youtube.search().list(q = str(keyword), #검색어
                                                    order = "relevance",  #정렬방법
                                                    part = "snippet", #필수 매개변수
                                                    maxResults = 1
                                                    ).execute()
        if search_response['items'][0]['id']['kind'] == "youtube#channel" :
            self.Popup.Popup_Window.show()
        else :
            self.title = search_response['items'][0]['snippet']['title']
            return self.title


    def ExtractThumbnails(self, keyword) : # API로 썸네일 주소 검출
            
        search_response = self.youtube.search().list(q = str(keyword), #검색어
                                                    order = "relevance",  #정렬방법
                                                    part = "snippet", #필수 매개변수
                                                    maxResults = 1
                                                    ).execute()
        if search_response['items'][0]['id']['kind'] == "youtube#channel" :
            self.Popup.Popup_Window.show()
        else :
            self.thumbnails = search_response['items'][0]['snippet']['thumbnails']['default']['url']
            return self.thumbnails
        