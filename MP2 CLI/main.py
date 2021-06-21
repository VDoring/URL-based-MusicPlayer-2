# made by VDoring. || https://github.com/VDoring

# main.py는 모든 프로그램 기능 흐름의 중심이 되는 곳입니다.
import mp_cli as cli

# 메인화면
user_select = cli.screenMain() # Play와 Explanation에서 선택.
if user_select == 1: # Play를 선택할경우
    user_select = cli.screenPlaytype() # 전체링크 플레이모드와 즐겨찾기 플레이모드 중 선택.
    if user_select == 1: # 전체링크 플레이모드를 선택할경우
        cli.screenPlaytypeAll()
    else: # 즐겨찾기 플레이모드를 선택할 경우
        cli.screenPlaytypeFav()

else: # Explanation을 선택할경우
    cli.screenExplanation()