# mp_cli.py는 모든 화면출력과 메뉴선택을 담당하는 곳입니다.
import os
import time

#by VDoring. 2021.06.19
#시작화면을 출력하고 메뉴를 선택하게 합니다.
#리턴값: 1,2
def screenMain():
    while True:
        print('< URL-based Player2 >\n')
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
                os.system('cls')
        else: # 입력값에 문자가 들어갔을 경우
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)
            os.system('cls')

#by VDoring. 2021.06.19
#전체링크 플레이 모드와 즐겨찾기 플레이 모드 메뉴를 출력하고, 그중 하나를 선택하게 합니다.
#리턴값: 1,2
def screenPlaytype():
    pass

#by VDoring. 2021.06.19
#이 프로그램이 무엇인지, 어떻게 작동하는지 안내하는 텍스트를 출력합니다.
#리턴값: 없음
def screenExplanation():
    pass

#by VDoring. 2021.06.19
#전체링크 플레이 모드의 4개의 세부 플레이 타입 메뉴를 출력하고 선택하게 합니다.
#리턴값: 1,2,3,4
def screenPlaytypeAll():
    pass

#by VDoring. 2021.06.19
#즐겨찾기 링크 플레이 모드의 4개의 세부 플레이 타입 메뉴를 출력하고 선택하게 합니다.
#리턴값: 1,2,3,4
def screenPlaytypeFav():
    pass