print("""

Problem 5
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

""")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))

a,b = b,a

print("Birinci Sayı : {}\nİkinci Sayı : {}".format(a,b))
