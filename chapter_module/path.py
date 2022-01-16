import sys

for path in sys.path:
    print(path)

# sys 모듈의 path 리스트를 먼저 조사
# 현재 워킹 디렉토리가 제일 먼저 조사됨
# 그 다음 PYTHONPATH 환경 변수의 디렉토리 검색