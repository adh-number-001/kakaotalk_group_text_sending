import time
from tkinter import *
import threading


import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.messagebox as tkmb
from tkinter import ttk

 
from selenium import webdriver
import cv2 as cv
from difflib import get_close_matches  
import time
 
import os
import schedule
 
import subprocess
import pyautogui as pag

import webbrowser
import pyperclip, pyautogui
import pyautogui, sys
 
import requests
import random
import datetime

import pyautogui as pag
from PIL import ImageGrab

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from datetime import datetime
from tkinter import messagebox
 
 
from tkinter import filedialog


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1  # 각 동작 사이에 1초 대기

def startThread():
    def run_in_thread():
        try:
            doRun()
        except Exception as e:
            print(f"Error in thread: {e}")
            # GUI 관련 에러 메시지도 메인 스레드에서 표시
            mainWin.after(0, lambda: messagebox.showerror("Error", str(e)))
    
    thread = threading.Thread(target=run_in_thread)
    thread.daemon = True
    thread.start()
 
def doRun():
    
    path = r"/Applications/KakaoTalk.app"
    subprocess.Popen(['open', '-a', 'KakaoTalk'])
    
    print('opening Kakao Talk')
    login_pass_search()

def login_pass_search():

    print("message")
    time.sleep(3)

    if chkvar.get() == 1:         # 체크박스가 체크 되었는지 확인
 
       print("첨부파일 선택하셨습니다 :",open_button_title["text"])


    while True:

        try:
            img = pyautogui.locateOnScreen('kakao_image/pass.png', confidence=0.8, grayscale = True)
            print("잠김 로그인 시도")

            #pyautogui.press('return')
          
            kakatok_pass_bunho    = kakatok_pass.get()
            pyautogui.write(kakatok_pass_bunho)

            time.sleep(1)
            search_tab()
            break

        except:

            print("로그인 성공--")
            search_tab()
            pass


def search_tab():

    print("message")
    time.sleep(3)

     
    while True:

        try:
            img = pyautogui.locateOnScreen('kakao_image/tab1.png', confidence=0.8, grayscale = True)
            button_location_search_tab = pyautogui.center(img)
            pyautogui.click(button_location_search_tab.x, button_location_search_tab.y)  

            print('친구탭 클릭')
             
            #pyautogui.press('return')
            time.sleep(1)
            find_fren()
            break

        except:

            print("친구탭 클릭")
            find_fren()
            pass

def safe_gui_operation(func):
    def wrapper(*args, **kwargs):
        if threading.current_thread() is not threading.main_thread():
            return mainWin.after(0, lambda: func(*args, **kwargs))
        return func(*args, **kwargs)
    return wrapper

@safe_gui_operation
def update_count_label(count):
    kakatok_member_count_send_label.configure(text=str(count))

@safe_gui_operation
def show_alert(message):
    pyautogui.alert(message)

def find_fren():

        time.sleep(random.uniform(3,4))
        
        button_location = pyautogui.locateOnScreen('kakao_image/search.png', confidence=0.6)

        title_search    = kakatok_search.get()
        title_content   = kakatok_content.get("1.0", "end")

        kakatok_member_count1 = int(kakatok_member_count.get())

        print(title_search)
        print(title_content)

        #검색버튼이 활성화 여부
        if button_location is None:  #검색버튼이 활성화 안되었다는 의미
            print("서치 버튼 찾기 실패 ㅠㅠ")

        else: #검색버튼 클릭
            
            try:
                
                time.sleep(random.uniform(1,2))
                button_location1 = pyautogui.center(button_location)
                pyautogui.click(button_location1.x, button_location1.y)  # X 아이콘을 눌러서 기존 텍스트를 지워주기


                time.sleep(random.uniform(2,2))
                pyperclip.copy(title_search)
                pyautogui.hotkey("command", "v")
                time.sleep(3)


                time.sleep(random.uniform(1,2))
               
                i=0

                for i in range(kakatok_member_count1):

                    print("보낸사람 카운터 : ",i)
                    current_time = datetime.now()
                    print("카톡 보낸시간 : ", current_time)

                    # GUI 업데이트를 메인 스레드에서 실행하도록 변경
                    # update_count_label(i+1)

                    if i == 0 :
                       pyautogui.press('down', presses=2)    #한깐씩 아래로 이동
                    else :
                       pyautogui.press('down', presses=2) 
                       
                    pyautogui.press('return')              #아이디 선택후 클릭
                    pyperclip.copy(title_content)
                    #pyautogui.press('tab')
                    pyautogui.hotkey("command", "v")
                    pyautogui.press('return')              #메세지 입력후 클릭
                    time.sleep(random.uniform(1,1)) 

                    if chkvar.get() == 1:                 # 첨부파일 체크박스가 체크 되었는지 확인
                
                        print("첨부파일 선택하셨습니다 :",open_button_title["text"])
                        pyautogui.hotkey("command", "t")
                        time.sleep(random.uniform(1,1))
                        pyperclip.copy(open_button_title["text"])
                        pyautogui.hotkey("command", "v")
                        pyautogui.press('return')
                        time.sleep(random.uniform(1,1)) 
                        pyautogui.press('return')      
                        time.sleep(random.uniform(1,1)) 

                    kakatok_member_count_send_label.configure(text=str(i+1))
                    print("확인전송번호 : ", i)

                    pyautogui.press('esc')                #카카오톡 채팅창 닫기
                    time.sleep(random.uniform(1,1)) 
               
                while True:           
                        
                    try:
                                 
                        button_location_close = pyautogui.locateCenterOnScreen("kakao_image/search.png",confidence=0.6)
                            
                        print(button_location_close)
                        print("채팅창 초기화를 위한 검색버튼 찾아 원위치") 
                        time.sleep(3)
                        
                        pyautogui.click(button_location_close)
                        print("검색 버튼 클릭")
                        time.sleep(3)

                        pyautogui.press('esc')                  #카카오톡 창 닫기 

                        break

                    except Exception as swear:
                    
                        print("검색 버튼 클릭 못찾음: ",str(swear))
                        
                        time.sleep(5)
 
                 
                pyautogui.alert('카톡 보내기가 완료 되었습니다')
                
                time.sleep(random.uniform(20,40))
                ex1()
                
            except Exception as swear:

                print("cannot open KakaoTalk: ",str(swear))

# 파일 열기 버튼 이벤트 핸들러 함수
def openFile():

    pyautogui.alert('[필수 | 반드시 카카오톡에서 파일을 보내신후 프로그램을 시작하세요]\n\n첨부파일 보내실때는 반드시 먼저 카카오톡에서\n보내실 사람을 본인 또는 1명을 선택하여 첨부파일을 보내주세요.\n\n보내실 파일을 카카오톡에서 보내신후\n\n채팅창 및 카톡창을 닫아주세요.\n\n그리고 프로그램을 실행해 주세요')


    file_path = filedialog.askopenfilename() # 파일 열기 대화상자 열기
    # 해당 파일 경로를 이용한 파일 처리 코드 작성
    print(os.path.basename(file_path))
    
    open_button_title.configure(text=str(os.path.basename(file_path)))
 



def ex1():
    
    mainWin.quit()
 


if __name__ == "__main__":

    mainWin = Tk()
    mainWin.geometry("720x760")
    mainWin.resizable(width=False,height=False)
    mainWin.title("카톡 메세지 보내기")

    kakatok_pass_title = Label(mainWin, text="카톡 잠김모드 진행시 비밀번호", fg='red', font=("맑은고딕", 9))
    kakatok_pass_title.place(x=70,y=30)

    kakatok_pass = Entry(mainWin, width=30)
    kakatok_pass.place(x=70,y=60,height=30)
    kakatok_pass.insert(0, "")

    kakatok_search_title = Label(mainWin, text="카톡 친구 목록에서 검색할 단어", font=("맑은고딕", 9))
    kakatok_search_title.place(x=70,y=96)

    kakatok_search = Entry(mainWin, width=30)
    kakatok_search.place(x=70,y=125,height=30)
    kakatok_search.insert(0, "검색단어 입력")

    kakatok_member_count_title_m = Label(mainWin, text="카톡에서 전송하실 사람수(명)", fg='blue', font=("맑은고딕", 9))
    kakatok_member_count_title_m.place(x=300,y=96)

    kakatok_member_count = Entry(mainWin, width=30)
    kakatok_member_count.place(x=300,y=125,height=30)

    kakatok_member_count.insert(0, "100")

    kakatok_content_title = Label(mainWin, text="카톡에서 보낼 메세지", font=("맑은고딕", 9))
    kakatok_content_title.place(x=70,y=168)

    kakatok_content = tkst.ScrolledText(mainWin, width=63, height=30)     # Create a scrolledtext
    kakatok_content.place(x=70,y=190)
 
    kakatok_member_count_send_title = Label(mainWin, text="전송 카운터", fg='red', font=("맑은고딕", 9))
    kakatok_member_count_send_title.place(x=560,y=30)

    kakatok_member_count_send_label = Label(mainWin, text="0", fg='red', font=("맑은고딕", 51))
    kakatok_member_count_send_label.place(x=560,y=120)
    chkvar = IntVar()                             # chkvar에 int 형으로 값을 저장
    chkbox = Checkbutton(mainWin, variable=chkvar)   # root라는 창에 체크박스 생성
    chkbox.config(text="첨부")                  # 체크박스 내용 설정
    chkbox.place(x=70,y=600)
 
    open_button = Button(mainWin, text="카톡 이미지 또는 파일 첨부", command=openFile)
    open_button.place(x=130,y=600)

    open_button_title = Label(mainWin, text="카톡 전송 URL", font=("맑은고딕", 9))
    open_button_title.place(x=330,y=605)

    b1 = Button(mainWin, text="카톡보내기 실행",fg='red',bg='yellow',width=25, height=3,command=startThread)
    b2 = Button(mainWin, text="종료",width=25, height=3,command=ex1)

    b1.place(x=70,y=650)
    b2.place(x=335,y=650)

    mainWin.mainloop()