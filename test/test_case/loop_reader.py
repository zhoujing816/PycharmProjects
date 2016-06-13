# coding=utf-8
import csv
import codecs
my_file = "C:\\test.csv"
data = csv.reader(file(my_file,'rb'))
for user in data:
    print ", ".join(user).decode('gb2312')
