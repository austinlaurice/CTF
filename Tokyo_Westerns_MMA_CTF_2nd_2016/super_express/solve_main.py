y = 76
x = 156

f = open('encrypted', 'r')
en = f.read()

ans = ''
now = 0
while now < 60:
    comp = int(en[now:now+2], 16)
    for t in range(33, 127):
        if (x * t + y) % 251 == comp:
            ans += chr(t)
            break
    now += 2

print ans

