# I2PaLayout
# For the arrangement of one page

def HeaderType(x):
    n = {}
    n[1] = '+'
    n[2] = '-'
    n[3] = '_'
    n[4] = '='
    n[0] = '__PLAN_LIST__'
    s = ''
    s= n[0]
    for i in range(10):
        s = n[x] + s
        s = s + n[x]
    return s

def LineType(x):
    n = {}
    n[1] = '+'
    n[2] = '-'
    n[3] = '_'
    n[4] = '='
    s = ''
    s = n[x] * 32
    return s

def EnderType(x):
    n = {}
    n[1] = '+'
    n[2] = '-'
    n[3] = '_'
    n[4] = '='
    n[0] = '__ONCE_BEGIN_NEVER_STOP__'
    s = ''
    s = n[x] * 3 + n[0] + n[x] * 3
    return s
def AskType(y,z):
    n = {}
    n[1] = 'Degree'
    n[2] = 'Suggestion'
    d = {}
    d[1] = 'leisure'
    d[2] = 'medium'
    d[3] = 'busy'
    s = {}
    s[1] = 'reclaim'
    s[2] = 'consolidate'
    s[3] = 'divergent'
    r = {}
    r[1] = n[1] + ': ' + d[y] + '\n'
    r[2] = n[2] + ': ' + s[z] + '\n'
    return r


if __name__ == '__main__':
    print(HeaderType(3))
    print(LineType(3))
    print(LineType(3))
    print(EnderType(3))
    r = AskType(1,2)
    print(r[1],r[2])