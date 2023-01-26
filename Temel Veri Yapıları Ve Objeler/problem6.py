print("""

Problem 6
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2

""")

a = int(input("Karşı Dik Kenar:"))
b = int(input("Komşu Dik Kenar:"))

x1 = a ** 2 + b ** 2

print("Hipotenüs : {} ".format(x1))
