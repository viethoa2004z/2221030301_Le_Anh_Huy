n = int(input("Mời nhập số lượng phần tử n: "))
a = []
for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
    a.append(x)

tong = 0
for x in a:
    if x % 2 == 0:
        tong += x

print("Tổng các số chẵn =", tong)
if tong % 7 == 0 and tong < 200:
    print("Tổng chia hết cho 7 và nhỏ hơn 200")
else:
    print("Không thỏa mãn điều kiện")
