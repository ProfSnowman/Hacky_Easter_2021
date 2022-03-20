#/usr/bin/python

encsha1s  = ["4ab56415e91e6d5172ee79d9810e30be5da8af18", "c19a3ca5251db76b221048ca0a445fc39ba576a0"]
encsha1s += ["fdb2c9cd51459c2cc38c92af472f3275f8a6b393", "6d586747083fb6b20e099ba962a3f5f457cbaddb"]
encsha1s += ["5587adf42a547b141071cedc7f0347955516ae13"]

sha1s = []

for i in range(len(encsha1s)):
    hash = ''
 
    for j in range(len(encsha1s[i])):
        ch = encsha1s[i][j]

        if ch in 'abcdef':
           ch = chr(ord(ch) + 3)

           if ch > 'f':
              ch = chr((ord(ch) - ord('f')) + 96)

        hash += ch

    sha1s.append(hash)

for i in range(len(sha1s)):
    print("%s" % sha1s[i])