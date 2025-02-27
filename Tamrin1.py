tarikh_tavalod = int(input('tarikh tavalod khod ra  be miladi vared konid : '))
while True:
    if (tarikh_tavalod % 4 == 0 and tarikh_tavalod % 10 == 0 and tarikh_tavalod % 400 == 0) or (tarikh_tavalod % 4 == 0 and tarikh_tavalod % 10 != 0):
        print('sale %s kabise hast' % tarikh_tavalod)
    else:
        print('sale %s kabise nist' % tarikh_tavalod)

    tarikh_tavalod = int(
        input('tarikh tavalod khod ra  be miladi vared konid : '))
