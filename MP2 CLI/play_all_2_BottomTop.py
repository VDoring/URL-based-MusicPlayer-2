import os
import time

import common_cli as cli
import common_value as val

#by VDoring. 2021.06.21
#전체플레이 모드-아래에서 위로 곡을 실행합니다.
#리턴값:없음
def playBottomTop():

    # 유효한 링크 수 파악 #
    mlist = open('Mlist.txt','r', encoding='utf-8') # 파일 열기
    mlist_all_lines_index = mlist.readlines() # 파일의 모든 글자들을 리스트 형식으로 저장
    mlist_lines_count = len(mlist_all_lines_index) # 파일 속 총 라인 개수
    mlist_available_links_locate = [] # 파일 속 사용가능한 링크인 라인의 위치
    for i in range(len(mlist_all_lines_index)): # 파일의 글자 라인 수 만큼 반복하면서 링크가 아닌 것을 파악하고, 총 링크갯수 카운트에서 제외
        if 'http' in mlist_all_lines_index[i]: # 링크인 경우
            mlist_available_links_locate.append(i) # 링크가 들어있는 위치를 리스트에 저장
            val.mlist_available_links_count += 1 # 파일 속 사용가능한 링크의 개수 +1