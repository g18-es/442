import mhashlib
import time

# problem 1
# original string: YR93B4D9D8F888E671A9C1423902D70D81AC8826E7
# hash functions to try: sha1, sha0, ripemd160, haval160, tiger160

p = '93b4d9d8f888e671a9c1423902d70d81ac8826e7'
j = 0

while j < 10000:
  if j <= 9:
    i = '000' + str(j)
  elif j <= 99 and j > 9:
    i = '00' + str(j)
  elif j <= 999 and j > 99:
    i = '0' + str(j)
  else:
    i = str(j)
  # if the salt added onto a 4-digit PIN has the same hash value as p,
  # then a match has been found.
  if mhashlib.sha1('YR' + i).hexdigest() == p:
    print(j)
    break
  j += 1
