n = int(input("Nhap so luong phan tu: "))

a = []

for i in range(n):
    x = int(input(f"Nhap phan tu thu {i + 1}: "))
    a.append(x)

tong = 0

for x in a:
    la_nguyen_to = True

    if x < 2:
        la_nguyen_to = False
    else:
        for i in range(2, x):
            if x % i == 0:
                la_nguyen_to = False
                break

    if la_nguyen_to:
        tong = tong + x

print("Tong cac so nguyen to la:", tong)

if tong % 2 != 0 and tong > 50:
    print("Tong la so le va lon hon 50")
else:
    print("Tong khong thoa man")