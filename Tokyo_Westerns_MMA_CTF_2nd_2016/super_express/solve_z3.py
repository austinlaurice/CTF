from z3 import *

x = Int('x')
y = Int('y')

s = Solver()
s.add( (x * ord('T') + y) % 251 == 0x80)
s.add( (x * ord('W') + y) % 251 == 0x5e)
s.add( (x * ord('C') + y) % 251 == 0xed)
s.add( (x * ord('F') + y) % 251 == 0xcb)
s.add( (x * ord('{') + y) % 251 == 0xbc)
s.add( (x * ord('}') + y) % 251 == 0xf9)
s.add( x < 251)
s.add( x >= 0)
s.add( y >= 0)
s.add( y < 251)

print(s.check())
print(s.model())
