# II3OutputData
# to change the type of data for the print of printer (bytes)

def ChangeType(s):
    s = bytes(s,'utf-8')
    return s

if __name__ == '__main__':
    s = 'sdjkajgj'
    print(ChangeType(s))