import telnetlib
from random import randint

table = [[randint(0, 1) for x in range(0, 3)] for y in range(0, 3)] 
history = [[], [], []]
def connect_server():
    IP = 'ppc1.chal.ctf.westerns.tokyo'
    PORT = 15376
    s = telnetlib.Telnet(IP, PORT)
    return s

def colmax(last):
    global table
    m = -1
    ret = 0
    for i in range(0, 3):
        if(m < table[last][i]):
            m = table[last][i]
            ret = i
    return (ret + 1)%3, m
    
def solve():
    global table
    print table
    arr = ['R\n', 'P\n', 'S\n']
    dic = {'Rock':0, 'Paper': 1, 'Scissors':2}
    s = connect_server()
    last = 0
    i = 0
    s.read_until('Rock? Paper? Scissors? [RPS]')
    while i < 50:
        apponent, max_num = colmax(last)
        c = (apponent + 1) % 3
        s.write(arr[c])
        now = s.read_until('\n').replace('\n', '')
        #print now
        now = now.split('-')
        real_max = (dic[now[1]] + 3 - 1)%3
        print history
        if history[last] != []:
            if history[last][-1] == real_max:
                pass
            elif history[last][-1] < real_max:
                table[last][real_max] = table[last][history[last][-1]] + 1
            elif history[last][-1] > real_max:
                table[last][real_max] = table[last][history[last][-1]]
        else:
            if(i <= 20):
                table[last][real_max] = max_num + randint(1, 3)
            else:
                table[last][real_max] = max_num + 1

        history[last].append(real_max)
        table[last][c] += 1
        last = c
        tmp = s.read_until('Rock? Paper? Scissors? [RPS]')
        print tmp
        if 'Congrats' in tmp:
            return True
        i += 1
    return False
i = 0
while(i < 100):
    table = [[randint(0, randint(1, 4)) for x in range(0, 3)] for y in range(0, 3)] 
    history = [[], [], []]

    #table = [[0 for x in range(0, 3)] for y in range(0, 3)] 
    if solve():
        break
    i += 1

