import os

#最常用格式的读取标准txt文件函数
def ReadFile_TXT(Path):
    '''
    :param Path: The absolute path of the file on your local computer
    :return: A list of the file's original data sets ---- [[i,j]......]
    '''
    f = open( Path + '.txt' , 'r')
    arr = []
    for eachline in f:  #每一行都是字符串的类型内容
        eachline = eachline.replace("\n", " ").replace("\t", " ").strip()  # 去掉换行和tab符号和收尾的空格
        if '#' not in eachline and "%" not in eachline:
            if "," in eachline:
                eachline = eachline.split(',', 2)  # 将字符串变为列表
            else:
                eachline = eachline.split(' ', 2)  # 将字符串变为列表
            num = len(eachline)  # 将列表中的字符串变为数字
            for i in range(num):
                eachline[i] = int(eachline[i])
            arr.append(eachline)
    f.close()
    return arr


#最常用格式的读取sir数据结果函数
def ReadFile_SIR(Path):
    '''
    :param Path: The absolute path of the file on your local computer
    :return: A dict of the file's original data sets ---- {i:value,......}
    '''
    f = open( Path + '.txt' , 'r' )
    arr = []
    for eachline in f:  # 每一行都是字符串的类型内容
        eachline = eachline.replace("\n", " ").replace("\t", " ").strip()  # 去掉换行和tab符号和收尾的空格
        if '#' not in eachline and "%" not in eachline:
            if "," in eachline:
                eachline = eachline.split(',', 2)  # 将字符串变为列表
            else:
                eachline = eachline.split(' ', 2)  # 将字符串变为列表
            num = len(eachline)  # 将列表中的字符串变为数字
            for i in range(num):
                data = (int(eachline[0]), float(eachline[-1]))
            arr.append(data)
    f.close()
    return dict(arr)


#读取某文件夹下的所有文件名
def ReadFolder(Path,type='.all'):
    '''
    :param Path: The path of the file you want to read
    :param type: Read the file type of the corresponding folder
                  type='.all' ---- Read all files, no matter what type
                  type='.svg' ---- Read a file with a.svg extension
    :return: List of file names
    '''
    filePath = Path+ '/'
    name = os.listdir(filePath)
    if type == '.all':
        return name
    else:
        flie_name = []
        for i in range(len(name)):
            name[i] = (os.path.splitext(name[i])[1], name[i])
            if name[i][0] == type:
                flie_name.append(name[i][1])
        return flie_name
