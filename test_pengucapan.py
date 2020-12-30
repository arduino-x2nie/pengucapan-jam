import unittest
from pengucapan import ucapkan

tepat = 'tepat'
satu = 'satu'
dua = 'dua'
tiga = 'tiga'
empat = 'empat'
lima = 'lima'
enam = 'enam'
tujuh = 'tujuh'
delapan = 'delapan'
sembilan = 'sembilan'
sepuluh = 'sepuluh'
sebelas = 'sebelas'
duabelas = 'dua belas'

class TestDict(unittest.TestCase):

    def assertFewEqual(self, a, b):
        fewa = a[:len(b)]
        return self.assertEqual(fewa, b)
    
    def test_jam_menit(self):
        self.assertEqual(ucapkan(1,0), [satu,tepat])