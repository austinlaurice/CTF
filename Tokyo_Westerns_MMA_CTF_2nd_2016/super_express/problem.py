import sys
key = '****CENSORED***************'
flag = 'TWCTF{*******CENSORED********}'

#flag length 30

if len(key) % 2 == 1:
    print("Key Length Error")
    sys.exit(1)

n = len(key) / 2
encrypted = ''
for c in flag:
    c = ord(c)
    for a, b in zip(key[0:n], key[n:2*n]):
        c = (ord(a) * c + ord(b)) % 251
    encrypted += '%02x' % c

print encrypted


(a(a(ac + b) + b)+b)

a3(a2a1c + a2b1 + b2)
