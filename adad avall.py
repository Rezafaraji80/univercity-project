n = int(input("megedar 'N' ra vared konid : "))
k = int(input("megedar 'K' ra vared konid : "))
count = 0
x = 0
adad_aval = []
y = 0

while count < k:

    for i in range(2, n):
        if n % i == 0:
            x = 1

    if x == 0:
        adad_aval.append(n)
        count += 1

    n += 1
    x = 0


print(adad_aval)
