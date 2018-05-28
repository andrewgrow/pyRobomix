from datetime import datetime
from time import sleep
from random import randint

import os
import sys
import html

# odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55,
#         57, 59]
#
# print('Today is ' + datetime.today().__str__())
#
# for i in range(15):
#     right_this_minute = datetime.today().minute
#     if right_this_minute in odds:
#         print("This minute seems a little odd (%d)" % right_this_minute)
#     else:
#         print("Not an odd minute (%d)" % right_this_minute)
#     randomTime = randint(1, 60)
#     print('Wait time ' + randomTime.__str__())
#     sleep(randomTime)


#
# where_i_am = os.getcwd()
# print("My current path is " + where_i_am)
# print("My platform is  " + sys.platform)
# print("HOME  " + os.getenv('TEMP').__str__())
#
#
# print(html.escape('This HTML fragment contains a <script>script</script> tag.'))
# print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))

# word = 'bottles'
# for beer in range(99, 0, -1):
#     print(beer, word, 'of beer on the wall.')
#     print(beer, 'of beer.')
#     print('Take one down.')
#     print('Pass it around.')
#     if beer == 1:
#         print('No more bottle of beer on the wall.')
#     else:
#         new_beer = beer - 1
#         if new_beer == 1:
#             word = 'bottle'
#         print(new_beer, word, 'of beer on the wall.')
#     print()

# vowels = ['a', 'e', 'i', 'o', 'u']
# word = "Milliways"
# found = []
# print('length of found =', len(found))
#
# for letter in word:
#     if letter in vowels:
#         print(letter)
#     else:
#         found.append(letter)
#
# print('length of found =', len(found))
# print(found.pop())
# print('length of found =', len(found))
#
# found.extend(vowels)
#
# print('length of found =', len(found))

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)


