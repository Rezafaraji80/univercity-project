t = -20
f = ((2*t)**3)+((2*t)**2)+t+6
f_prime = ((6*t)**2)+(4*t)+1
print("megh  dar F = %f va f' = %f ast" % (f, f_prime))
ti = f/f_prime
print("f tagsim bar f' = ", ti)
ti_ = t - ti
i = 1
while i < 200:

    print('nogtehe badi = ', ti_)
    f = ((2*t)**3)+((2*t)**2)+t+6
    f_prime = ((6*t)**2)+(4*t)+1

    if abs(f_prime) > 0.000000001:

        if f != 0:

            print("megh  dar F = %f va f' = %f ast" % (f, f_prime))
            ti = f/f_prime
            print("f tagsim bar f' = ", ti)
            ti_ = t - ti
            t = ti_
            i = i + 1

        if abs(f) < 0.000000001:
            if abs(f) != 0:
                print(
                    'rishe moadele "F" ba %d bar talash taghriban barabar ast ba = %f' % (i, ti_))

            else:
                print(
                    'rishe moadele "F" ba %d bar talash dagigan barabar ast ba = %f' % (i, ti_))
            break

    else:
        print('megdar moshtag "F" barabr ba 0 ast bo meghdar digar test konid ')
        break

if i == 200:
    print('modele hamgera nashod!')
