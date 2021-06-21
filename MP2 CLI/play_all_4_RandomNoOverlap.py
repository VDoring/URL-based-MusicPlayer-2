import os
import time
import random

import common_cli as cli
import common_value as val
import common_func as func

#by VDoring. 2021.06.21
#전체플레이 모드->중복재생 불가능한 랜덤모드를 실행합니다.
#리턴값:없음
def playRandomNoOverlap():
    # Mlist.txt 파일 존재 확인 #
    is_file_available = func.checkMlistFile()
    if is_file_available == False: # 파일이 인식되지 않는다면
        return

    # 유효한 링크 수 파악 #
    mlist = open('Mlist.txt','r', encoding='utf-8') # 파일 열기
    mlist_all_lines_index = mlist.readlines() # 파일의 모든 글자들을 리스트 형식으로 저장
    mlist_lines_count = len(mlist_all_lines_index) # 파일 속 총 라인 개수
    mlist_available_links_locate = [] # 파일 속 사용가능한 링크인 라인의 위치
    for i in range(len(mlist_all_lines_index)): # 파일의 글자 라인 수 만큼 반복하면서 링크가 아닌 것을 파악하고, 총 링크갯수 카운트에서 제외
        if 'http' in mlist_all_lines_index[i]: # 링크인 경우
            mlist_available_links_locate.append(i) # 링크가 들어있는 위치를 리스트에 저장
            val.mlist_available_links_count += 1 # 파일 속 사용가능한 링크의 개수 +1
    random.shuffle(mlist_available_links_locate) # 랜덤재생을 위해 리스트 섞기

     # 링크 실행 #
    mlist.seek(0) # 파일 라인을 처음 위치로 이동
    for i in mlist_available_links_locate: # 사용가능한 링크 수만큼 반복
        line_index = mlist_all_lines_index[i] # 파일의 한 라인의 텍스트를 저장
        link = line_index.split() # 띄어쓰기 기준으로 문자열 분리
        os.system('start chrome --incognito ' + link[0]) # 링크가 포함된 크롬 시크릿모드 실행 명령어 실행
        val.mlist_current_links_play_count += 1 # 지금까지 재생한 링크의 개수 +1
        if val.mlist_available_links_count == val.mlist_current_links_play_count: # 지금까지 재생한 링크의 수와 사용가능한 링크의 수가 같다면(링크를 다 재생했다면)
            return
        user_select = cli.screenAskNextMusic() # 다음 곡을 재생할건지 묻기
        if user_select == False: # 사용자가 그만 듣겠다고 답하면
            return

    val.clearCommonValue() # 공통으로 사용된 변수 초기화 -> 작동안함. 이유는 모르겠음