#!/usr/bin/python3
"""Log Parsing"""
import sys

status_dic = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_size = 0
count = 0
try:
    for line in sys.stdin:
        line_content = line.split(" ")
        if len(line_content) > 5:

            file_size = line_content[-1]
            status = line_content[-2]

            if status in status_dic:
                status_dic[status] += 1

            total_size += int(file_size)
            count += 1

        if count == 10:
            count = 0
            print("File size: {}".format(total_size))
            for k, v in sorted(status_dic.items()):
                if v > 0:
                    print("{}: {}".format(k, v))
except Exception:
    pass
finally:
    print("File size: {}".format(total_size))
    for k, v in sorted(status_dic.items()):
        if v > 0:
            print("{}: {}".format(k, v))
