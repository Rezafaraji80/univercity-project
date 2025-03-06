import math

print('baraye mohasebe rishe hay yek moadele daraje 2 be sorat "ax^2+bx=c=0" zarayeb khasye shode ra vared konid! \n')
a = int(input('magdar "a" ra vared konid :'))
b = int(input('magdar "b" ra vared konid :'))
c = int(input('magdar "c" ra vared konid :'))
print('moadele barabar ba %dX^2 + %dX + %d = 0 ast.' % (a, b, c))
delta = b**2-(4*a*c)

if delta > 0:
    radikal_delta = math.sqrt(delta)
    x1 = (-b+radikal_delta)/(2*a)
    x2 = (-b-radikal_delta)/(2*a)
    print('in moadele do rishe hagigi %f va %f darad.' % (x1, x2))

elif delta == 0:
    x1 = (-b)/(2*a)
    print('in moadele yak rishe hagigi %f darad.' % x1)

else:
    print('in moadele rishe hagigi nadarad')
