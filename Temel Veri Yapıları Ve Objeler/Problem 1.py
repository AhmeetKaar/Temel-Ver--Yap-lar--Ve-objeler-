print("""

Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.

""")





a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))
c = int(input("Üçüncü Sayı:"))

x1 = a
x2 = b
x3 = c

print("{} * {} * {} sonucu {} 'dir.".format(x1,x2,x3,x1 * x2 * x3))
