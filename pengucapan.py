angka = {
    0: 'tepat',
    1: 'satu',
    2: 'dua',
    3: 'tiga',
    4: 'empat',
    5: 'lima',
    6: 'enam',
    7: 'tujuh',
    8: 'delapan',
    9: 'sembilan',
    10: 'sepuluh',
    11: 'sebelas',
    12: 'dua belas',
}


def eja(n):
    lut1 = ['nol', 'satu', 'dua', 'tiga', 'empat',
            'lima', 'enam', 'tujuh', 'delapan', 'sembilan',
            'sepuluh', 'sebelas', 'dua belas', 'tiga belas',
            'empat belas', 'lima belas', 'enam belas',
            'tujuh belas', 'delapan belas', 'sembilan belas']

    lut20 = ['x', 'x', 'dua puluh', 'tiga puluh', 'empat puluh',
             'lima puluh', 'enam puluh', 'tujuh puluh', 'delapan puluh',
             'sembilan puluh']

    triples = ['x', 'ribu', 'juta', 'miliar',
               'biliar', 'quadrillion', 'quintillion',
               'sextillion', 'septillion', 'octillion',
               'nonillion', 'decillion']

    words = []
    shift = 0
    hasNumber = False
    insertpos = -1
    while n > 0:
        ones = n % 10
        shiftmod = shift % 3
        shiftdiv = shift / 3
        if shiftdiv > 0 and shiftmod == 0:
            insertpos = len(words)
            hasNumber = False
        if shiftmod == 2 and ones > 0:
            words.append('ratus')
            words.append(lut1[ones])
            hasNumber = True
        if shiftmod == 1 and ones > 0:
            words.append(lut20[ones])
            hasNumber = True
        if shiftmod == 0:
            tens = n % 100
            if 0 < tens < 20:
                words.append(lut1[tens])
                shift += 1
                n = n / 10
                hasNumber = True
            elif ones > 0:
                words.append(lut1[ones])
                hasNumber = True
        if hasNumber and insertpos >= 0:
            words.insert(insertpos, triples[shiftdiv])
            insertpos = -1
            hasNumber = False
        n = n / 10
        shift += 1
        # oldones = ones
    words.reverse()
    text = ' '.join(words)
    result = text.split(' ')
    return result
    # return words if words else ['nol']


def mid(n):
    "around `n` +/- 1"
    return [n-1, n, n+1]


def ucapkan(h, m):
    # jam = angka.get(h)
    # menit = angka.get(m)
    jam = eja(h)
    menit = eja(m)
    waktu = []
    if m in mid(0) + [59]:
        waktu = [jam, 'tepat']
    elif m in mid(15):
        waktu = [jam, 'seperempat']
    elif m in mid(30):
        jam = eja(h+1)
        waktu = ['setengah', jam]
    elif m in mid(45):
        jam = eja(h+1)
        waktu = [jam, 'kurang', 'seperempat']
    elif m < 30:
        waktu = [jam, 'lebih', menit]
    else:
        # waktu = [jam, menit]
        jam = eja(h+1)
        menit = eja(abs(60-m))
        waktu = [jam, 'kurang', menit]

    return flattened(waktu)


def flattened(arr):
    words = []
    for r in arr:
        if isinstance(r, list):
            words += r
        else:
            words.append(r)
    text = ' '.join(words)
    result = text.split(' ')
    return result
