import unittest
from pengucapan import ucapkan, eja

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
# duabelas = 'dua belas'
belas = 'belas'
puluh = 'puluh'
kurang = 'kurang'
lebih = 'lebih'
seperempat = 'seperempat'
setengah = 'setengah'


class TestAngka(unittest.TestCase):
    def test_jari(self):
        self.assertEqual(eja(2), [dua])
        self.assertEqual(eja(20), [dua, puluh])
        self.assertEqual(eja(22), [dua, puluh, dua])
        self.assertEqual(eja(12), [dua, belas])


class TestJam(unittest.TestCase):

    def assertFewEqual(self, a, b):
        fewa = a[:len(b)]
        return self.assertEqual(fewa, b)

    def test_jam_menit(self):
        self.assertFewEqual(ucapkan(1, 0), [satu, tepat])
        self.assertFewEqual(ucapkan(11, 0), [sebelas, tepat])
        self.assertFewEqual(ucapkan(12, 0), [dua, belas, tepat])

    def test_perempat(self):
        self.assertFewEqual(ucapkan(1, 15), [satu, seperempat])
        self.assertFewEqual(ucapkan(11, 15), [sebelas, seperempat])
        self.assertFewEqual(ucapkan(11, 30), [setengah, dua, belas])
        self.assertFewEqual(ucapkan(11, 45), [dua, belas, kurang, seperempat])

    def test_lebih(self):
        self.assertFewEqual(ucapkan(1, 5), [satu, lebih, lima])
        self.assertFewEqual(ucapkan(1, 10), [satu, lebih, sepuluh])
        self.assertFewEqual(ucapkan(11, 20), [sebelas, lebih, dua, puluh])
        self.assertFewEqual(
            ucapkan(12, 25), [dua, belas, lebih, dua, puluh, lima])
        # self.assertFewEqual(ucapkan(11, 45), [dua, belas, kurang, seperempat])

    def test_kurang(self):
        self.assertFewEqual(ucapkan(10, 55), [sebelas, kurang, lima])
        self.assertFewEqual(ucapkan(1, 50), [dua, kurang, sepuluh])
        self.assertFewEqual(ucapkan(11, 40), [dua, belas, kurang, dua, puluh])
        self.assertFewEqual(ucapkan(11, 45), [dua, belas, kurang, seperempat])
