# mp_cli.py는 모든 화면출력과 메뉴선택을 담당하는 곳입니다.
import os
import time

import value as val

#by VDoring. 2021.06.19
#시작화면을 출력하고 메뉴를 선택하게 합니다.
#리턴값: 1,2
def screenMain():
    while True:
        os.system('cls') # 화면 지우기
        print('< URL-based MusicPlayer 2 >\n')
        print('[1] Play')
        print('[2] Explanation')
        print('\n> ',end='')
        user_select = input()

        if user_select.isdigit(): # 유저 입력값이 숫자로만 이루어진 경우
            if int(user_select) == 1: # 유저 입력값이 1일때
                return 1
            elif int(user_select) == 2: # 유저 입력값이 2일때
                return 2
            else: # 유저 입력값이 1이나 2가 아닐때
                print('[!] Choose from 1 or 2 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)

#by VDoring. 2021.06.19
#전체링크 플레이 모드와 즐겨찾기 플레이 모드 메뉴를 출력하고, 그중 하나를 선택하게 합니다.
#리턴값: 1,2
def screenPlaytype():
    while True:
        os.system('cls') # 화면 지우기
        print('Choose play mode..\n')
        print('[1] All')
        print('[2] Favorite(--) only')
        print('\n> ',end='')
        user_select = input()

        if user_select.isdigit(): # 유저 입력값이 숫자로만 이루어진 경우
            if int(user_select) == 1: # 유저 입력값이 1일때
                return 1
            elif int(user_select) == 2: # 유저 입력값이 2일때
                return 2
            else: # 유저 입력값이 1이나 2가 아닐때
                print('[!] Choose from 1 or 2 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)


#by VDoring. 2021.06.19
#이 프로그램이 무엇인지, 어떻게 작동하는지 안내하는 텍스트를 출력합니다.
#리턴값: 없음
def screenExplanation():
    os.system('cls') # 화면 지우기
    print('< VDoring\'s URL-based MusicPlayer 2 >')
    print('이 프로그램은 .txt파일에 음악 등의 링크를 저장해 작업을 하시는 분들을 위해 보다 편리하게 링크를 실행할 수 있게 도와주는 프로그램입니다.')
    print('{사용법}')
    print('1. Mlist.txt에 자신이 원하는 인터넷 링크를 넣습니다.')
    print('2. Mlist.txt 파일을 저장한 후 해당 프로그램을 실행합니다.')
    print('3. 자신이 원하는 재생 모드를 선택해 사용합니다.')
    print('{참고사항}')
    print('1. Mlist.txt에 링크를 넣을때 메모도 같이 하고 싶다면 \'space\'키를 이용해 링크와 구분하여 메모하면 됩니다.')
    os.system('pause')

#by VDoring. 2021.06.19
#전체링크 플레이 모드의 4개의 세부 플레이 타입 메뉴를 출력하고 선택하게 합니다.
#리턴값: 1,2,3,4
def screenPlaytypeAll():
    while True:
        os.system('cls') # 화면 지우기
        print('Choose \'All\' play mode type..\n')
        print('[1] from Top to Bottom')
        print('[2] from Bottom to Top')
        print('[3] Overlap')
        print('[4] No Overlap')
        print('\n> ',end='')
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
                print('[!] Choose from 1,2,3,4 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)
    

#by VDoring. 2021.06.19
#즐겨찾기 링크 플레이 모드의 4개의 세부 플레이 타입 메뉴를 출력하고 선택하게 합니다.
#리턴값: 1,2,3,4
def screenPlaytypeFav():
    while True:
        os.system('cls') # 화면 지우기
        print('Choose \'Favorite\' play mode type..\n')
        print('[1] from Top to Bottom')
        print('[2] from Bottom to Top')
        print('[3] Overlap')
        print('[4] No Overlap')
        print('\n> ',end='')
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
                print('[!] Choose from 1,2,3,4 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)


#by VDoring. 2021.06.20
#다음 곡을 재생할지 묻는 텍스트를 출력하고 입력을 기다립니다.
#반환값: True, False
def screenAskNextMusic():
     while True:
        os.system('cls') # 화면 지우기
        print('Move on to the next URL? [%d/%d]\n'%(val.mlist_current_links_play_count, val.mlist_available_links_count))
        print('[1] Yes')
        print('[2] No')
        print('\n> ',end='')
        user_select = input()

        if user_select.isdigit():
            if int(user_select) == 1: # Yes일때
                return True
            elif int(user_select) == 2: # No일때
                return False
            else: # 유저 입력값이 1이나 2가 아닐때
                print('[!] Choose from 1,2 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)