# encoding=utf-8
import time
try:
    my_file = file("C:\\HaxLogs.txt")
    while True:
        line =my_file .readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line
finally:
    my_file.close()
    print "closed!"
