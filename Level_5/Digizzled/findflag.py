#!/usr/bin/python

import sys

if len(sys.argv) < 3:
    print("Usage:\tpython findflag.py <wordlist> <hash>\n")
    print("\twordlist\t- dictionary/wordlist file\n")
    print("Example:\n")
    print("\tpython findflag.py lower.txt 3a940588")

else:
    wrdlst = sys.argv[1]
    s1 = int(sys.argv[2], 16) & 0xffff
    s2 = int(sys.argv[2], 16) >> 16

    start = 'he2021{'
    end = '}'

    try:
       ## Open the wordlist file with read only permit
       f1 = open(wrdlst)

    except IOError:
       print("File %s does not exist." % wrdlst)

    else:
       ## Read the first word from the wordlist file 
       word = f1.readline()

       ## If the file is not empty keep reading one line at a time
       ## till the file is empty

       foundflag = False

       while word and foundflag == False:
          flag = start + word.strip('\n') + end
          cur_s1 = s1
          cur_s2 = s2
          
          for i in range(len(flag)):
             found = False
             x = cur_s2

             while found == False:
                if cur_s1 * x % 65521 == cur_s2:
                   found = True
                
                else:
                   x -= 1
 
                   if x == 0:
                      x = 65521

             cur_s2 = x             
             cur_s1 = cur_s1 - ord(flag[i]) % 65521

          if cur_s1 == 13 and cur_s2 == 37:
             foundflag = True
          
          else:
             word = f1.readline()

       if foundflag:
          print('flag: %s' % word)

       f1.close()