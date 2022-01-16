from file_util import load, save, load_json, save_json


def main():
    #datas = [123, 45, 67, 89]
    datas = [
        {
        "name" : "히나나",
        "age" : 20
    }, {
        "name": "하지메",
        "age" : 22
    }
    ]

    #save('pickle.dat', datas) #binary 데이터
    save_json('json1.json', datas)
    
    content = load_json('json1.json')
    print(content)

main()