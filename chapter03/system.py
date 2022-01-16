import sys

def main():
    print("버전: ", sys.version)
    print("플랫폼: ", sys.platform)
    print("바이트 순서: ", sys.byteorder)
    print("모듈 경로: ")
    for p in sys.path: # 디렉토리에서 찾을 때까지 검색
        print(p)
    sys.exit(0) # 0 : 정상종료

main()