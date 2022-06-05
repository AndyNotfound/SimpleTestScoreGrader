nim = int(input('NIM anda? '))
nilaiUts = int(input('Nilai UTS? '))
nilaiUas = int(input('Nilai UAS? '))

totalNilai = (nilaiUts + nilaiUas) / 2

def abjadNilai(num):
    if num <= 29:
        return 'F'
    elif num >= 90:
         return 'A'
    elif num >= 80:
         return 'B+'
    elif num >= 70:
         return 'B'
    elif num >= 60:
         return 'C+'
    elif num >= 50:
         return 'C'
    elif num >= 40:
         return 'D'
    elif num >= 30:
         return 'E'
    else:
        print('what the hell')
    return num

abjadNilai = abjadNilai(totalNilai)

if abjadNilai == 'F' or abjadNilai == 'E' or abjadNilai == 'D':
    print('Tidak Lulus')
else:
    print('Lulus')