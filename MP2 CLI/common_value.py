# common_value.py는 공통으로 사용되는 변수를 정리하는 곳입니다.

# 사용 후 초기화가 필요한 변수
mlist_available_links_count = 0 # 파일 속 사용가능한 링크의 개수
mlist_current_links_play_count = 0 # 지금까지 재생한 링크의 개수

#by VDoring. 2021.06.20
#공통으로 사용되는 변수의 값 초기화
#리턴값: 없음
def clearCommonValue():
    mlist_available_links_count = 0
    mlist_current_links_play_count = 0