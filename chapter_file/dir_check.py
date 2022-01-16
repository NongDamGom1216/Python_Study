import os

files = os.listdir('/Users/hyunjinjeong/Desktop/Roselia')
for i in files:
    print(i)

print("-"*50)

# 폴더에서 mp3파일만 출력


def get_file_list(dir, ext):
    files = os.listdir(dir)
    file_list = list(filter(lambda name: name.endswith(ext), files))
    return file_list


def main():
    import os
    DIR_PATH = '/Users/hyunjinjeong/Desktop'

    songs = get_file_list(DIR_PATH, '.mp3')

    for i in songs:
        print(i)

    #절대 경로로 출력
    for i in songs:
        print(f'{DIR_PATH}:{i}')
        print(os.path.join(DIR_PATH, i)) #기억해두기
        print(os.path.getsize(DIR_PATH))

main()