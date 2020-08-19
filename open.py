# 打开dict.txt文件
with  open('dict.txt') as f:
    # 读取dict文件
    d = list()
    d = f.readlines()
    for x in d:
        print(x)
