files1 = [
    "figure.jpg",
    "song.mp3",
    "video.mp4",
    "figure2.jpg",
    "video2.mp4"
]

files2 = [
    "hinana.jpg",
    "roseliasong.mp3",
    "niji.mp4",
    "m@sterpiece.jpg",
    "vacation.mp4"
]

def find_type(type, file_list):
    print('-'*20)

    for file in file_list:
        if file.endswith('.'+type):
            print(type, "파일 : ", file)

def main():
    find_type("jpg", files1)
    find_type("mp3", files1)
    find_type("mp4", files2)

main()