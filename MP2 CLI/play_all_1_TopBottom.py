import os
import time

#by VDoring. 2021.06.20
#전체플레이 모드-위에서 아래순서로 곡을 실행합니다.
#리턴값:없음
def playTopBottom():
    # Mlist.txt 파일 존재 확인 #
    is_file_available = os.path.isfile('Mlist.txt') # Mlist.txt 파일이 올바른 위치에 존재하는지 확인
    if is_file_available == False: # Mlist.txt 파일이 없다면
        print('[!] Mlist.txt 파일을 찾을 수 없습니다 [!]')
        print('[!] 해당 프로그램 파일의 위치와 같은 경로에 있는지 확인해주세요 [!]')
        time.sleep(1.5)
        return

    # 유효한 링크 수 파악 #
    mlist = open('Mlist.txt','r', encoding='utf-8') # 파일 열기
    mlist_all_lines_index = mlist.readlines() # 파일의 모든 글자들을 리스트 형식으로 저장
    mlist_lines_count = len(mlist_all_lines_index) # 파일 속 총 라인 개수
    mlist_available_links_locate = [] # 파일 속 링크인 라인의 위치
    for i in range(len(mlist_all_lines_index)): # 파일의 글자 라인 수 만큼 반복하면서 링크가 아닌 것을 파악하고, 총 링크갯수 카운트에서 제외
        if 'http' in mlist_all_lines_index[i]: # 링크가 아닌 경우
            mlist_available_links_locate.append(i)

    # 링크 실행 #
    mlist.seek(0) # 파일 라인을 처음 위치로 이동
    for i in mlist_available_links_locate: # 사용가능한 링크 수만큼 반복
        line_index = mlist_all_lines_index[i]
        link = line_index.split()
        os.system('start chrome --incognito ' + link[0]) # 링크가 포함된 크롬 시크릿모드 실행 명령어 실행
        

    #디버그용
    #print(mlist_available_links_count)
    #time.sleep(100)