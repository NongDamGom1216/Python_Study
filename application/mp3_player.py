import os, sys, eyed3
from pygame import mixer
from file_util import get_file_list

DIR_PATH = '/Users/hyunjinjeong/Desktop'
song_list = []
song = None
current_index = -1

# 메뉴
# 목록 재생 정지 이전 다음 종료

def print_tag(file_path):
    try:
        s = eyed3.load(file_path)
        print(f'가수: {s.tag.artist}')
        print(f'앨범: {s.tag.album}')
        print(f'곡명: {s.tag.title}')
    except:
        print(file_path)

def init():
    global song_list
    mixer.init()
    song_list = get_file_list(DIR_PATH, '.mp3')

def print_list():
    # 인덱스 번호를 붙이고 출력
    for ix, song in enumerate(song_list):
        print(f'{ix} {song}')
    print()

def play_music(index):
    global song

    #이전에 재생 중이면 먼저 정지
    if song: #None이 아니면이라는 뜻
        song.stop()

    song_path = os.path.join(DIR_PATH, song_list[index]) # 절대 경로로 주어야한다.
    song = mixer.Sound(song_path)
    song.play()
    
    print_tag(song_path)

# 선곡해서 재생하기
def play():
    global current_index, song
    current_index = int(input('선곡 : '))

    play_music(current_index)

def stop():
    global song
    if song: #None이 아니면이라는 뜻
        song.stop()
    song = None

def play_prev():
    global song, current_index
   
    if current_index == 0:
        current_index = len(song_list)
    
    current_index -= 1

    play_music(current_index)


def play_next():
    global song, current_index
    current_index += 1

    if current_index == len(song_list):
        current_index = 0

    play_music(current_index)
    

def exit():
    sys.exit(0)

def print_menu():
    print('-'*50)
    print('목록    재생    정지    이전    다음    종료')
    print('-'*50)

def main():
    init()
    while True:
        print_menu()
        select = input("선택: ")
        if select == '목록':
            print_list()
        elif select == '재생':
            play()
        elif select == '정지':
            stop()
        elif select == '이전':
            play_prev()
        elif select == '다음':
            play_next()
        elif select == '종료':
            exit()
        else:
            print('명령을 다시 입력하십시오.')

main()