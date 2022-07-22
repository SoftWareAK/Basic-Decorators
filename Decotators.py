#python'da decarators'lar ,argüman olarak fonksiyon alıp,
#sonuçta yine fonksiyon döndüren fonksiyonlara denir.


def linkYap(f):
    def yaz():
        return "<a href='http://www." + f() +".com'>link</a> "
    return yaz

def adres():
    return "google"
a=linkYap(adres)
print(a())

@linkYap     #fonksiyonu deceratora bağlama
def adr():
    return "python"
print(adr())
