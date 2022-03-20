#!/usr/bin/python3

import jwt

def decode_jwts(jwts):
    decode_lvl = jwt.decode(jwts, options={"verify_signature": False})
    
    for key in decode_lvl.keys():
       if key in ['i', 'ii', 'iii', 'iv', 'v', 'vi']:
          print('%s\t%s' % (key, decode_lvl[key]))
          
 
       elif not decode_lvl[key] in ['no{flag}' , 'he']:
          decode_jwts(decode_lvl[key])

f1 = open('jwts.txt')
jwts = f1.read()
f1.close()

decode_jwts(jwts)