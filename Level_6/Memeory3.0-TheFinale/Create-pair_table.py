import os, subprocess

f1 = open("md5-pairs.txt", 'w')

dirs = os.listdir('pics')

for i in range(len(dirs)):
    result = subprocess.check_output('md5sum pics\\' + dirs[i] + '\\*', shell=False).decode() 
    result = result.split('\r\n')

    md5s = []

    for j in range(len(result) - 1):
       md5s.append(result[j][1:33])

    md5s.sort()

    for j in range(len(md5s)):
       f1.write("%s" % md5s[j])

       if j < len(md5s) - 1:
          f1.write(',')

    f1.write('\n')

f1.close()