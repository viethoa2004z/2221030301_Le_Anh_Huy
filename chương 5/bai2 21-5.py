n = int(input("Nhập số nguyên dương n: "))
tong = 0
for ch in str(n):
    tong += int(ch)

print("Tổng các chữ số =", tong)
if tong % 3 == 0:
    print("Tổng chia hết cho 3")
else:
    print("Tổng không chia hết cho 3")
