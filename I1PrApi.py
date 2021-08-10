# I1PrAPI
# For the collection of printer api

import os
import win32print
from datetime import datetime,date,time,timedelta
import string

def TimeFind():
    now = datetime.now()
    now = str(now)
    return now[0:10]

def DirSearcher():
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

def printer(content):
    printer_name = win32print.GetDefaultPrinter()
# raw_data could equally be raw PCL/PS read from
# some print-to-file operation
#
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("input data", None, None))
        try:
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, content)
            win32print.EndPagePrinter(hPrinter)
        finally:
            win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)

if __name__=='__main__':
    s = TimeFind()
    content = bytes(s+'\n','utf-8')
    printer(content)
    print(content)