# IIInputData
# This is the input section

from datetime import datetime,date,time,timedelta
import time

def ArramgeInfo(keyword,planday):
    '''input keyword for the main task;
    input planday for the number of days;
    input interval for the leap of plan.'''
    s = {}
    percentage = {}
    for i in range(1,planday+1):
        percentage[i] = str(int((100*i/int(planday)))) + '%'
    for i in range(1,planday+1):
        s[i] = keyword + '      ' + percentage[i] + '\n'
    return s

def InputDataBelonging(planday,interval):
    n = {}
    m = {}
    m[0] = 0
    for i in range(1,planday):
        m[i] = interval  + m[i-1] + 1
    for i in range(1,planday+1):
        now = datetime.now()
        delta = timedelta(days=m[i-1])
        n_days = now + delta
        n_days = str(n_days)
        n[i] = n_days[0:10]
    return n

def KeyTimeCombination(keyword,planday,interval):
    t = InputDataBelonging(planday,interval)
    k = ArramgeInfo(keyword,planday)
    n = {}
    for i in range(1,planday+1):
        n[t[i]] = k[i]
    return n

if __name__ == '__main__':

    print(InputDataBelonging(10,0))
    x = KeyTimeCombination('abdd',10,4)
    print(x)
