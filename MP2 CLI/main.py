# made by VDoring. || https://github.com/VDoring

# main.py는 모든 프로그램 기능 흐름의 중심이 되는 곳입니다.
import common_cli as cli
import play_all_1_TopBottom as pa1
import play_all_2_BottomTop as pa2
import play_all_3_RandomOverlap as pa3
import play_all_4_RandomNoOverlap as pa4
import play_fav_1_TopBottom as pf1
import play_fav_2_BottomTop as pf2
import play_fav_3_RandomOverlap as pf3
import play_fav_4_RandomNoOverlap as pf4

# 메인화면
while True:
    user_select = cli.screenMain() # Play와 Explanation에서 선택.
    if user_select == 1: # Play를 선택할경우
        user_select = cli.screenPlaytype() # 전체링크 플레이모드와 즐겨찾기 플레이모드 중 선택.
        if user_select == 1: # 전체링크 플레이모드를 선택할경우
            user_select = cli.screenPlaytypeAll()
            if user_select == 1: # [1] from Top to Bottom를 선택할경우
                pa1.playTopBottom()
            elif user_select == 2: # [2] from Bottom to Top를 선택할경우
                pa2.playBottomTop()
            elif user_select == 3: # [3] Overlap을 선택할경우
                pa3.playRandomOverlap()
            elif user_select == 4: # [4] No Overlap을 선택할경우
                pa4.playRandomNoOverlap()

        else: # 즐겨찾기 플레이모드를 선택할 경우
            user_select = cli.screenPlaytypeFav()
            if user_select == 1: # [1] from Top to Bottom를 선택할경우
                pass
            elif user_select == 2: # [2] from Bottom to Top를 선택할경우
                pass
            elif user_select == 3: # [3] Overlap을 선택할경우
                pass
            elif user_select == 4: # [4] No Overlap을 선택할경우
                pass

    else: # Explanation을 선택할경우
        cli.screenExplanation()