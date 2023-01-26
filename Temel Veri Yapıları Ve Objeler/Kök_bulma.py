"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem: ax^2 + bx + c

Deltayı Hesaplama : b ** 2 - 4 * a * c

Birinci kök: (-b - delta ** 0.5) / (2*a)

İkinci kök: (-b + delta ** 0.5) / (2*a)

NOT:SORU YAZARINI SORGUYA ÇEKMEYİ UNUTMA!!!
"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)

print("Birinci kök : {}\nİkinci kök : {}\n".format(x1,x2))
