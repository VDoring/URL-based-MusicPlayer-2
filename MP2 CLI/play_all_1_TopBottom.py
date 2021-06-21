import os
import time

#by VDoring. 2021.06.20
#전체플레이 모드-위에서 아래순서로 곡을 실행합니다.
#리턴값:없음
def playTopBottom():
    is_file_available = os.path.isfile('Mlist.txt') # Mlist.txt 파일이 올바른 위치에 존재하는지 확인
    if is_file_available == False: # Mlist.txt 파일이 없다면
        print('[!] Mlist.txt 파일을 찾을 수 없습니다 [!]')
        print('[!] 해당 프로그램 파일의 위치와 같은 경로에 있는지 확인해주세요 [!]')
        time.sleep(1.5)
        return

    mlist = open('Mlist.txt','r', encoding='utf-8') # 파일 열기
    mlist_all_lines_index = mlist.readlines() # 파일의 모든 글자들을 리스트 형식으로 저장
    mlist_lines_count = len(mlist_all_lines_index) # 파일 속 총 라인 개수
    mlist_not_available_lines_count = 0 # 파일 속 링크가 아닌 라인 개수
    for i in range(len(mlist_all_lines_index)): # 파일의 글자 라인 수 만큼 반복하면서 링크가 아닌 것을 파악하고, 총 링크갯수 카운트에서 제외
        if ('http' not in mlist_all_lines_index[i]) or ('https' not in mlist_all_lines_index[i]): # 링크가 아닌 경우
            mlist_not_available_lines_count += 1
    mlist_available_lines_count = mlist_lines_count - mlist_not_available_lines_count # 파일 속 사용가능한 링크가 있는 라인 수

    #디버그용
    print(mlist_available_lines_count)
    time.sleep(100)