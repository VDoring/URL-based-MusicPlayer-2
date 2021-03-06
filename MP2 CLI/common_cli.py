# common_cli.py는 모든 화면출력과 메뉴선택을 담당하는 곳입니다.
import os
import time

import common_value as val

#by VDoring. 2021.06.19
#시작화면을 출력하고 메뉴를 선택하게 합니다.
#리턴값: 1,2
def screenMain():
    while True:
        os.system('mode con cols=40 lines=11') # 타이틀화면 화면 크기 설정
        os.system('title MP2 - Title') # 윈도우타이틀 설정

        print('\n - -<-< URL-based MusicPlayer 2 >->- - ')
        print('\n\n               [1] Play')
        print('\n               [2] Info')
        print('\n               > ',end='')
        user_select = input()

        if user_select.isdigit(): # 유저 입력값이 숫자로만 이루어진 경우
            if int(user_select) == 1: # 유저 입력값이 1일때
                return 1
            elif int(user_select) == 2: # 유저 입력값이 2일때
                return 2
            else: # 유저 입력값이 1이나 2가 아닐때
                print('       [!] Choose from 1 or 2 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('     [!] Please enter a number! [!]')
            time.sleep(0.75)

#by VDoring. 2021.06.19
#전체링크 플레이 모드와 즐겨찾기 플레이 모드 메뉴를 출력하고, 그중 하나를 선택하게 합니다.
#리턴값: 1,2
def screenPlaytype():
    while True:
        os.system('cls') # 화면 지우기
        os.system('title MP2 - Set mode....') # 윈도우타이틀 설정

        print('\n         < Choose play mode.. >')
        print('\n\n             [1] All')
        print('\n             [2] Favorite')
        print('\n                > ',end='')
        user_select = input()

        if user_select.isdigit(): # 유저 입력값이 숫자로만 이루어진 경우
            if int(user_select) == 1: # 유저 입력값이 1일때
                return 1
            elif int(user_select) == 2: # 유저 입력값이 2일때
                return 2
            else: # 유저 입력값이 1이나 2가 아닐때
                print('       [!] Choose from 1 or 2 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('     [!] Please enter a number! [!]')
            time.sleep(0.75)


#by VDoring. 2021.06.19
#이 프로그램이 무엇인지, 어떻게 작동하는지 안내하는 텍스트를 출력합니다.
#리턴값: 없음
def screenExplanation():
    os.system('mode con cols=130 lines=25') # 설명화면 화면 크기 설정
    os.system('title MP2 - Explanation') # 윈도우타이틀 설정

    print('\n- - -<-< VDoring\'s URL-based MusicPlayer 2 >->- - --------------------------------------------------------------------------------')
    print('\n이 프로그램은 .txt파일에 음악 등의 링크를 저장해 특정 작업을 하시는 분들을 대상으로 빠른 링크 실행을 도와주는 프로그램입니다.')
    print('\n\n{사용법}')
    print('1. Mlist.txt에 자신이 원하는 인터넷 링크를 넣습니다.')
    print('2. Mlist.txt 파일을 저장한 후 해당 프로그램을 실행합니다.')
    print('3. 자신이 원하는 재생 모드를 선택합니다.')
    print('(자세한 설명은 GitHub을 참조하세요)')
    print('\n{참고사항}')
    print('1. Mlist.txt에 링크를 넣을때 메모도 같이 하고 싶다면 \'space\'키를 이용해 링크와 구분해야합니다!')
    print('\n{프로젝트 링크}')
    print('GitHub: https://github.com/VDoring/URL-based-MusicPlayer-2\n\n\n')
    os.system('pause')

#by VDoring. 2021.06.19
#전체링크 플레이 모드의 4개의 세부 플레이 타입 메뉴를 출력하고 선택하게 합니다.
#리턴값: 1,2,3,4
def screenPlaytypeAll():
    while True:
        os.system('mode con cols=42 lines=14') # 화면 지우기
        os.system('title MP2 - Set mode..') # 윈도우타이틀 설정

        print('\n    < Choose \'All\' play mode type.. >    ')
        print('\n\n          [1] from Top to Bottom')
        print('\n          [2] from Bottom to Top')
        print('\n          [3] Random Overlap')
        print('\n          [4] Random No Overlap')
        print('\n                 > ',end='')
        user_select = input()

        if user_select.isdigit(): # 유저 입력값이 숫자로만 이루어진 경우
            if int(user_select) == 1: # 유저 입력값이 1일때
                return 1
            elif int(user_select) == 2: # 유저 입력값이 2일때
                return 2
            elif int(user_select) == 3: # 유저 입력값이 3일때
                return 3
            elif int(user_select) == 4: # 유저 입력값이 4일때
                return 4
            else: # 유저 입력값이 1,2,3,4가 아닐때
                print('       [!] Choose from 1,2,3,4 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('      [!] Please enter a number! [!]')
            time.sleep(0.75)
    

#by VDoring. 2021.06.19
#즐겨찾기 링크 플레이 모드의 4개의 세부 플레이 타입 메뉴를 출력하고 선택하게 합니다.
#리턴값: 1,2,3,4
def screenPlaytypeFav():
    while True:
        os.system('mode con cols=46 lines=14') # 화면 지우기
        os.system('title MP2 - Set mode..') # 윈도우타이틀 설정

        print('\n    < Choose \'Favorite\' play mode type.. > ')
        print('\n\n            [1] from Top to Bottom')
        print('\n            [2] from Bottom to Top')
        print('\n            [3] Random Overlap')
        print('\n            [4] Random No Overlap')
        print('\n                   > ',end='')
        user_select = input()

        if user_select.isdigit(): # 유저 입력값이 숫자로만 이루어진 경우
            if int(user_select) == 1: # 유저 입력값이 1일때
                return 1
            elif int(user_select) == 2: # 유저 입력값이 2일때
                return 2
            elif int(user_select) == 3: # 유저 입력값이 3일때
                return 3
            elif int(user_select) == 4: # 유저 입력값이 4일때
                return 4
            else: # 유저 입력값이 1,2,3,4가 아닐때
                print('          [!] Choose from 1,2,3,4 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('        [!] Please enter a number! [!]')
            time.sleep(0.75)


#by VDoring. 2021.06.20
#다음 곡을 재생할지 묻는 텍스트를 출력하고 입력을 기다립니다.
#반환값: True, False
def screenAskNextMusic():
     while True:
        os.system('mode con cols=40 lines=11') # 화면 지우기
        os.system('title Playing..') # 윈도우타이틀 설정

        print('\n      Move on to the next URL? [%d/%d]'%(val.mlist_current_links_play_count, val.mlist_available_links_count))
        print('\n\n                [1] Yes')
        print('\n                [2] No')
        print('\n                  > ',end='')
        user_select = input()

        if user_select.isdigit():
            if int(user_select) == 1: # Yes일때
                return True
            elif int(user_select) == 2: # No일때
                return False
            else: # 유저 입력값이 1이나 2가 아닐때
                print('         [!] Choose from 1,2 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('     [!] Please enter a number! [!]')
            time.sleep(0.75)