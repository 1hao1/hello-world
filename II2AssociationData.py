# II2AssociationData
# to write in the data form input information and extra data form storage
from I1PrApi import *
def SavaData(t,k):

    for i in t:
        fn = r'D:\PP_PLAN_LIST\Data' + '\\' + t[i] + '.txt'
        f = open(fn,'a')
        f.write(k[i])
        f.close()
    return

def ExtractData():
    f_n = r'D:\PP_PLAN_LIST\Data'
    result = TimeFind()
    if not os.path.exists(f_n):
        os.makedirs(f_n)
    filename = f_n + '\\' + result + '.txt'
    file2 = open(filename, 'r+')
    filecontent = file2.readlines()
    file2.close()
    print(filecontent)
    return filecontent

if __name__ == '__main__':
    s = ['afkjdfka','wejkfjaskd','sajdfkj']
    print(len(s))