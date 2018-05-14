from datetime import datetime
import os
import sys
import html

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23,25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# right_this_minute = datetime.today().minute
#
# print('Today is ' + datetime.today().__str__())
#
# if right_this_minute in odds:
#     print("This minute seems a little odd (%d)" % right_this_minute)
# else:
#     print("Not an odd minute (%d)" % right_this_minute)
#
# where_i_am = os.getcwd()
# print("My current path is " + where_i_am)
# print("My platform is  " + sys.platform)
# print("HOME  " + os.getenv('TEMP').__str__())
#
#
# print(html.escape('This HTML fragment contains a <script>script</script> tag.'))
# print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))

for i in range(5):
    i += 1
    print(i)
