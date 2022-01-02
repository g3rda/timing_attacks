import os
import string
import datetime

timeelapsed = [0]
result = 'different'

def try_next(arr):
    global timeelapsed
    global result
    tmp = []
    for i in string.ascii_lowercase:
        a = datetime.datetime.now()
        result = os.popen('python3 string_comparison.py '+''.join(arr)+i).read().strip()
        b = datetime.datetime.now()
        c = b - a
        if result == 'same':
            print(c.microseconds, ":", end = ' ')
            return string.ascii_lowercase.index(i)
        tmp += [c.microseconds]
    if max(tmp) - timeelapsed[-1] < 100000:
        return -1
    print(max(tmp), ":", end = ' ')
    timeelapsed += [max(tmp)//100000 * 100000]
    return tmp.index(max(tmp))


arr = []
while result!='same':
    next = try_next(arr)
    if next!= -1:
        arr += string.ascii_lowercase[next]
    else:
        timeelapsed = timeelapsed[:-1]
        arr = arr[:-1]
    print(''.join(arr))

print("\nSecret:",''.join(arr))
