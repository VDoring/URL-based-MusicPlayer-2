# common_func.py는 공통으로 사용되는 특정 기능을 수행하는 함수를 모아두는 곳입니다.
import os
import time

#by VDoring. 2021.06.21
#Mlist.txt 파일의 존재여부를 확인합니다.
#리턴값:True, False
def checkMlistFile():
    is_file_available = os.path.isfile('Mlist.txt') # Mlist.txt 파일이 올바른 위치에 존재하는지 확인
    if is_file_available == False: # Mlist.txt 파일이 없다면
        print('[!] Mlist.txt 파일을 찾을 수 없습니다 [!]')
        print('[!] 해당 프로그램 파일의 위치와 같은 경로에 있는지 확인해주세요 [!]')
        time.sleep(1.5)
        return False
    return True