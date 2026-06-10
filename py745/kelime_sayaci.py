import sys


class Dugum:


    def __init__(self, kelime):
        self.kelime = kelime
        self.sayi = 1


class Heap:
    def __init__(self):
 
        self.dizi = []

    def bos_mu(self):
        return len(self.dizi) == 0

    def oncelikli(self, a, b):
      
        harf_a = a.kelime[0].lower()
        harf_b = b.kelime[0].lower()
        if harf_a != harf_b:
            return harf_a < harf_b
        return a.sayi > b.sayi

    def yukari_tasi(self, i):

        while i > 0:
            ebeveyn = (i - 1) // 2
            if self.oncelikli(self.dizi[i], self.dizi[ebeveyn]):
                self.dizi[i], self.dizi[ebeveyn] = self.dizi[ebeveyn], self.dizi[i]
                i = ebeveyn
            else:
                break

    def asagi_tasi(self, i):

        n = len(self.dizi)
        while True:
            sol = 2 * i + 1
            sag = 2 * i + 2
            en_oncelikli = i
            if sol < n and self.oncelikli(self.dizi[sol], self.dizi[en_oncelikli]):
                en_oncelikli = sol
            if sag < n and self.oncelikli(self.dizi[sag], self.dizi[en_oncelikli]):
                en_oncelikli = sag
            if en_oncelikli == i:
                break
            self.dizi[i], self.dizi[en_oncelikli] = self.dizi[en_oncelikli], self.dizi[i]
            i = en_oncelikli

    def kelime_ekle(self, kelime):

        for i in range(len(self.dizi)):
            if self.dizi[i].kelime == kelime:
          
                self.dizi[i].sayi += 1
                self.yukari_tasi(i)
                return
     
        self.dizi.append(Dugum(kelime))
        self.yukari_tasi(len(self.dizi) - 1)

    def kok_cikar(self):
       
        if self.bos_mu():
            return None
        kok = self.dizi[0]
        son = self.dizi.pop()
        if not self.bos_mu():
            self.dizi[0] = son
            self.asagi_tasi(0)
        return kok


def kelimeleri_oku(yol):

    kelimeler = []
    noktalama = ".,;:!?()[]{}\"'-_/\\"
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            for parca in satir.split():
                temiz = parca.strip(noktalama)
                if temiz:
                    kelimeler.append(temiz)
    return kelimeler


def main():
    if len(sys.argv) > 1:
        yol = sys.argv[1]
    else:
        yol = input("TXT dosyasinin yolunu girin: ").strip()

    try:
        kelimeler = kelimeleri_oku(yol)
    except FileNotFoundError:
        print("Dosya bulunamadi:", yol)
        return

    if not kelimeler:
        print("Dosyada kelime bulunamadi.")
        return

    heap = Heap()

    for kelime in kelimeler:
        heap.kelime_ekle(kelime)


    print()
    print("Kelime          Sayi")
    print("--------------------")
    while not heap.bos_mu():
        dugum = heap.kok_cikar()
        print("{:<15} {}".format(dugum.kelime, dugum.sayi))


if __name__ == "__main__":
    main()
