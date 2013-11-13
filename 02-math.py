# coding: latin-1
import math
print "#1 Mingi kolmnurk, sin(20kraadi), y külg 20m ja x külg vaja leida "
print

x = 65/math.sin(20 * math.pi/180)
print 'vastus: x = ',round(x,2),'m';



num = raw_input("#2 Sisesta mingi number mis arvutatakse cos, tan, sin = ")
s = int(num)
print "Sin: ",math.sin(s * math.pi/180)
print "Cos: ",math.cos(s * math.pi/180)
print "Tan: ",math.tan(s * math.pi/180)
