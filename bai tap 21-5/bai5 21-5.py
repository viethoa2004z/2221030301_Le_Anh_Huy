m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))

tong = 0
for ch in str(n):
    tong += int(ch)

print("Tổng các chữ số của n =", tong)
if tong != 0 and m % tong == 0:
    print(m, "chia hết cho", tong)
else:
    print(m, "không chia hết cho", tong)
