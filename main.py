# This is a new plan about making full use of my printer.
# It can be divide into two main parts, which is related to the real world and the virtual world.
# For the each part, there will be several subordinates who are responsible for concrete function.
# I The Real World. About the printer API, and the layout of page.
# II The Virtual World. About the input of data, the output of data, and association of data.

from I1PrApi import *
from I2PaLayout import *
from  IIInputData import *
from  II2AssociationData import *
from  II3OutputData import *

mode = input('Please enter the mode: (p or w)')
if mode == 'p':
    head = HeaderType(3)
    head_b = ChangeType(head)
    printer(head_b)
    time_now = 'Today Date' + ':'+TimeFind() + '\n'
    time_now_b = ChangeType(time_now)
    printer(time_now_b)
    operator = 'Operator:hao xiangyang\n'
    operator_b = ChangeType(operator)
    printer(operator_b)
    line = LineType(3)
    line_b =ChangeType(line)
    printer(line_b)
    filecontent = ExtractData()
    l = len(filecontent)
    for i in range(l):
        filecontent_c =str(filecontent[i])
        filecontent_b = ChangeType(filecontent_c)
        printer(filecontent_b)
    line = LineType(3)
    line_b = ChangeType(line)
    printer(line_b)
    if l<=5:
        y = 1
    elif l>5 and l<=10:
        y = 2
    else:
        y = 3
    DS = AskType(y,y)
    for i in DS:
        DS_b = ChangeType(DS[i])
        printer(DS_b)
    ender = EnderType(3)
    ender_b = ChangeType(ender)
    printer(ender_b)
    line = LineType(3)
    line_b = ChangeType(line)
    printer(line_b)
    line = LineType(3) + '\n' + '\n'
    line_b = ChangeType(line)
    printer(line_b)

else:
    keyword = input('keyword= ')
    planday = input('planday= ')
    planday = int(planday)
    interval = input('interval= ')
    interval = int(interval)
    k = ArramgeInfo(keyword,planday)
    t = InputDataBelonging(planday,interval)
    SavaData(t,k)
    print('Complete...')
