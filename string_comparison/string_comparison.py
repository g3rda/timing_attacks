import datetime
import time
import sys

def compareStrings(str1, str2):
    for i in range(len(str1)):
        try:
            if str1[i] != str2[i]:
                return False
        except:
            return False
        time.sleep(0.1)
    return True

secret = "snow"

i = sys.argv[1]

result = compareStrings(secret, i)
if result:
    print("same")
else:
    print("different")

#
# a = datetime.datetime.now()
# result = compareStrings("polarbear", "polaroid")
# b = datetime.datetime.now()
# c = b - a
# print("compareStrings(\"polarbear\", \"polaroid\") takes", c.microseconds, "microseconds.")
#
# a = datetime.datetime.now()
# result = compareStrings("hello", "goodbye")
# b = datetime.datetime.now()
# c = b - a
# print("compareStrings(\"hello\", \"goodbye\") takes", c.microseconds, "microseconds.")
