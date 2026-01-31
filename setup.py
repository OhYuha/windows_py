import os # import
import hashlib # import
import time # import
def md(path): # 폴더 생성 함수
    if not os.path.exists(path):
        os.makedirs(path)
md("C:/windowspy") # 폴더 생성
print("windows py 설치를 시작합니다.") # 안내
print("이름을 입력하여 주십시오" ,end=" ") # input
uid = input(":") # input
hash_object = hashlib.sha256(uid.encode()) # 유저아이디 sha256 암호화
uidsha = hash_object.hexdigest() # 유저아이디 sha256 암호화
f = open("C:/Windowspy/uid.txt","w") # txt 파일 생성/오픈
f.write(uidsha) # 유저아이디 저장
f.close() # 끄기
print("비밀번호를 입력하세요 :", end=" ") # 안내
upw = input() # input
hash_object = hashlib.sha256(upw.encode()) # 비밀번호 sha256 암호화
upwsha = hash_object.hexdigest() # 비밀번호 sha256 암호화
f = open("C:/Windowspy/upw.txt","w") # txt 파일 생성/오픈
f.write(upwsha) # 비밀번호 쓰기
f.close() # 파일 닫기
print("Windows py Setup.py 을 종료합니다. 다음에는 windows py start.py 로 접속해 주세요") # 안내
time.sleep(2) # 2초 기다리기
exit() # py 파일 끄기

