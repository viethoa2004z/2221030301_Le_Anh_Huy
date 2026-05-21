a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

tong = a + b + c

print("Tong =", tong)

dem = 0

for ch in str(tong):
    if int(ch) % 2 == 0:
        dem = dem + 1

print("So chu so chan trong tong la:", dem)
