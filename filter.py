# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 15:47
# @Author  : Eric_Douzhixin
# @File    : Filter.py

import re
import os
import time
import csv

print('Author: DZX')
print("""______   _   _   _                 
|  ___| (_) | | | |                
| |_     _  | | | |_    ___   _ __ 
|  _|   | | | | | __|  / _ \ | '__|
| |     | | | | | |_  |  __/ | |   
\_|     |_| |_|  \__|  \___| |_|    
""")
raw_file = input("Input full file name of raw data i.e. waiting_for_processing.csv\n") #'annotation_by_ncbi.csv' #



column = input("Input the column(s) you want to search, start by 1, and separate with ',' i.e. 16,23\nOne column end with nothing, just Enter!\n") # '1' #
if len(column) > 1:
    column_int = column.split(',')
else:
    column_int = column


target_name = input("Input full file name of your targets i.e. target.txt\n") #'GH10 characterized genbank.txt'#
target = []
time1 = time.time()
with open(target_name,'r') as f:
    content_target = f.readlines()
    for i in content_target:
        if i not in target:
            target.append(i.strip('\n'))
        time2 = time.time()
        time3 = time2-time1
        if time3 % 5 ==0:
            print('searching target(s): ',', '.join(target),'\n')
print('Get targets ',len(target))
get_content = []
full_info = []
with open(raw_file,'r') as csvfile:
    content = csv.reader(csvfile)
    for row in content:
        full_info.append(row)
        for i in column_int:
            for t in target:
                if t==row[int(i)-1]:
                    if row not in get_content:
                        get_content.append(row)

print(len(get_content))
print('Content produced successfully!\n')
header = full_info[0]
resultfile = raw_file.split('.')[0]+'_result.csv'
with open(resultfile, 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for i in get_content:
        writer.writerow(i)

print('Mission completed successfully!\n')
os.system('pause')







