#!/usr/bin/python3

import hashlib, os, requests

f1 = open("md5-pairs.txt", 'r')
pairvals = f1.readline()

pairtable = []

while pairvals:
    pairtable.append(pairvals.rstrip('\n').split(','))
    pairvals = f1.readline()

f1.close()
 
s = requests.Session()
rounds = 0

while rounds < 10:
    md5s = []
    s.get('http://46.101.107.117:2107/')

    for i in range(98):
       resp = s.get('http://46.101.107.117:2107/pic/' + str(i + 1))
       m = hashlib.md5()
       m.update(resp.content)
       md5s.append([])
       md5s[i].append(m.hexdigest())
       md5s[i].append(i + 1)

    md5s.sort()

    num = 0
    pairs = []

    while len(md5s) > 0:
       curmd5 = md5s[0][0]
       pairs.append([])
       pairs[num].append(md5s[0][1])
       pairs[num].append('')
       md5s.remove(md5s[0])

       found = False
       i = 0

       while i < len(pairtable) and found == False:
          for j in range(len(pairtable[i])):
             if pairtable[i][j] == curmd5:
                pair_row = i
                found = True

          if found == False:
            i += 1

       if found == True:
          found = False
          i = 0
          row = pair_row

          while i < len(md5s) and found == False:
             for j in range(len(pairtable[row])):
                if pairtable[row][j] == md5s[i][0]:
                   pair_row = i
                   found = True

             if found == False:
                i += 1
           
          if found == True:
             pairs[num][1] = md5s[pair_row][1]
             md5s.remove(md5s[pair_row])

       num += 1
    
    if len(pairs) == 49:
       for i in range(len(pairs)):
          d = 'first=' + str(pairs[i][0]) + '&second=' + str(pairs[i][1])
          header = {"Content-Type": "application/x-www-form-urlencoded"}
          resp = s.post('http://46.101.107.117:2107/solve', data = d, headers=header)

       rounds += 1

       if resp.text == "nextRound":
          print('Round %s' % rounds)

       else:
          print(resp.text)
