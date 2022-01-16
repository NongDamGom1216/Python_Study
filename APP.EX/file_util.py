# 파이썬 자료형을 그대로 저장하고, 그대로 복원한다.
# 반드시 binary 모드로 오픈해야 한다.
# 파일 모듈, pickle
# python 끼리만 사용가능하다.

import pickle, os
import json #dat 파일이 아니라 txt로

def save(fpath, data):
    try:
        with open(fpath, 'wb') as file:
            pickle.dump(data, file)

    except Exception as e:
        print(f"{fpath} 파일 쓰기에 실패했습니다.")
        print(e)

def save_json(fpath, data):
    try:
        with open(fpath, 'wt') as file:
            json.dump(data, file)

    except Exception as e:
        print(f"{fpath} 파일 쓰기에 실패했습니다.")
        print(e)


def load(fpath):
    try:
        with open(fpath, 'rb') as file:
            data = pickle.load(file)
            return data
    except:
        print(f"{fpath} 파일 읽기에 실패했습니다.")

def load_json(fpath):
    try:
        with open(fpath, 'rt') as file:
            data = json.load(file)
            return data
    except:
        print(f"{fpath} 파일 읽기에 실패했습니다.")


def get_file_list(dir, ext):
    files = os.listdir(dir)
    file_list = list(filter(lambda name: name.endswith(ext), files))
    return file_list