#!/usr/bin/python

import os

for i in range(1, 12):
    os.system('wget -q -r http://46.101.107.117:2107')
    os.system('copy "46.101.107.117+2107\pic" pics')
    os.system('ren pics\*. *-' + str(i) + '.jpg')
