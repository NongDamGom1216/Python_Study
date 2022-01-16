# MP3Player
# 데이터 : 노래 목록, 현재 노래
# 기능 : 목록, 선곡, 재생, 이전, 다음 ---> 메뉴
# 객체 지향형을 사용하면 전역 변수의 사용을 피할 수 있다.

from baseapp import Application
import eyed3, os, sys
from pygame import mixer
from file_util import get_file_list


class MP3Player(Application):
    def __init__(self) -> None:
        super().__init__("MP3Player")
        self.DIR_PATH = '/Users/hyunjinjeong/Desktop' # 음악 파일 디렉토리
        self.song_list = [] # 재생 목록
        self.song = None # 현재 재생중인 파일
        self.current_index = -1 # 현재 재생 파일의 인덱스

        # 멤버 초기화
    # 메뉴 구성, create_menu(), override
    def create_menu(self):
        self.menu.add_menu('목록', self.print_list)
        self.menu.add_menu('재생', self.play)
        self.menu.add_menu('다음', self.play_next)
        self.menu.add_menu('이전', self.play_prev)
        self.menu.add_menu('일시정지', self.stop)
        self.menu.add_menu('종료', self.exit)

    def init(self): # 오버라이딩
        super().init() # 내부에서 create_menu() 호출
        
        mixer.init()
        self.song_list = get_file_list(self.DIR_PATH, '.mp3')
    
    def print_tag(self, file_path):
        try:
            self.file_path = file_path
            s = eyed3.load(self.file_path)
            print(f'가수: {s.tag.artist}')
            print(f'앨범: {s.tag.album}')
            print(f'곡명: {s.tag.title}')
        except:
            print(self.file_path)

    def print_list(self):
        for ix, song in enumerate(self.song_list):
            print(f'{ix} {song}')
        print()
    
    def play_music(self, index):
        #이전에 재생 중이면 먼저 정지
        if self.song: #None이 아니면이라는 뜻
            self.song.stop()

        song_path = os.path.join(self.DIR_PATH, self.song_list[index]) # 절대 경로로 주어야한다.
        self.song = mixer.Sound(song_path) #self.song은 Sound 객체의 인스턴스
        self.song.play()
    
        self.print_tag(song_path)
    
    def play(self):
        self.current_index = int(input('선곡 : '))

        self.play_music(self.current_index)
    
    def play_next(self):
        self.current_index += 1

        if self.current_index == len(self.song_list):
            self.current_index = 0

        self.play_music(self.current_index)
    
    def play_prev(self):
        if self.current_index == 0:
            self.current_index = len(self.song_list)
    
        self.current_index -= 1

        self.play_music(self.current_index)

    def stop(self):
        if self.song: #None이 아니면이라는 뜻
            self.song.stop()
        self.song = None
    
    def exit(self):
        sys.exit(0)

def main():
    app = MP3Player()
    app.run()

main()